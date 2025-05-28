# 3) ცვლადში შეინახეთ თქვენი გვარი. შემდეგ მომხმარებელს შემოატანინეთ გვარი. შეამოწმეთ თქვენი გვარები ემთხვევა თუ არა ერთმანეთს. თუ ემთხვევა ტერმინალში დაუბეჭდეთ - "Our surnames are similar." სხვა შემთხვევაში - "We have different surnames". ეს პროგრამა აუცილებლად Case Insensitive უნდა იყოს.



გვარი=input("what is your last name?")
ჩემი_გვარი="Drobzhevi"

if გვარი.lower()==ჩემი_გვარი.lower():
    print( "Our surnames are similar.")
else:
    print( "We have different surnames.")