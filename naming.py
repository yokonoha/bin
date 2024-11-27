def namerandompicker():
    from random import choice
    nam1=["よ","れ","は","や","ま","ぎ","ち","の","こ","り","す","さ","い","え","の"]
    nam2=["あ","い","え"]
    A=choice(nam1)
    B=choice(nam2)
    return A+B

x=namerandompicker()
print(x)