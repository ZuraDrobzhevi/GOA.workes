# Input() ის საშუალებით რამდენიმე მომხმარებელს შემოატანინეთ სახელი. ცვლადებში შეინახეთ მათ მიერ შემოტანილი სახელების Capitalized ვერსია. შექმენით names სია, რომელიც თავდაპირველად იქნება ცარიელი და თქვენი დავალება იქნება თითოეული სახელის შემოტანაზე დაამატოთ ეს სახელები სიაში, სიის თითოეულ განახლებაზე დაბეჭდეთ სია.

names = []
while True:
    name = input()
    if not name:
        break
    capitalized_name = name.capitalize()
    names.append(capitalized_name)
    print(names)









