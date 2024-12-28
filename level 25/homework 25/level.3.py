#3)შექმენით სია, მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ შეეკითხეთ როგორ უნდა რო შეცვალოს ეს სახელი / თუ გადმოგცემთ "upper" სიაში დაამატეთ მომხმარებლის სახელი გადიდებულად, თუ გადმოგცემთ "lower" სიაში დაამატეთ დაპატარავებულად, თუ გადმოგცათ "capitalize" სიაში დაამატეთ ისე, რომ სახელის პირველი ასო გადიდებული იყოს...

#ჩემი ვარიანტი
# upper="upper"
# lower="lower"
# capitalize="capitalize"

# სია=["Zaza","Nini","mari","ARNOLD","Lux"]
# შენი_სახელი=input("შემოიტანეთ თქვენი სახელი:")
# შეცვლა=input("როგორ გინდათ შეცვალოთ თქვენი სახელი upper-ით lower-ით თუ capitalize :")
# if შეცვლა == upper: print (შენი_სახელი.upper())
# if შეცვლა == lower: print (შენი_სახელი.lower())
# if შეცვლა == capitalize: print (შენი_სახელი.capitalize()) 

# სია.append(შენი_სახელი)
# print(სია)


#მასწავლებლის ვარიანტი
user_name=input("enter your name:")
choice = input("Enter your choice")
names=[]
if choice == "upper":
    names.append(user_name.upper())
elif choice =="lower":
    names.append(user_name.lower())
print(names)
