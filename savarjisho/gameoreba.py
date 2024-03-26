for i in range(1, 100):
    if i % 2 == 0:
        print(str(i) + " luwia")
    else:
        print(str(i) + " kentia")


#   gavaketot kalkulatori -->

def edition(x, y):
    return x + y

print(edition(6, 3))

def edition(x, y):
    return x - y

print(edition(6, 3))

def edition(x, y):
    return x * y

print(edition(6, 3))

def edition(x, y):
    return x / y

print(edition(6, 3))



#   გავაკეთოთ პროგრამა. მომხმარებელს სჰემოატანინეტ პაროლი იქამდე, სანამ არ დაემთხვევა რეგისტრირებულ პაროლს, while და if else გამოყენებით


password = "tazo123"

while True:
    input_password = input("enter your password: ")

    if password == input_password:
        print("successfuly logged in")
        break
    else:
        print("incorrect password ")
        try_again = input("try_agein? (yes or no): ")
        if try_again == "no":
          break
        print("invalid input")



#    araperi  -->

password = "tazo123"

while True:
    passwordinput = input("enter password: ")

    if passwordinput == password:
        print("the password is correct")
        break

    else:
        print("the password is incorrect, try again")




#   დაწერე პროგრამა რომელიც გამოიტანს რიცხვებს 1იდან 10ამდე while ციკლის გამოყენებით


num = 0
while num <= 10:
    print(num)
    num += 1

#  while ციკლის მეშვეობით შეამოწმე რიცხვები 1 დან 20 ჩათვლით. რიცხვი თუ იყოფა 3 და 5 ზე მაშინ დაპრინტე ეგ რიცხვი 

i = 1
while i <= 20:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1


#    --->