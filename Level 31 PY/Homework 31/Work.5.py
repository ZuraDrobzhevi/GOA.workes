
# 5) ცვლადში შეინახეთ სახელი. შემდეგ მომხმარებელსაც შემოატანინეთ თავისი სახელი. თუ თქვენი სახელების პირველი და ბოლო ასო ერთმანეთს დაემთხვევა გამოიტანეთ 2.
# თუ სახელის ან პირველი ან ბოლო ასო დაემთხვევა გამოიტანეთ 1. ყველა სხვა შემთხვევაში: 0.


my_name = "Zura"
user_name = input("what is your name?:")
if my_name[0] == user_name[0] and my_name[-1] == user_name[-1]:
    print(2)
elif my_name[0] == user_name[0] or my_name[-1] == user_name[-1]:
    print(1)
else:
    print(0)




