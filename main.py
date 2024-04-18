yabancisozcukler = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "Rofl" :"Bir şakaya karşılık cevap",
            "Sheesh" :"Onaylamamak",
            "Aggro" :"agresifleşmek"
}
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in yabancisozcukler.keys():
    print (word,"kelimesinin anlamı=",yabancisozcukler[word])
else:
    print ("Bu kelime sözlüğümde yoktur!")
