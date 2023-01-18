import mysql.connector as mysql
connection = mysql.connect(user='root',password='7028996272',host='localhost',database='bank')
cursor = connection.cursor()

#	OPEN NEW ACCOUNT

def new_acc():
	name = input("Enter your name:  ")
	acc_no = int(input("enter account number:  "))
	ph_no = int(input("Enter contact number : "))
	dob = input("Enter date of birth:  ")
	aadhar_no = int(input("Enter aadhar number :  "))
	ope_amt = int(input("Enter opening amount:  "))

	data1 = (name,acc_no,ph_no,dob,aadhar_no,ope_amt)
	q1 = """insert into account values (%s,%s,%s,%s,%s,%s);"""
	cursor.execute(q1,data1)
	connection.commit()
	print("Values inserted successfully")

#	DEPOSIT AMOUNT

def deposit_amount():
	amt = int(input("enter amount between 10-100:  "))
	acc2 = int(input("Enter account number :  "))
	acc = [(acc2)]
	q1 = """select amount from account where acc_no = %s;"""
	cursor.execute(q1,acc)
	val = cursor.fetchone()
	val2 = ((amt + val[0]))
	q2 = """update account set amount = %s where acc_no = %s;"""
	aa = (val2,acc2)
	cursor.execute(q2,aa)
	connection.commit()
	print("Amount credited successfully")
#deposit_amount()

#	WITHDRAW AMOUNT

def withdraw_amount():
	acc = int(input("Enter account number:  "))
	q1 = """select amount from account where acc_no = %s;"""
	data1 = (acc,)
	cursor.execute(q1,data1)
	val = cursor.fetchone()
	amt = int(input("Enter amount you want to remove:  "))
	val2 = ((val[0] - amt))
	q2 = """update account set amount = %s where acc_no = %s;"""
	bb = (val2,acc)
	cursor.execute(q2,bb)
	connection.commit()
	print("Amount withdrawn successfully")
	
#withdraw_amount()

#	BALANCE ENQUIRY

def balance_enquiry():
	acc = int(input("Enter account number:  "))
	q1 = """select amount from account where acc_no = %s;"""
	data1 = (acc,)
	cursor.execute(q1,data1)
	val = cursor.fetchone()
	print("Your balance is ",val[0])
#balance_enquiry()

#	DISPLAY CUSTOMER DETAILS

def display_details():
	acc = int(input("Enter account number:  "))
	q1 = """select * from account where acc_no = %s;"""
	cursor.execute(q1,(acc,))
	val = cursor.fetchall()
	for i in val:
		print("name: ",i[0],"\naccount number: ",i[1],"\nPhone number: ",i[2],"\nDate of birth: ",i[3],"\nAadhar number: ",i[4],"\nAmount: ",i[5],"\n")

#display_details()

#	CLOSE AN ACCOUNT

def close_account():
	acc = int(input("Enter account number:  "))
	q1 = """delete from account where acc_no = %s;"""
	cursor.execute(q1,(acc,))
	connection.commit()
	print("account deleted")
#close_account()

while True:
	print("1.Open new account\n2. Deposit amount\n3. Withdrawn amount\n4. balance enquiry\n5. Display customer details\n6. Close an account") 
	choice = int(input("Enter your choice between 1 and 6:  "))
	if choice == 1:
		new_acc()
	elif choice == 2:
		deposit_amount()
	elif choice == 3:
		withdraw_amount()
	elif choice == 4:
		balance_enquiry()
	elif choice == 5:
		display_details()
	elif choice == 6:
		close_account()
	else:
		print("Invalid input")
	ask = input("Want to continue\nType y or n:  ")
	if ask == "y":
		continue
	elif ask == "n":
		break
	else:
		print("Wrong input")


