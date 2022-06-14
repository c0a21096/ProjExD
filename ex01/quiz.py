import random

quiz = {
    "サザエと旦那の名前は？":("マスオ","ますお"), 
    "カツオの妹の名前は？":("ワカメ","わかめ"), 
    "タラオはカツオから見てどんな関係？":("甥","おい","甥っ子","おいっこ")
}

def syutudai():
    q = random.choice(quiz.keys())
    ans = quiz[q]
    return q ,ans

def kaito():
    q, ans = syutudai()
    print(q, ans)
    print(f"問題:\n{q}")
    userans = input("答えるんだ:")
    if userans in ans:
        print("正解")
    else:
        print("出直してこい")

if __name__ == "__main__":
    kaito()

