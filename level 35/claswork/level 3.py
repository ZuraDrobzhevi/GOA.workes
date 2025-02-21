#3)
weight=(int(input("what is your weight?")))
hight=(int(input("what is your hight?")))
b= weight / (hight ** 2)

if b < 18.5:
    print("wnderweight")
elif b>=18.5 and b<25:
    print("normal")
elif b>=25 and b<30:
    print("Overweight")
elif b>30:
    print("Obesity")
