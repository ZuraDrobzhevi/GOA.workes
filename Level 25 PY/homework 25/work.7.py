"""
BOSS Level: 
🔥 დაწერე ფუნქცია, რომელიც მიიღებს ტექსტს, დააბრუნებს ყველა სიტყვის სიგრძეს და დაამატებს მას "სიგრძე" თითოეულ სიტყვას.

📌 მაგ: word_lengths("hello world python") → ['hello 5', 'world 5', 'python 6']

📝 დეტალები:
ტექსტი უნდა გაიყოს სიტყვებად.

თითოეულ სიტყვას უნდა დაემატოს მისი სიგრძე.


(არ არის აუცილებელი ამ დავალების შესრულება თუ შეძლებთ გააკეთეთ)

"""

def oword_lengths (st):
    splited_st = st.split(" ")
    result += ""

    for i in splited_st:
        result += f"{i} {len(i)}"

    print(result)

oword_lengths("hello world python")





