#第12回：It's difficult.
'''入力された自然数の公約数を全部列挙、素数かどうかを判断''' 
n = int(input("Data?"))
# int not iterable. so n---range(1, n+1)
for i in range(1, n+1):#辞書でもない、リストでもないから、range()を使う。リストなら、括弧はいらん
    if n % i == 0:
        print(i)
       
n = int(input("Data?"))
for i in range(1, n + 1):
    if n % i == 0:
        if i != 1 and i != n: #数学の考え方
            print("bushisushu")
            break;#ループの中断

'''ユークリッド互除法'''
a = int(input("a?"))
b = int(input("b?"))
r = a%b
while r:
    a = b
    b = r
    r = a % b
print(b)


'''数当てゲーム'''
import random
r = random.randrange(100)

while True:#True表示一直循环直到满足break的条件
    p = int(input("What's your number?"))#放在外面会形成无限循环
    if r > p:#要有大小，才能有比较。
        print("Smaller!!")
    elif r < p:
        print("Bigger!!")
    else:
        print("This is right!")
        break

'''会議の日程調整'''
＃第13回：例外処理、複雑な反復処理、関数の応用
for i in range(5):
    value = int(input("Zhengshu?"))
    try:
        print(100 / value)
    except:
        print("Over")
        break
else:
    print("This loop is over!")
