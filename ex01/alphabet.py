import random

TARGET_NUM = 10
MISSING_NUM = 2
TRIALS = 5

def main():
    questioning(initgame())

def initgame():
    alphabet = [chr(c+65) for c in range(26)]
    target_chars = random.sample(alphabet, TARGET_NUM)
    missing_chars = random.sample(target_chars, MISSING_NUM)
    display_chars = [n for n in target_chars if n not in missing_chars]
    #print(f"{target_chars}\n{missing_chars}\n{display_chars}")
    return display_chars, missing_chars

def puzzle(answer):
    ans_l = answer
    for i in range(TRIALS):
        if not ans_l:
            print("clear")
        ans_chr = input(f"{i+1}つ目の文字を入力してください：")
        if ans_chr in ans_l:
            ans_l.remove(ans_chr)
        else:
            print("不正解です。またチャレンジしてください")
            break

def questioning(display, answer):
    display = " ".join(display)
    print(f"表示文字:{display}")

    ans_num = input("欠損文字はいくつあるでしょうか？")
    if ans_num == MISSING_NUM:
        print("正解です。それでは具体的に欠損文字を１つずつ入力してください")
        puzzle(answer)
            
    else:
        print("不正解です。")

main()