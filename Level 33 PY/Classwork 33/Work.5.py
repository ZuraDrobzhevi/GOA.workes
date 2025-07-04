# 5)შექმენით ფუნქცია, რომელსაც გადაეცემა წინადადება (მაგ: "hello how are you") და შედეგად აბრუნებს სიას, სადაც იქნება მოცემული თითოეული სიტყვა და გვერძე ეწერება მისი სიგრძე (["hello 5", "how 3", "are 3", "you 3"]

def word_len(sentance):
    result = []
    words = ""

    for i in sentance:
        if i != " ":
            words += i
        else:
            result.append(words + str(len(words)))
            words = ""

    result.append(words + str(len(words)))
    print(result)

word_len("Hello how are you")