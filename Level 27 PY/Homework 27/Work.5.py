# 5) დღეს ნასწავლ ყველა მეთოდზე გააკეთეთ 5-5 მაგალითი.

text=("giorgi")
text0=("zura")
text1=("ilia")
text2=("vaja")
text3=("rati")
text4=("")

#1) 5 მაგალითი capitaliz()

def cap(cap_word):
    print (cap_word.capitalize())
cap(text)
cap(text0)
cap(text1)
cap(text2)
cap(text3)
cap(text4)

#2) 5 მაგალითი lower()
def low(low_word):
    print (low_word.lower())
low(text)
low(text0)
low(text1)
low(text2)
low(text3)
low(text4)

#3) 5 მაგალითი upper()
def up(up_word):
    print (up_word.upper())
up(text)
up(text0)
up(text1)
up(text2)
up(text3)
up(text4)

#4) 5 მაგალითი swapcease()
def swap(swap_word):
    print (swap_word.swapcase())
swap(text)
swap(text0)
swap(text1)
swap(text2)
swap(text3)
swap(text4)

#5) მაგალითი find()

name = "Elene"
print(name.index("E"))  # output: 0
print(name.index("l"))  # output: 1
print(name.index("e"))   # output: 2
print(name.index("n"))  # output: 3
print(name.index("e"))  # output: 4