import mysql.connector as mysql
connection = mysql.connect(host='localhost',user='root',password='7028996272',database='college')
cursor = connection.cursor()

#q = '''create database college;'''
#cursor.execute(q)
#qq = '''use college'''
#cursor.execute(qq)
#qqq = '''create table users (username varchar(200), password varchar(200), type varchar(200));'''
#cursor.execute(qqq)
#connection.commit()
#qqqq = '''create table student (roll_no int(100), username varchar(200), password varchar(200), marks int(100), result varchar(100));'''
#cursor.execute(qqqq)
#connection.commit()
#tables created successfully.

def add_user():
	privilege = input("Enter student or teacher: ")
	username = input(f"Enter {privilege}'s username: ")
	password = input(f"Enter {privilege}'s password: ")
	q1 = '''insert into users (username,password,type) values (%s,%s,%s);'''
	data1 = (username,password,privilege)
	cursor.execute(q1,data1)
	connection.commit()
	print(f"{username}'s values inserted")

def delete_user():
	d_username = input("Enter username: ")

	q2 = '''delete from users where username = %s;'''
	cursor.execute(q2,(d_username,))
	connection.commit()
	print(f"{d_username} deleted successfully")

#teacher can add student's roll number, result here
def teacher():
	print("\nEnter studentdetails: ")
	s_username = input("Enter sudent's username: ")
	s_password = input("Enter student's password: ")
	q4 = '''select * from users where username = %s;'''
	cursor.execute(q4,(s_username,))
	val2 = cursor.fetchall()
	for i in val2:
		s_user = i[0]
		s_pass = i[1]
	if s_username == s_user:
		if s_password == s_pass:
			roll_no = int(input("Enter roll number of student: "))
			marks = int(input("Enter student's marks: "))
			result = input("Enter Pass or Fail: ")
			q5 = '''insert into student (roll_no,username,password,marks,result) values (%s,%s,%s,%s,%s);'''
			data5 = (roll_no,s_username,s_password,marks,result)
			cursor.execute(q5,data5)
			connection.commit()
			print("student details entered successfully")
			

#here students can see his/her details.
def students():
	q7 = '''select * from student where username = %s;'''
	cursor.execute(q7,(stud_username,))
	val7 = cursor.fetchall()
	for i in val7:
		print("Roll no: ",i[0])
		print("Marks  : ",i[3])
		print("Result : ",i[4])


while True:
	print("\nChoose the following\n1. admin\n2. Teacher\n3. Student")
	choice = int(input("Enter 1 or 2 or 3:  "))
	if choice == 1:
		a_username = input("Enter admin's username: ")
		a_password = input("Enter admin's password: ")
		if a_username=="admin":
			if a_password == "admin":
				while True:
					print("\nChoose number mention before your work:\n1.Add new Student/Teacher\n2.Delete existing teacher/Student\n3.Logout ")
					choice2 = int(input("Enter Your choice:  "))
					if choice2 == 1:
						add_user()
					elif choice2 == 2:
						delete_user()
					elif choice2 == 3:
						break
					else:
						print("invalid input")
						break
			else:
				print("Wrong password")
		else:
			print("Wrong username")
	elif choice == 2:
		t_username = input("Enter your username: ")
		t_password = input("Enter your password: ")
		q3 = '''select * from users where username = %s;'''
		cursor.execute(q3,(t_username,))
		val = cursor.fetchall()
		for i in val:
			t_user = i[0]
			t_pass = i[1]
		if t_user == t_username:
			if t_pass == t_password:
				print("Login successfully")
				teacher()
	elif choice == 3:
		stud_username = input("Enter your username: ")
		stud_password = input("Enter your password: ")
		q6 = '''select * from users where username = %s;'''
		cursor.execute(q6,(stud_username,))
		val6 = cursor.fetchall()
		for i in val6:
			stud_user = i[0]
			stud_pass = i[1]
		if stud_username == stud_user:
			if stud_password == stud_pass:
				students()
			else:
				print("Invalid password")
		else:
			print("Invalid username")
				