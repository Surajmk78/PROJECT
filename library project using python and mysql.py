import mysql.connector as mysql
connection = mysql.connect(user='root',password='7028996272',host='localhost',database='library')
cursor = connection.cursor()

def display():
	show = """select * from books"""
	cursor.execute(show)
	showed = cursor.fetchall()
	print("\n")
	for i in showed:
		print(i)

def addbook():
	bookname = input("Enter tha name of book:  ")
	add = """insert into books (bookname) values (%s);"""
	record = [bookname]
	cursor.execute(add,record)
	connection.commit()
	print("book added")

def rentbook():
	booknamed = input("enter tha book of name :  ")
	usernamed = input("enter your name:  ")
	record = [booknamed]
	record2 = [booknamed,usernamed]
	dels = """delete from books where bookname = %s;"""
	rented = """insert into rentbooks (bookname,username) values (%s,%s);"""
	cursor.execute(dels,record)
	print("Book removed from library")
	cursor.execute(rented,record2)
	connection.commit()
	print("Book added to rented table")


def returnbook():
	bookn = input("Enter ta name of book you want to return:	")
	deld = """delete from rentbooks where bookname = %s;"""
	store = [bookn]
	cursor.execute(deld,store)
	print("book removed from rented table")
	ins = """insert into books (bookname) values (%s);""" 
	cursor.execute(ins,store)
	connection.commit()




while True:
	print("\n1.Display books\n2.add book\n3.rent a book\n4.return book")
	user_choice = int(input("Enter your choice:	"))
	if user_choice == 1:
		display()
	elif user_choice == 2:
		addbook()
	elif user_choice == 3:
		rentbook()
	elif user_choice == 4:
		returnbook()
	else:
		print("Wrong input")
	ask = input("\nYou want to continue\nType y or n:  ")
	if ask == "y":
		continue
	elif ask == "n":
		break
	else:
		print("Type y or n\ncontinued")

cursor.close()
connection.close()