import random
count_test = 0
right = 0
score = 0
while count_test < 11:
    op = ['+', '-', '*', '/']
    i = random.randint(0, 100)
    j = random.randint(0, 100)
    sy = random.choice(op)
    print('%d %s %d = ' % (i, sy, j))
    question = int(input("Please input your question:"))
    r1 = i + j
    r2 = i - j
    r3 = i * j
    r4 = i / j
    if question == r1:
        print('回答正确')
        count_test += 1
        right += 1
    elif question == r2:
        print('回答正确')
        count_test += 1
        right += 1
    elif question == r3:
        print('回答正确')
        count_test += 1
        right += 1
    elif question == r4:
        print('回答正确')
        count_test += 1
        right += 1
    else:
        print('回答错误')
        count_test += 1

score = right * 10
print('答题结束！共有10道题，回答正确为%d道,得分为%d' % (right, score))