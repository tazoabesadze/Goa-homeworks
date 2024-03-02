# 5)Write a program that simulates a simple login system. Ask the user for a username and password, 
# and if they enter "admin" and "password123", respectively, print "Login successful" using if-else.
# 2) ამ ფოტოს მიხედვიტ გააკეთეთ პროგრამა. (მოხმარებელს შემოატანინეთ პაროლი იქამდე სანამ არ დაემტხვევა 
# რეგისტრირებულ პაროლს, while ციკლის და if else _ის გამოყენებით) (edited)

user = "admin"
password = "password123"
user_input1 = input("please enter your user: ")
user_input2 = input("please enter your password: ")
if user_input1 == user and user_input2 == password:
    print("login finished")
else:
    print("incorect username password")