import mysql.connector
import re
import random
import msvcrt




conn=mysql.connector.connect(host='localhost', password='root',user='root', database="Python")

if conn.is_connected():
    print("Successfully Connected...")

mycursor = conn.cursor()

temp=True 

username = ""
logged_in = False


# To input password as *
def masked_input(prompt):
    print(prompt, end='', flush=True)
    password = ''
    while True:
        char = msvcrt.getch()
        char = char.decode('utf-8')
        if char == '\r' or char == '\n':
            print('')
            return password
        elif char == '\b':
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)

def validation(password):
    if len(password) <8 or len(password) >20:
        print("jg",len(password))
        print("Password must be at least 8 characters long.")
        return False

    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False

    if not re.search(r"[^a-zA-Z0-9]", password):
        print("Password must contain at least one special symbol.")
        return False

    print("Password is valid.")
    return True


def register():
    nm=input("Enter the Name:")
    enrol=input("Enter the Enrollment Number:")
    col=input("Enter the College Name:")
    while True:
        psw=input("Enter the Password:")
        if validation(psw):
            con=input("Enter the Contact:")
            sql = "INSERT INTO register (name,enrollment,college,password,contact) VALUES (%s,%s,%s,%s, %s)"
            mycursor.execute(sql, (nm, enrol, col, psw, con))
            conn.commit()
            print("Registration successful.")
            break  
        else:
            print("Registration failed. Please try again.")
            try_again = input("Do you want to try again? (y/n): ")
            if try_again.lower() != 'y':
                break  


def login():
    user = input("Enter the username: ")
    sql=mycursor.execute('select * from register where enrollment = %s',(user,))
    mycursor.execute(sql, (user))
    data = mycursor.fetchone()  
    if data is not None:
        try:
            pass
        except:
            pass
        pwd = masked_input("Enter password: ")
        if data[4] == pwd:
            print(f"Welcome {data[1]}")
            username = user
            logged_in = True
        else:
            print("Wrong password!!!")
            login()
    else:
        print("Wrong Username or you didn't registered with us!!!")
        ch = input("do you want to register!!! y/n")
        if ch=='y' or ch == 'Y':
            register()
        else:
            login()

    print("""
        Choose 1 for Attempt quiz
        Choose 2 for View result
        Choose 3 for Show profile
        Choose 4 for Update Profile
    """)
    ch = input("Enter your choice: ")
    if ch == '1':
        attemptQuiz(username, data)
    elif ch == '2':
        result(data)
    elif ch == '3':
        showProfile(data,logged_in)
    elif ch == '4':
        updateProfile(data,logged_in)


def updateProfile(log,user):
    pass

def showProfile(user,log):
    print(log)
    if log:
        print(f"HELLO {user[1]} Your college is {user[3]} Your contact number is {user[-1]}")
    ch = input("Do you want to update your profile: y/n")
    if ch == 'y' or ch == 'Y':
        updateProfile()
    
def attemptQuiz(uname,data):
    ch = input("Choose an option\n 1. Python\n 2. Java\n 3. Math\n 4. Back to Login")
    if ch == '1':
        sql = "select * from question where category = 'Python'"
        mycursor.execute(sql)
        ques = mycursor.fetchall() #fetchone()
        # print(ques) #[(),(),(),()]
        qu = [] #100
        for i in ques:
            qu.append(i) #[, , , , ,]
        qs = random.sample(qu,5) #14, 25, 89, 99
        n = 1
        correct = 0
        for i in qs:
            print(f"HEllo {uname} you are attempting quiz of {i[-1]}")
            print(f"Q.{n}. {i[1]}\n A. {i[4]}\n B. {i[5]}\n C. {i[6]}\n D. {i[7]}\n")
            ans = input("Your Answer A/B/C/D: ").lower()
            if ans == i[2]:
                correct += 1

            n = n+1
        print(f"Your Result is {correct}")
        sql = "INSERT INTO result (enrollment,marks,name,category) VALUES (%s,%s,%s,'Python')"
        mycursor.execute(sql,(data[2],correct,data[1]))
        conn.commit()
        attemptQuiz(uname,data)
    elif ch == '2':
        sql = "select * from question where category = 'Java'"
        mycursor.execute(sql)
        ques = mycursor.fetchall() #fetchone()
        # print(ques) #[(),(),(),()]
        qu = [] #100
        for i in ques:
            qu.append(i) #[, , , , ,]
        qs = random.sample(qu,4) #14, 25, 89, 99
        n = 1
        correct = 0
        for i in qs:
            print(f"Q.{n}. {i[1]}\n A. {i[4]}\n B. {i[5]}\n C. {i[6]}\n D. {i[7]}\n")
            ans = input("Your Answer A/B/C/D: ").lower()
            if ans == i[2]:
                correct += 1

            n = n+1
        print(f"Your Result is {correct}")
    elif ch == '3':
        sql = "select * from question where category = 'Java'"
        mycursor.execute(sql)
        ques = mycursor.fetchall() #fetchone()
        # print(ques) #[(),(),(),()]
        qu = [] #100
        for i in ques:
            qu.append(i) #[, , , , ,]
        qs = random.sample(qu,4) #14, 25, 89, 99
        n = 1
        correct = 0
        for i in qs:
            print(f"Q.{n}. {i[1]}\n A. {i[4]}\n B. {i[5]}\n C. {i[6]}\n D. {i[7]}\n")
            ans = input("Your Answer A/B/C/D: ").lower()
            if ans == i[2]:
                correct += 1

            n = n+1
        print(f"Your Result is {correct}")
    elif ch=='4':
        login()
        

def result(data):
    
    sql="""select * from result where enrollment= %s"""
    mycursor.execute(sql, (data[2],))
    ques = mycursor.fetchone() 
    print(f"Marks of {data[1]} in {ques[4]} : ")
    print(ques[3])

while(temp):
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    ch= input("Enter any choise")
    if ch == "1":
        register()
    elif ch == "2":
        login()
    elif ch == "3":
        exit()
    else:
        print("Invalid choise")
        temp = False


