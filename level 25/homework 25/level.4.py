#4)მომხმარებელს შემოატანინეთ მისი სახელი, თუ ეს სახელი იქნება სიგრძეში 6 სიმბოლოზე მეტი ან ტოლი, მაშინ დაუბეჭდეთ "Hello", თუ იქნება სიგრძეში 5 სიმბოლო, დაუბეჭდეთ "Ola", სხვა შემთხვევაში დაუბეჭდეთ "Bonju".






name=input("enter your name:")
if len(name)>6:print("hello")
if len(name)==6:print("hello")
if len(name)==5:print("Ola")
if len(name)<5:print("Ola")
