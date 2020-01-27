import psycopg2

connection = psycopg2.connect(
  database="main_data_db",
  user="ilya_erlingas",
  password="3322879",
  host="127.0.0.1",
  port="5432"
)
cur = connection.cursor()
print("Database opened successfully")


def create_db():    # создает таблицы
    cur.execute('''CREATE TABLE STUDENT  
         (ID INT PRIMARY KEY NOT NULL,
         NAME TEXT NOT NULL,
         GPA NUMERIC(10,2),
         BIRTH TIMESTAMP WITH TIME ZONE;''')
    cur.execute('''CREATE TABLE COURSE  
             (ID INT PRIMARY KEY NOT NULL,
             NAME CHARACTER VARYING(100) NOT NULL,;''')


def get_students(course_id):    # возвращает студентов определенного курса
    for name in cur.execute('SELECT NAME FROM CURSE WHERE NAME={course_id};'):
        print(name)


def add_students(course_id, students):  # создает студентов и
    for course_id, students in cur.execute('INSERT INTO STUDENT (ID, NAME, GPA, BIRTH) VALUES(1, "Игорь", 10, 112);', course_id, students):  # записывает их на курс
        print({students}, "Добавлен в базу")
        print(course_id)


def add_student(student): # просто создает студента
    for student in cur.execute('INSERT INTO STUDENT(NAME) VALUES("Диана");', student):
        print(student, "Добавление выполнено успешно!")


def get_student(student_id):
    for id_1 in cur.execute('SELECT ID FROM STUDENT WHERE ID=student_id;'):
        print(id_1)


connection.close()
