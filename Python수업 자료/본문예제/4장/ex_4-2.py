#!/usr/bin/env python
# coding: utf-8

"""
4.2 함수의 응용
(p.53 ~ p.63)
"""

# In[1]: p.53
import turtle
turtle.forward(100)


# In[2]: p.54
import turtle
turtle.shape('turtle')
turtle.forward(100)


# In[3]:
import turtle
turtle.forward(100)
turtle.right(90)


# In[4]:
import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)


# In[5]: p.55
import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
import math
turtle.right(90+45)  # 원점 방향으로 방향 전환하기
turtle.forward(math.sqrt(100*100*2))  # 빗변의 길이를 계산 후 선긋기


# In[6]: p.56
import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.setpos(0, 0)


# In[7]:
import turtle
turtle.circle(100)


# In[8]: p.57
import turtle
turtle.circle(-100)


# In[9]: p.58
import turtle
turtle.pencolor('red')
turtle.forward(200)
turtle.pencolor('blue')
turtle.circle(100)


# In[10]: p.59
import turtle
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.circle(-100)


# In[11]:
import turtle
turtle.color('red')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.pencolor('blue')
turtle.circle(-100)


# In[12]: p.60
import random
print(random.randint(1, 2))


# In[13]:
import random
print(random.randint(50, 100))


# In[14]: p.62
import turtle
import random
for i in range(10):
    for j in range(5):
        col = random.randint(0, 3)
        if (0 == col):
            turtle.pencolor("yellow")
        elif (1 == col):
            turtle.pencolor("blue")
        elif (2 == col):
            turtle.pencolor("red")
        elif (3 == col):
            turtle.pencolor("green")
        col = random.randint(0, 4)
        if (0 == col):
            turtle.color('red')
        elif (1 == col):
            turtle.color('blue')
        elif (2 == col):
            turtle.color('green')
        elif (3 == col):
            turtle.color('purple')
        elif (4 == col):
            turtle.color('yellow')
        sel = random.randint(0, 4)
        if (0 == sel):
            turtle.forward(random.randint(50, 100))
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

