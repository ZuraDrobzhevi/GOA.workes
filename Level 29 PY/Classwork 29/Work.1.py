# 1) შექმენით ფუნცქიცა რომელსაც გადასცემთ რაღაც სახელს შემდეგ გადაუარეთ ამ სახელს for loop'ით და დააბრუნეთ თითოეული ელემენტი upper ქეისში



def upper_name(name):
    for i in range(len(name)):
        print(name[i].upper())

upper_name("zura")