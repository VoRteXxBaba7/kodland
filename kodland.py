# Arkadaşlarınızı şaşırtın
my_words = ["Hi!", "Python Pro", "Kodland"] 
print(my_words[1])

name = input()
print("Hi ", name)

import random
emojis = ["^^", "0_o", ":)", "¯\\_(ツ)_/¯", "(￢_￢)"]
print(random.choice(emojis))

hakkimdaki_gercekler=["tarçın","tavuk pilav","araba projem"]
print(random.choice(hakkimdaki_gercekler))


meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print("istediğiniz kelimenin anlamı:",meme_dict[word])
    else:
        print("aradığınız sözlük bulunmamaktadır")
