import random,time,mysql.connector as mysql,smtplib
connection = mysql.connect(host='localhost',user='root',password='7028996272')
cursor = connection.cursor()

class Manager:
    emp_id = 100
    def __init__(self):
        q1 = """create database Employee"""
        cursor.execute(q1)
        connection.commit()
        print("q1")
        q2 = """use Employee"""
        cursor.execute(q2)
        connection.commit()
        print("q2")
        
        q3 = """create table employee(Emp_id int(100),Username varchar(100),Password varchar(100),Job_role varchar(100),Salary int(100),Ph_no bigint(100),Email_id varchar(100),Attendance int(100))"""
        cursor.execute(q3)
        connection.commit()
        print("q3")
        
    def add_emp(self):
        print("\n     ------->>    Add New Employee    <<-------         \n")
        self.emp_id += 1

        """if employee id already exist then takes new id"""
        # if self.emp_id in self.dict1:
        #     self.emp_id += 100
        
        username = input("Enter employee's username:    ")
        password = input("Enter employee's password:    ")
        job_role = input("Enter employee's job role:    ")
        try:
            salary = int(input("Enter employee's salary  :    "))
        except:
            print("\nOops!! Invalid Input ....\nEnter Salary Only in Digits")
            Manager.add_emp(self)

        else:
            mobile_no = int(input("Enter Mobile Number      :    "))
            if len(str(mobile_no)) == 10:
                mail_id = input("Enter employee's mail I'd:    ")
                if "@" and "gmail.com" in mail_id:
                    print("Before q4")
                    q4 = """insert into employee (Emp_id,Username,Password,Job_role,Salary,Ph_no,Email_id,Attendance) values (%s,%s,%s,%s,%s,%s,%s,%s)"""
                    qq = (self.emp_id,username,password,job_role,salary,mobile_no,mail_id,10)

                    cursor.execute(q4,qq,)
                    print("after cursor.execute")
                    connection.commit()  
                    print("After connection.commit")                  
                    print("\n!!_ _ _ _ Employee Added Successfully _ _ _ _!!")
                    
                    
                else:
                    print("\nOops!! Invalid E-mail I'd ....\nE-mail I'd Should Contain '@' and 'gmail.com' \nEnter Again")
                    Manager.add_emp(self)
            else:
                print("\nOops!! Please Enter 10 digit Mobile number\nEnter Again")
                Manager.add_emp(self)

    def promote_emp(self):
        print("\n     ------->>    Promote Employee    <<-------         \n")        
        emp_id = int(input("Enter employee I'd       :   "))
        job_role = input("Enter employee's job role:   ")
        salary = int(input("Enter employee's salary  :   "))
        q5 = """update employee set Job_role = %s where Emp_id = %s"""
        qq = (job_role,emp_id)
        cursor.execute(q5,qq,)
        q6 = """update employee set Salary = %s where Emp_id = %s"""
        qqq = (salary,emp_id)
        cursor.execute(q6,qqq,)
        connection.commit()
        print("Updated")
        
    def display_details(self):
        emp_id = int(input("\nEnter Employee's I'd :  "))
        q = """select * from employee where Emp_id = %s """
        qq = (emp_id,)
        cursor.execute(q,qq)
        qqq = cursor.fetchall()
        for i in qqq:
            print("Username :   ",i[1])
            time.sleep(0.5)
            print("Password :   ",i[2])
            time.sleep(0.5)
            print("Job_role :   ",i[3])
            time.sleep(0.5)
            print("Salary :   ",i[4])
            time.sleep(0.5)
            print("Phone_no :   ",i[5])
            time.sleep(0.5)
            print("Email_id :   ",i[6])
            time.sleep(1.5)

    def remove_emp(self):
        print("\n     ------->>    Remove Employee    <<-------         \n")
        emp_id = int(input("Enter Employee's I'd :  "))
        q = """delete from employee where Emp_id = %s"""
        qq = (emp_id,)
        cursor.execute(q,qq)
        connection.commit()    
        print("Removed ....")    
        
    def manager_login(self):
        try:
            while True:
                print("\n- - - - - - - - - - - - - - - ")
                print("\nHello Admin ( *-* )\nChoose the following option:\n\n1.Add Employee\n2.Promote Employee\n3.Display Employee details\n4.Remove Employee\n5.Exit\n")
                choice2 = int(input("Enter Your Choice : "))
                if choice2 == 1:
                    Manager.add_emp(self)
                elif choice2 == 2:
                    Manager.promote_emp(self)
                elif choice2 == 3:
                    Manager.display_details(self)
                elif choice2 == 4:
                    Manager.remove_emp(self)
                elif choice2 == 5:
                    break
                else:
                    print("OOPS!!   Invalid option...")
        except:
            print("\nOops ---->> Error Occurred")
            Manager.manager_login(self)
            
    
class Employee(Manager):
    # def __init__(self):
    #     super().__init__()
        # self.attendance2 = {101:10}

    def attendance(self):
        print("\n     ------->>    Employee Attendance    <<-------         \n")
        
        emp_id = int(input("Enter Employee's I'd :     "))
        attend = input("Enter present/absent :     ")
        if attend == "present" or attend == "p":
            # update = self.attendance2[emp_id] 
            q1 = """select Attendance from employee where Emp_id = %s"""
            qq = (emp_id,)
            cursor.execute(q1,qq)
            total = cursor.fetchone()
            q2 = """update employee set Attendance = %s where Emp_id = %s"""
            qqq = (total[0]+1,emp_id)
            cursor.execute(q2,qqq)
            connection.commit()
            print(f"Total Present days   :    {total[0]+1}",)
        elif attend == "absent" or attend == "a":
            print("Total Present days   :    ")
        else:
            print("\nOops!!  Invalid Input ....\n")
            Employee.attendance(self)
            

    def monthly_salary(self):
        print("\n     ------->>    Employee's Salary    <<-------         \n")
        # try:
        emp_id = int(input("Enter Employee's I'd :      "))
        q1 = """select Salary from employee where Emp_id = %s"""
        qq = (emp_id,)
        cursor.execute(q1,qq)
        sal = cursor.fetchone()
        per_day = sal[0]//30
        q2 = """select Attendance from employee where Emp_id = %s"""
        qqq = (emp_id,)
        cursor.execute(q2,qqq)
        attd = cursor.fetchone()
        total_salary = attd[0]*per_day
        print(f"\nTotal Working days :    {total_salary}")
        print("\n\t  <<---  Keep Working Champ  --->>")
        print("\n\t<<- - - - - - ( * - * ) - - - - - ->>")
            
            
    
    def update_details(self):
        """"This Method Updates The Details Of an Employee"""
        print("\n     ------->>    Update Employee Details    <<-------         \n")
        try:
            emp_id = int(input("Enter employee's I'd:   "))
            
            mobile_no = int(input("Enter Mobile Number     :     "))
            if len(str(mobile_no)) == 10:
                    rand = random.randrange(1111,9999)
                    print(f"OTP to verify Your Mobile Number\n\t** {rand} **\n")
                    verify = int(input("Enter the Above OTP:    "))
                    if rand == verify:
                        q1 = """update employee set Ph_no = %s where Emp_id = %s"""
                        qq = (mobile_no,emp_id)
                        cursor.execute(q1,qq,)
                        connection.commit()
                        print("Mobile Number Updated ....")
                        mail_id = input("\nEnter employee's mail I'd :     ")
                        if "@" and "gmail.com" in mail_id:
                            rand2 = random.randrange(1111,9999)
                            print(f"OTP to Verify Your E-mail I'd\n\t** {rand2} **\n")
                            verify2 = int(input("Enter the Above OTP:    "))
                            if rand2 == verify2:
                                q2 = """update employee set Email_id = %s where Emp_id = %s"""
                                qqq = (mail_id,emp_id)
                                cursor.execute(q2,qqq,)
                                connection.commit()
                                print("E-mail I'd Updated ....")
                                print("\n_ _ _ _ Employee's Detail's Updated Successfully _ _ _ _")
                                time.sleep(1)
                            else:
                                print("Entered OTP is invalid ....")
                                Employee.update_details(self)
                        else:
                            print("Oops!! ---->> Invalid E-mail I'd ....\nEnter again")
                            Employee.update_details(self)
                    else:
                        print("Entered OTP is Invalid ....")
                        Employee.update_details(self)
            else:
                    print("Oops!! ---->> Enter 10 Digit Number Only ....\nEnter again")
                    Employee.update_details(self)
        except:
            print("\nOops ---->> Error Occurred")
            Employee.update_details(self)
            
            
    def employee_login(self):
        while True:
            try:
                print("\n\nHello Employee ( *-* )\nChoose the following option:\n\n1.Display Details\n2.Update Details\n3.Attendance\n4.Monthly Salary\n5.Exit\n")
                choice = int(input("Enter Your Choice :     "))
                if choice == 1:
                    Manager.display_details(self)
                elif choice == 2:
                    Employee.update_details(self)
                elif choice == 3:
                    Employee.attendance(self)
                elif choice == 4:
                    Employee.monthly_salary(self)
                elif choice == 5:
                    break
                else:
                    print("Invalid Input ....")
            except:
                print("\nOops!!  Enter Valid Input ....")

    def __del__(self):
        print("\n\t<<------ Thanks For Visit ------>>")     
        
        
        
    def home(self):
        while True:
            print("\n\nChoose Login Option\n1.Admin \n2.Employee \n3.Exit")
            choice = int(input("\nEnter your choice:  "))
            if choice == 1:
                username = input("\nEnter admin's username:   ")
                if username == "admin":
                    password = input("Enter admin's password:   ")
                    if password == "admin":
                        print("\n---> Admin Login Successfully <---\n")
                        Manager.manager_login(self)

                    else:
                        print("Invalid Password....")
                else:
                    print("Invalid username....")
            elif choice == 2:
                try:
                    username2 = input("Enter Your Username  :     ")
                    q1 = """select Username from employee"""
                    cursor.execute(q1)
                    a = cursor.fetchone()
                    for i in a:
                        if i == username2:
                            password2 = input("Enter Your Password  :     ")
                            q2 = """select Password from employee"""
                            cursor.execute(q2)
                            aa = cursor.fetchone()
                            for i in aa:
                                if i == password2:
                                    Employee.employee_login(self)
                                    break
                            else:
                                print("Invalid Password ...")
                    else:
                        print("Invalid Password ....")
                            

                                
                except:
                    print("\nOops Invalid Login Input ....")

            elif choice == 3:
                q3 = """drop database Employee"""
                cursor.execute(q3)
                connection.commit()
                
                break
            else:
                print("Invalid choice....")
                q4 = """drop database Employee"""
                cursor.execute(q4)
                connection.commit()
                break       
            
            
emp = Employee()
emp.home()
del emp
