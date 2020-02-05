import psycopg2
import datetime

dt = datetime.datetime.now()
connection = psycopg2.connect(
    database="main_data_db",
    user="ilya_erlingas",
    password="3322879",
    host="127.0.0.1",
    port="5432"
)
cur = connection.cursor()
print("Database opened successfully")


# def create_db():  # создает таблицы
#
#     cur.execute('''CREATE TABLE STUDENT
#          (ID_STUDENT SERIAL PRIMARY KEY NOT NULL,
#          NAME TEXT NOT NULL,
#          GPA NUMERIC(10,2),
#          BIRTH TIMESTAMP WITH TIME ZONE);
#          ''')
#     connection.commit()
#
#     cur.execute('''CREATE TABLE COURSE
#              (ID_COURSE SERIAL PRIMARY KEY NOT NULL,
#              NAME CHARACTER VARYING(100) NOT NULL);
#              ''')
#     connection.commit()
#
#     cur.execute('''CREATE TABLE STUDENTS_AND_COURSES
#                 (ID_1 SERIAL PRIMARY KEY,
#                 STUDENT_ID INTEGER REFERENCES STUDENT(ID_STUDENT),
#                 COURSE_ID INTEGER REFERENCES COURSE(ID_COURSE));
#                 ''')
#
#     connection.commit()
#
#
# create_db()


def get_students(course_id):  # возвращает студентов определенного курса
    cur.execute('SELECT STUDENT.ID_STUDENT, STUDENT.NAME, STUDENT.GPA, STUDENT.BIRTH, COURSE.ID_COURSE, COURSE.NAME'
                ' FROM STUDENT INNER JOIN COURSE ON COURSE.ID_COURSE = STUDENT.ID_STUDENT;',
                (course_id,))
    print(cur.fetchall())
    return cur.fetchall()


get_students('1')


def add_students(students, course_id):  # создает студентов и
    cur.execute('INSERT INTO STUDENT(NAME) VALUES(%s);',
                (students,))
    cur.execute('INSERT INTO COURSE(NAME) VALUES(%s);',
                (course_id,))
    name_id = cur.execute('SELECT ID_STUDENT FROM STUDENT WHERE NAME=%s',
                          (students,))
    course_id_1 = cur.execute('SELECT ID_COURSE FROM COURSE WHERE ID_COURSE=%s;',
                              course_id)
    cur.execute('INSERT INTO STUDENTS_AND_COURSES(STUDENT_ID, COURSE_ID) VALUES(%s, %s);',
                (name_id, course_id_1,))
    connection.commit()
    print("Студент(ы): ", students, 'добавлен(ы) в список студентов и на курс ', course_id)
    print('Данные о студенте(ах) добавлены!')
    return connection.commit()


add_students('Игорь', '9')


def add_student(student):  # просто создает студента
    cur.execute('INSERT INTO STUDENT(NAME) VALUES(%s);',
                (student,))
    connection.commit()
    print(student, "добавление выполнено успешно!")
    return connection.commit()


add_student('Карина')


def get_student(student_id):
    cur.execute('SELECT NAME FROM STUDENT WHERE ID_STUDENT=%s;',
                (student_id,))
    return cur.fetchall()


get_student('1')

cur.close()
connection.close()
