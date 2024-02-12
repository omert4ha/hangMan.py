import random
list = ["python","print","random","while"]
kelime = random.choice(list)
adam = ['''
  +-----+
  o      |
 /|\     |
 / \     |
         ''','''
 +-----+
  o      |
 /|\     |
 /       |
          ''','''
 +-----+
  o      |
 /|\     |
         |
''','''
  +-----+
  o      |
 /|      |
         |
 ''','''
  +-----+
  o      |
  |      |
         |
''','''
  +-----+
         |
         |
         |
''']

dogruHarf=[]
yanlısHarf=[]
hak=len(adam)

while hak>0:
    out=""
    for h in kelime:
        if h in dogruHarf:
            out+=h
        else:
            out+="_"
    if out==kelime:
        break
    print("kelime: ",out)
    print(adam[hak-1])
    girHarf = input()
    if girHarf in dogruHarf or girHarf in yanlısHarf:
        print(girHarf,"zaten girildi :/")
    elif girHarf in kelime:
        print("doğru harf")
        dogruHarf.append(girHarf)
    else:
        print("Yanlış harf!!!")
        hak-=1
yanlısHarf.append(girHarf)

if hak!=0:
    print("Kazandın, Kelimeniz::",kelime)
else:
    print("kaybettin, Kelime::",kelime,"idi")

