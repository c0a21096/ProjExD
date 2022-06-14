import random

TARGET_NUM = 10
MISSING_NUM = 2
TRIALS = 5

def main():
    target, display, missing = generate_list()
    print(f"{target}\n{missing}\n{display}")
    print(display)
    is_qn_collect = quiestioning_num()
    if is_qn_collect:
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
        is_qc_collect = quiestioning_chr(missing)
        if is_qc_collect:
            print("ゲームクリアです。")
        else:
            ("不正解です、またチャレンジしてください")
    else:
        print("不正解です。")

def generate_list():
    alphabet = [chr(c+65) for c in range(26)]
    target_chars = random.sample(alphabet, TARGET_NUM)
    missing_chars = random.sample(target_chars, MISSING_NUM)
    display_chars = [n for n in target_chars if n not in missing_chars]
    #print(f"{target_chars}\n{missing_chars}\n{display_chars}")
    return target_chars, display_chars, missing_chars

def quiestioning_num():
    ans_num = int(input("欠損文字はいくつあるでしょうか？:"))
    if ans_num == MISSING_NUM:
        return True
    else:
        return False

def quiestioning_chr(missing):
    for i in range(TRIALS):
        if len(missing) <= 0:
            return True
        ans_chr = input(f"{i+1}つ目の文字を入力してください:")
        if ans_chr in missing:
            missing.remove(ans_chr)
        else:
            break
    return False

if __name__ == "__main__":
    main()