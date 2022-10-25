#!/usr/bin/env python
# coding: utf-8

"""
2.3 입출력함수
(p.20 ~ p.33)
"""

# In[1]: p.21
print('안녕하세요!')


# In[2]:
print(3)  # 정수형


# In[3]:
print(3.5)  # 실수형


# In[4]:
print(True)  # 부울형


# In[5]:
print(3+5)


# In[6]: p.22
import math
r = 2
print(math.pi * r * r)


# In[7]: 
a = 3
b = 3.5
c = True
print(a)  # 정수형(int)
print(b)  # 실수형(float)
print(c)  # 부울형(bool)


# In[8]:
a = 3
b = 3.5
print(a+b)


# In[9]: p.23
print(3.5)


# In[10]:
two = 0b11  # 2진수는 0b를 사용 [영(0)과 binary를 나타내는 b]
print(two)


# In[11]:
eight = 0o11  # 8진수는 0o를 사용 [영(0)과 octet을 나타내는 o]
print(eight)


# In[12]:
a = 0x11  # 16진수는 0x를 사용 [영(0)과 hex를 나나태는 x]
print(a)


# In[13]:
age = 21
print('나이: ', age)


# In[14]:
name = '홍길동'
print('나는', name, '입니다.')


# In[15]: p.24
a = 3
b = 3.5
print(a, '*', b, '=', a*b)


# In[16]: p.25
print("%d" % 3)  # [C언어] print("%d", 3); 명령문과 동일


# In[17]:
print("%f" % 3.5)


# In[18]:
a = 3
b = 3.5
print("%d" % a)


# In[19]:
print("%f" % b)


# In[20]: p.26
name = input()


# In[21]:
print(name)  # 방금 입력한 문자열이 출력됨


# In[22]:
name = input('이름: ')


# In[23]:
print(name)  # name에 자신이 입력한 이름을 확인 가능


# In[24]:
age = input('나이: ')


# In[25]:
print(age)  # age에 자신이 입력한 나이를 확인 가능


# In[26]:
age = input('나이: ')


# In[27]:
after = input('몇 년 후? ')


# In[28]:
print(age + after)


# In[29]: p.27
age = input('나이: ')


# In[30]:
after = input('몇 년 후? ')


# In[31]:
print(int(age) + int(after))


# In[32]:
print('나이: ' + 21)


# In[33]:
print('나이: ' + str(21))


# In[34]: p.29
age = input('나이: ')


# In[35]:
print(int(age) + 10)


# In[36]:
old = age + 10
print(old)


# In[37]:
type(age)


# In[38]:
age = int(age)
type(age)


# In[39]: p.30
height = input('키: ')


# In[40]:
print(height)


# In[41]:
type(height)


# In[42]:
height = input('키: ')


# In[43]:
print(float(height) + 1.5, 'cm')


# In[44]: p.31
num = 5.5
print(int(num))


# In[45]:
a = '5'  # 문자열형의 값
print(int(a))


# In[46]:
b = '5.5'
print(int(b))


# In[47]: p.32
a = input('참(True)/거짓(False): ')


# In[48]:
a


# In[49]:
type(a)


# In[50]:
a = input('참(True)/거짓(False): ')


# In[51]:
print(bool(a))


# In[52]: p.33
a = input('참(1)/거짓(0): ')


# In[53]:
a = int(a)
print(bool(a))


# In[54]:
input('당신은 성인입니까?\n')

