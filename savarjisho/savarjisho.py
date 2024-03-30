# for i in range(1, 100):
#     if i % 2 == 0:
#         print(str(i) + " luwia")
#     else:
#         print(str(i) + " kentia")


#   gavaketot kalkulatori -->

# def edition(x, y):
#     return x + y

# print(edition(6, 3))

# def edition(x, y):
#     return x - y

# print(edition(6, 3))

# def edition(x, y):
#     return x * y

# print(edition(6, 3))

# def edition(x, y):
#     return x / y

# print(edition(6, 3))



#   გავაკეთოთ პროგრამა. მომხმარებელს სჰემოატანინეტ პაროლი იქამდე, სანამ არ დაემთხვევა რეგისტრირებულ პაროლს, while და if else გამოყენებით


# password = "tazo123"

# while True:
#     input_password = input("enter your password: ")

#     if password == input_password:
#         print("successfuly logged in")
#         break
#     else:
#         print("incorrect password ")
#         try_again = input("try_agein? (yes or no): ")
#         if try_again == "no":
#           break
#         print("invalid input")



#    araperi  -->

# password = "tazo123"

# while True:
#     passwordinput = input("enter password: ")

#     if passwordinput == password:
#         print("the password is correct")
#         break

#     else:
#         print("the password is incorrect, try again")




#   დაწერე პროგრამა რომელიც გამოიტანს რიცხვებს 1იდან 10ამდე while ციკლის გამოყენებით


# num = 0
# while num <= 10:
#     print(num)
#     num += 1

#  while ციკლის მეშვეობით შეამოწმე რიცხვები 1 დან 20 ჩათვლით. რიცხვი თუ იყოფა 3 და 5 ზე მაშინ დაპრინტე ეგ რიცხვი 

# i = 1
# while i <= 20:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1


#    --->


# შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან სიტყვას. შემდეგ თქვენ უნდა მოახდინოთ ამ სიტყვის შებრუნება, 
# მაგ: word - drow. საბოლოდ კი დააბრუნეთ შედეგი.

# def word(name):
#     return name[::-1]

# print(word("tazo"))



# def numbesr(number):
#     return number ** 3

# print(numbesr(5))



# def numbesr(number):
#     return number * 2

# print(numbesr(5))



# def num(number):
#     if number % 2 == 0:
#         print("tazo")
#     else:
#         print(number)

# print(num(6))

# --------->>>>-------->>>>>>>>>

# დაპრინტეთ გოას ფასები:
# კვირაში 1-ხელ 190 ლარი
# კვირაში 2-ჯერ 290 ლარი
# კვირაში 3-ჯერ 390 ლარი
# და გამოთვალეთ მაგაზე 20% ფასდაკლება. და ლამაზად დაპრინტეთ


# tax1 = 190
# discount = 30
# tax1_discount1 = tax1 - tax1 * discount / 100

# tax2 = 290
# discount = 30
# tax2_discount2 = tax2 - tax2 * discount / 100

# tax3 = 390
# discount = 30
# tax3_discount3 = tax3 - tax3 * discount / 100

# print(tax1)
# print(tax2)
# print(tax3)

# print(tax1_discount1)
# print(tax2_discount2)
# print(tax3_discount3)


# შექმენით ფუნქცია, რომელიც მომხმარებელს შეეკითხება რიცხვს,
#ხოლო დაუპრინტავს ამ რიცხვზე 3-ჯერ დიდ რიცხვს.

# num = int(input("enter a number: "))
# num = num * 3

# print(num)



# def say_hi(user_name):
#     print("gamarjoba " + user_name)

# say_hi(input("enter your name: "))




# num1 = int(input("plearse enter start value: "))
# num2 = int(input("plearse enter end value: "))

# result = 0

# for num in range(num1, num2 + 1):
#     result =  result + num
#     print(num)

# print(result)


# ---->>>>>---------->>>>>>

# print("1. SignUp")
# print("2. LogIn")
# print("3. Exit")

# user_choice = int(input("please enter your choice: "))

# if user_choice == 1:
#     print("SignUp")
# elif user_choice == 2:
#     print("LogIn")
# elif user_choice == 3:
#     print("Exit")
# else:
#     print("invalid choice")

# -------->>>>>>>>>>>------------>>>>>>


# შექმრნით სარეგიატრაციო ფორმა. რეგისტრაცია და ლოგინი!   -->
# მოვთხოვოთ: სახელი, გვარი, მეილი და პაროლი.

# while True:

#     print("1. sign up")
#     print("2. login up")
#     print("3. exit")

#     person_choice = int(input("please enter your choise:  "))

#     if person_choice == 1:
#         print("sing up page")
#         enter_name = input("enter your name:  ")
#         enter_surname = input("enter your surname:  ")
#         enter_gmail =  input("enter your gmail:  ")
#         enter_password = input("enter your password:  ")
#         enter_password2 = input("enter your password egain:  ")

#         if enter_password == enter_password2:
#             print("You are logged in to the account")
#         else:
#             print("You could not log in to your account")

#     if person_choice == 2:
#         print("login up")

#         input_name = input("enter your name:  ")
#         input_gmail = input("enter your gmil:  ")
#         input_password = input("enter your password:  ")

#         if input_name == enter_name and input_password == enter_password and input_gmail == enter_gmail:
#             print("You have registered")
#         else:
#             print("You failed to register")

#     if person_choice == 3:
#         print("EXIT. Thank you for using our service")
#     else:
#         print("Invalid digit")
#     break
