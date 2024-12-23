#2)მომხმარებელს შემოატანინეთ მისი საყვარელი 5 საჭმელი (For Loop-ის მეშვეობით), შემდეგ შემოატანინეთ რიცხვი და ამ რიცხვის ინდექზე მდგომი ელემენტი ჯერ დაუბეჭდეთ, ბოლო ამოაგდეთ და ამოგდების შემდეგ დაბეჭდეთ სია.






favorite_food_1=input("enter your favorite food1:")
favorite_food_2=input("enter your favorite food2:")
favorite_food_3=input("enter your favorite food3:")
favorite_food_4=input("enter your favorite food4:")
favorite_food_5=input("enter your favorite food5:")
foods=[favorite_food_1,   favorite_food_2,    favorite_food_3,   favorite_food_4,   favorite_food_5,    ]

num=int(input("enter your number:"))
print(foods[num])

foods.pop(-1)
print(foods)
