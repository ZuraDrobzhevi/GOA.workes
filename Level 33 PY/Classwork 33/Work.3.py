#3)შექმენით სია სადაც შეინახავთ 5 სახელს. შემდეგ მომხმარებელს შემოატანინეთ სახელი და ინდექსი თუ ინდექსი აღემატება სიის რაოდენობას დააბრუნეთ ერორი სტრინგის სახით სხვაშემთხვევაში დაამატეთ სიაში.

names = ["Ana", "Levan", "Mariam", "Giorgi", "Nino"]

new_name = input("Enter a new name: ")
index = int(input("Enter index: "))

if index > len(names):
    print("Error: Index exceeds list size")
else:
    names.insert(index, new_name)
    print("Updated list:", names)