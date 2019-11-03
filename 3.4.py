import calendar

yy = []
for i in range(2010, 2031):
    yy.append(i)
mm = []
for j in range(1, 13):
    mm.append(j)
# print(mm[8:12])
for i in range(1, 21):
    for j in mm[0:5]:
        print(calendar.month(yy[i], mm[j], w=3))
    print("*"*20 + str(yy[i]) + "上学期" + "*"*20)
    for j in mm[7:-1]:
        print(calendar.month(yy[i], mm[j]))
    print("*"*20 + str(yy[i]) + "下学期" + "*"*20)
