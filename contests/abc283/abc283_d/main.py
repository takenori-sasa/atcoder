from collections import defaultdict
S = input()
# 中断した () を管理するリスト
X = []
# a ～ z がすでに箱に入っているか管理
Y = defaultdict(int)

# 今見ている () の中身を管理
now = set()
for s in S:
    # 新しい () の登場にあわせて、今見ている () を X に格納
    if s == "(":
        X.append(now)
        now = set()
        continue

    if s == ")":
        # 今見ている () の中身をキーに X を初期化
        for t in now:
            Y[t] = 0

        # 直前の () を取り出す
        now = X.pop()
        continue

    # 被りを検出したら終了
    if Y[s] != 0:
        print("No")
        exit()

    # s を使用済みに変更
    Y[s] = 1
    # 今見ている () に s が存在することを記録
    now.add(s)
    print(now, X, Y)

print("Yes")
