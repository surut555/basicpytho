# fullname = input("Enter your name:")
# age = int(input("Enter your age:"))
# print(fullname)
# print(age+5)

user = input("Enter username: ")
pwd = input("Enter password: ")

set_uset = "admin"
set_pass = "1234"

if user == set_uset and pwd == set_pass:
    print("Yan ! login success")
else:
    print("Opp! login faill!!!")
