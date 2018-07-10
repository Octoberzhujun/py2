#老师随机分配问题    author：wsq
rooms = [[],[],[]]
teachers = ["A","B","C","D","E","F","G","H","I","J","K"]

i = len(teachers)
#print(i)
import random
j1 = random.choice(range(i))
#print(j1)

mj1 = j1
while mj1 >0:
    mj1 -= 1
    my = random.choice(teachers)
    rooms[0].append(my)
    teachers.remove(my)
#print(teachers)

j2 = random.choice(range(i-j1))
#print(j2)
mj2 = j2
while mj2 >0:
    mj2 -= 1
    my2 = random.choice(teachers)
    rooms[1].append(my2)
    teachers.remove(my2)

j3 = i - j1 - j2
while j3 >0:
    j3 -= 1
    my3 = random.choice(teachers)
    rooms[2].append(my3)
    teachers.remove(my3)
print("教室分配情况如下所示：")
print(rooms)

#简写
rooms = [[], [], []]
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for i in teachers:
    a = random.randint(0, 2)
    rooms[a].append(i)
print(rooms)