# 1) შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით რიცხვების სია. თქვენ უნდა დააბრუნოთ გაფილტრული სია,
#    სადაც უკვემარტო 4-ის ჯერადები იქნება.

def numbers():
    for i in range(21):
        if i %4 == 0:
            print(i)

print(numbers())


# 2) შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლისგან მიღებულ სახელსა და გვარს. შემდეგ ისინი დაამატეთ სიაში და დააბრუნეთ სია.

# def names(name, surname):
#     full_name = [name, surname]
#     return full_name
    
# print(names("tazo", "abesadze"))


# 3) მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები. ეს რიცხვები გადაეცით ფუნქციას, for ციკლით სიაში შეინახეთ მათ შორის არსებული რიცხვები.
#  შემდეგ მოახდინეთ გაფილტვრა, ისევ for ციკლით განიხილეთ თითოეული რიცხვი - თუ რიცხვი ლუწი იქნება, ახალ სიაში დაამატეთ მისი მეორე ხარისხი, 
# ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი კვადრატული ფესვი (0.5 ხარისხი).

# num1 = int(input("enter start number: "))
# num2 = int(input("enter end number: "))

# def numbers():
#     for i in range(num1, num2):
#         if i %2 == 0:
#             print(i ** 2)
#         else:
#             print(i ** 0.5)

# print(numbers())


# # 4) შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს. გვარის თითოეული ასო გადაიტანეთ ახალ სიაში. შემდეგ for ციკლის გამოყენებით 
# # იმუშავეთ ამ სიაზე - მარტო ლუწ ინდექსებზე მყოფი ასოები დაამატეთ ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია.
# # Bonus (არაა სავალდებულო): ეს სია გარდაქმენით სთრინგად და ამ სახით დააბრუნეთ. 

# def surname(name):
#     name_list = []
#     for i in range(1,len(name),2):
#         name_list.append(name[i])
#     print(name_list)

# print(surname("abesadze"))


# # 5) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. თქვენ უნდა დააბრუნოთ ამ სიის საშუალო არითმეტიკული ( ჯამი / სიგრძე )

# list = [6, 3, 1, 13, 14]

# def avg():
#     return sum(list)

# print(avg())

# # 6) შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან სიტყვას. შემდეგ თქვენ უნდა მოახდინოთ ამ სიტყვის შებრუნება, 
# # მაგ: word - drow. საბოლოდ კი დააბრუნეთ შედეგი.

# def word(str):
#     return str[::-1]

# print(word("tazo"))


# # 7) შექმენით ფუნქცია, რომელიც მიიღებს რიცხვების სიას და თქვენ დააბრუნებთ მის გაფილტრულ ვერსიას, 
# # რომელსაც არ ექნება დუპლიკატები (ერთი და იგივე ელემენტები).

# def func():
#     for i in range(1, 2):
#         if i % 4 == 0:
#             print(i)

# print(func())