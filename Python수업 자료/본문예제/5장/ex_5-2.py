#!/usr/bin/env python
# coding: utf-8

"""
5.2 배열의 종류
(p.76 ~ p.111)
"""

# In[1]: p.77
price = [1020, 870, 3160, 2650]
fruits = ['사과', '오렌지', '포도', '복숭아']
print(price)
print(fruits)


# In[2]: p.78
price = [1020, 870, 3160, 2650]
fruits = ['사과', '오렌지', '포도', '복숭아']
print(price[1])
print(fruits[-1])


# In[3]:
fruits = ['사과', '오렌지', '사과', '복숭아']
fruitstag = ['사과', 1020, '오렌지', 870, '복숭아', 2650]


# In[4]:
a = [3, 5, 7]
b = a
b[0] = b[0] - 2
print('a=', a, 'b=', b)


# In[5]: p.79
price = [1020, 870, 3160, 365, 731]
print(price[0:2])  # 인덱스 0에서 2 전까지 출력
print(price[0:4:2])  # 인덱스 0에서 4 전까지 2의 간격으로 출력
print(price[1::2])  # 인덱스 1에서 2의 간격으로 끝까지 출력


# In[6]: p.80
x = 12.23
y = 23.34
packing = [x, y]  # packing!
type(packing)
print('Packing:', packing)
[c1, c2] = packing  # unpacking!
print('Unpacking:\nc1:', c1)
print('c2:', c2)


# In[7]: p.81
fruits1 = ['사과', '오렌지', '포도']
fruits2 = ['복숭아', '키위']
allfruits = fruits1 + fruits2
print(allfruits)


# In[8]:
prime = [2, 3, 5]
prime.append(7)
print(prime)


# In[9]: p.82
a = list()  # list()는 빈 리스트 생성, a = []와 동일
for i in range(5):
    a.append(i)
    print(a[i])


# In[10]:
fruits = ['사과', '귤', '포도']
fruits.append('수박')
print(fruits)


# In[11]: p.83
animals = ['새', '코끼리', '강아지']
for i, animal in enumerate(animals):
    print(i, animal)


# In[12]:
fruits = ['사과', '오렌지', '포도']
fruits.insert(1, '키위')
print(fruits)


# In[13]: p.84
mylist = [3, 5, 4, 9, 1, 8, 2, 1]
newlist = [i for i in mylist if (i%2)==0]
print(newlist)


# In[14]: p.85
nums = [0, 1, 2, 3, 4, 5]
del nums[1]
print(nums)


# In[15]:
nums = [0, 1, 2, 3, 4, 5]
del nums[1:5]
print(nums)


# In[16]: p.86
nums = [1, 3, 5, 7, 9]
nums.pop()  # 9가 삭제되어 [1, 3, 5, 7]로 변경됨
nums.pop()  # 7이 삭제되어 [1, 3, 5]로 변경됨
print(nums)  # 결과를 출력


# In[17]:
nums = [1, 3, 5, 7, 9]
nums.pop(2)
print(nums)


# In[18]:
nums = [0, 1, 2, 3, 4, 5]
nums[1:2] = []
print(nums)


# In[19]:
word = 'orange'
print('r' in word)


# In[20]: p.87
fruits = ['사과', '오렌지', '포도']
print('포도' not in fruits)


# In[21]:
a = [1, 2, 3]
b = a * 2
print(b)


# In[22]:
a = [1, 2, 3]
for i in a:
    print(i * 2)


# In[23]: p.88
fruits = ['사과', '오렌지', '포도']
print(len(fruits))


# In[24]:
nums = [5, 7, 1, 3, 5, 7, 1, 3, 3, 5, 7, 9]
print(nums.count(5))


# In[25]: p.89
nums = [1, 2, 3, 4, 5, 3]
print(nums.index(3))


# In[26]:
nums = [3, 5, 2, 1, 5, 3]
nums.sort()
print(nums)


# In[27]:
nums = [3, 5, 2, 1, 5, 3]
nums.sort(reverse = True)
print(nums)


# In[28]:
fruits = ['apple', 'orange', 'grape', 'orange']
fruitdb = [['apple', 1020], ['orange', 880], ['grape', 3160]]


# In[29]: p.90
fruitdb = [['사과', 1020], ['오렌지', 880], ['포도', 3160]]
print(fruitdb[1])
print(fruitdb[1][0])


# In[30]:
record = [
    [1, 2, 3],
    [10, 20, 30],
    [100, 200, 300]]
index = [ary[1] for ary in record]
print(index)


# In[31]:
mylist = [[1, 2], [3, 4, 5], [6, 7]]
newlist = [x for x in mylist if len(x)==2]
print(newlist)


# In[32]: p.92
def times2(a):
    a = a * 2
    print(a)
nums = [1, 2, 3]
times2(nums)


# In[33]: p.94
empty = ()  # 빈 튜플을 생성 또는 empty = tuple()
animals = ('토끼', '사자', '원숭이')
fruits = '사과', '오렌지', 1020, 880
start = '하나', '둘',
print(fruits)


# In[34]: p.95
print(fruits[1])  # 인덱싱 기능
print(fruits[1:3])  # 슬라이싱 기능


# In[35]:
fruits[1] = '키위'


# In[36]:
animals = ('토끼', '사자', '원숭이')
fruits = '사과', '오렌지', 1020, 88,
things = animals, fruits
print(things)


# In[37]: p.96
fruits = (['포도', '망고'], ['사과', '키위'])
print(fruits[1])


# In[38]:
fruits = (['포도', '망고'], ['사과', '키위'])
newfruits = ['수박', '참외']
fruits[1] = newfruits


# In[39]:
fruits = [('포도', '망고'), ('사과', '키위')]
fruits[0] = ('수박', '참외')
print(fruits)


# In[40]:
fruits = (['포도', '망고'], ['사과', '키위'])
fruits[1][0] = '수박'
print(fruits)


# In[41]: p.97
dice = (3, 2, 5, 3, 4)
dice[2:4]


# In[42]:
x = 12.23
y = 23.34
packing = (x, y) # packing!
type(packing)
print('packing:', packing)
(c1, c2) = packing # unpacking!
print('c1:', c1)
print('c2:', c2)


# In[43]:
dice1 = (3, 2, 5, 3, 4)
dice2 = (6, 1, 4, 2, 3)
dice3 = dice1 + dice2
print(dice3)


# In[44]: p.98
dice = (3, 2, 5, 3, 4)
print(2 in dice)
print(2 not in dice)


# In[45]:
a = (1, 2, 3)
b = a * 2
print(b)


# In[46]:
dice = (1, 2, 3)
print(len(dice))


# In[47]: p.99
dice = (5, 3, 1, 2, 3, 6)
print(dice.count(3))


# In[48]:
dice = (5, 3, 1, 2, 3, 6)
print(dice.index(3))


# In[49]:
dice1 = (6, 1, 4)
dice2 = (5, 2, 1)
result = (dice1, dice2)
print(result)
print(result[1][1])


# In[50]: p.100
name = '홍길동'
age = 21
height = 172.5
print('이름: {} 나이: {} 키: {}'.format(name, age, height))


# In[51]:
print('이름: {0:3s} 나이:{1:3} 키:{2:6.1f}'.format(name, age, height))


# In[52]: p.101
import turtle
import random
for i in range(10):
    for j in range(5):
        col = random.randint(0, 4)
        coltype = ('yellow', 'blue', 'red', 'purple', 'green')
        col = random.randint(0, 4)
        turtle.color(coltype[col])
        sel = random.randint(0, 4)
        if (0 == sel):
            turtle.forward(random.randint(30, 50))
        elif (1 == sel):
            turtle.right(random.randint(90, 360))
        elif (2 == sel):
            turtle.begin_fill()
            turtle.circle(random.randint(-100, -20))
            turtle.end_fill()
        elif (3 == sel):
            turtle.forward(random.randint(30, 50))
        elif (4 == sel):
            turtle.circle(random.randint(20, 100))
    a = float(random.randint(-300, 300))
    b = float(random.randint(-300, 300))
    turtle.goto(a, b)


# In[53]: p.102
student = { }  # 빈 사전을 생성함. 또는 student = dict()
student['지훈'] = 1234
print(student)


# In[54]:
student = { }
student['지훈'] = 1234
student['수민'] = 2345
print(student)


# In[55]: p.103
fruitdb = {'사과':1020, '오렌지':880, '포도':3160}
print(fruitdb)


# In[56]:
fruitdb = {'사과':1020, '오렌지':880, '포도':3160}
print(fruitdb[1])
print(fruitdb[1:2])


# In[57]: p.104
fruitdb = {'사과':1020, '오렌지':880, '포도':3160}
del fruitdb['사과']
print(fruitdb)


# In[58]:
student = {'현준': 1234, '민지': 2345}
print('SeJong' in student)
print(student.get('현준'))
print(student.get('민지'))
print(student.keys())
print(student.values())
print(student.items())


# In[59]: p.105
student = {'현준': 1234, '민지': 2345}
newstd = {'승민': 3456, '유진': 4567}
student.update(newstd)
print(student)


# In[60]:
student = dict([['현준', 1234], ['민지', 2345]])
print(student)
student = dict([('현준', 1234), ('민지', 2345)])
print(student)
student = dict((('현준', 1234), ('민지', 2345)))
print(student)


# In[61]:
student = dict(현준=1234, 민지=2345)
print(student)


# In[62]:
person = {'name':'준혁', 'age':21, 'height':172.5}
print('이름:{0[name]}, 나이:{0[age]}, 키:{0[height]}'.format(person))


# In[63]: p.107
dict = { }  # 빈 사전을 생성 또는 dict = set()
dict = {3, 2, 3, 1}  # 중복된 원소를 포함한 데이터 입력
print(dict)


# In[64]:
fruits = ['사과', '오렌지', '포도', '오렌지']
fruits = set(fruits)
print(fruits)


# In[65]:
fruits = {'사과', '오렌지', '포도'}
fruits.add('키위')
print(fruits)


# In[66]:
fruits = {'사과', '오렌지', '포도'}
fruits.update({'수박', '배'})
print(fruits)


# In[67]: p.108
fruits = {'사과', '오렌지', '포도', '수박'}
fruits.remove('오렌지')
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)


# In[68]:
fruits = {'사과', '오렌지', '포도'}
print('사과' in fruits)
print('키위' not in fruits)


# In[69]: p.109
one = {1, 3, 5, 7, 8}
two = {1, 3, 5, 6, 8}
print('one | two:', one | two)
print('one & two:', one | two)
print('one - two:', one - two)
print('one ^ two:', one ^ two)


# In[70]: p.110
one = {1, 3, 5, 8}
two = {1, 3, 5, 8}
print('one <= two:', one <= two)
print('one < two:', one < two)
print('one >= two:', one >= two)
print('one > two:', one > two)


# In[71]:
training_data = [['연두', 3, '사과'],
                 ['노랑', 3, '사과'],
                 ['빨강', 2, '포도'],
                 ['빨강', 1, '포도'],
                 ['노랑', 3, '레몬']]
def fruit_counts(data):
    counts = {}
    for row in data:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts
result = fruit_counts(training_data)
print(result)

