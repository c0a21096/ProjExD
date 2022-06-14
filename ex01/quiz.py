import random

quiz = {
    "サザエと旦那の名前は？":("マスオ","ますお"), 
    "カツオの妹の名前は？":("ワカメ","わかめ"), 
    "タラオはカツオから見てどんな関係？":("甥","おい","甥っ子","おいっこ")
}

def generate():
    q, ans = random.choice(list(quiz.items()))
    return q ,ans

def main():
    q, ans = generate()
    print(f"問題:\n{q}")
    userans = input("答えるんだ:")
    if userans in ans:
        print("正解")
    else:
        print("出直してこい")

if __name__ == "__main__":
    main()

