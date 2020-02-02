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
         (ID SERIAL PRIMARY KEY NOT NULL,
         NAME TEXT NOT NULL,
         GPA NUMERIC(10,2),
         BIRTH TIMESTAMP WITH TIME ZONE
         )''')
    connection.commit()

    cur.execute('''CREATE TABLE COURSE
             (ID SERIAL PRIMARY KEY NOT NULL,
             NAME CHARACTER VARYING(100) NOT NULL
             )''')
    connection.commit()


create_db()


def get_students(course_id):  # возвращает студентов определенного курса
    cur.execute('SELECT NAME FROM COURSE WHERE ID=%s',
                (course_id,))
    return cur.fetchall()


get_students('1')


def add_students(students, course_id):  # создает студентов и
    cur.execute('INSERT INTO STUDENT(NAME) VALUES(%s)',
                (students,))
    cur.execute('insert into COURSE(NAME) VALUES(%s)',
                (course_id,))

    return connection.commit()


add_students('Дмитрий', '9')


def add_student(student):  # просто создает студента
    cur.execute('INSERT INTO STUDENT(NAME) VALUES(%s)',
                (student,))
    connection.commit()
    print(student, "Добавление выполнено успешно!")


add_student('Дмитрий')


def get_student(student_id):
    cur.execute('SELECT NAME FROM COURSE WHERE ID=%s;',
                (student_id,))
    return cur.fetchall()


get_student('1')

cur.close()
connection.close()
