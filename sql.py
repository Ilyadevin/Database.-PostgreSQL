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


def create_db():  # создает таблицы

    cur.execute('''CREATE TABLE STUDENT
         (ID_S SERIAL PRIMARY KEY NOT NULL,
         NAME TEXT NOT NULL,
         GPA NUMERIC(10,2),
         BIRTH TIMESTAMP WITH TIME ZONE);
         ''')
    connection.commit()

    cur.execute('''CREATE TABLE COURSE
             (ID_C SERIAL PRIMARY KEY NOT NULL,
             NAME CHARACTER VARYING(100) NOT NULL);
             ''')
    connection.commit()

    cur.execute('''CREATE TABLE STUDENTS_AND_COURSES
                (ID_1 SERIAL PRIMARY KEY,
                STUDENT_ID INTEGER REFERENCES STUDENT(ID_S),
                COURSE_ID INTEGER REFERENCES COURSE(ID_C));
                ''')

    connection.commit()


create_db()


class WorkWithSQL:
    def __init__(self):
        pass

    def get_students(self, course_id):
        cur.execute('SELECT STUDENT.ID_S, STUDENT.NAME, STUDENT.GPA, STUDENT.BIRTH, COURSE.ID_C, COURSE.NAME'
                    ' FROM STUDENT INNER JOIN COURSE ON COURSE.ID_C = %s;',
                    (course_id,))

        print(cur.fetchall())

        return cur.fetchall()

    def add_students(self, students, course_id):
        cur.execute('INSERT INTO STUDENT(NAME) VALUES(%s) RETURNING ID_S;',
                    (students,))
        id_from_student = cur.fetchall()[0]

        cur.execute('INSERT INTO COURSE(NAME) VALUES(%s)RETURNING ID_C;',
                    (course_id,))
        id_from_course = cur.fetchall()[0]

        cur.execute('INSERT INTO STUDENTS_AND_COURSES(STUDENT_ID, COURSE_ID) VALUES(%s, %s);',
                    (id_from_student, id_from_course,))

        connection.commit()

        print("Студент(ы): ", students, 'добавлен(ы) в список студентов и на курс ', course_id)

        print('Данные о студенте(ах) добавлены!')

        return connection.commit()

    def add_student(self, student):
        cur.execute('INSERT INTO STUDENT(NAME) VALUES(%s);',
                    (student,))

        connection.commit()

        print(student, "добавление выполнено успешно!")

        return connection.commit()

    def get_student(self, student_id):
        cur.execute('SELECT NAME FROM STUDENT WHERE ID_S=%s;',
                    (student_id,))

        return cur.fetchall()


SQL = WorkWithSQL()
SQL.get_student(input('Студентов какого курса необходимо получить? '))
SQL.add_students(input('Введите имя студента для записи: '), input('Введите курс на который нужно записать студента: '))
SQL.add_student(input('Введите имя студента, без записи на курс: '))
SQL.get_student(input('Студент по сирийному номеру: '))

cur.close()
connection.close()
