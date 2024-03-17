meme_dict = {
    "CREEPY": "Korkunç",
    "LOL": "Komik bir şeye verilen cevap",
    "SHEESH": "Onaylamamak"
 
}
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
word=word.upper()
if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
else:
    print("kelimeyi bulamadık")
