#!/usr/bin/env python
# coding: utf-8

"""
5.1 문자열
(p.65 ~ p.76)
"""

# In[1]: p.65
print("hello")  # 'hello'를 출력!
print('hello')  # 'hello'를 출력!


# In[2]:
print('My friend's house.')


# In[3]:
print("My friend's house.")


# In[4]:
print("그녀가 말했다. "안녕!".")


# In[5]:
print('그녀가 말했다. "안녕!".')


# In[6]: p.66
animal = 'frog'
print(animal[3])


# In[7]:
animal = 'frog'
print(animal[-1])


# In[8]: p.67
animal = '진돗개'
print(animal[0])
print(animal[-2])


# In[9]: p.68
animal = 'frog'
print(animal[1])


# In[10]:
animal = 'frog'
print(animal[1:3])


# In[11]:
animal = 'frog'
print(animal[0:3:2])


# In[12]: p.69
animal = 'frog'
print(animal[:])  # [:]는 전체의 문자열 출력
print(animal[1:])  # [1:]는 인덱스 1에서부터 문자열의 끝까지 출력
print(animal[:2])  # [:2]는 처음부터 2 직전까지의 내용 출력


# In[13]:
animal = 'elephant'
print(animal[::2])
print(animal[::-2])


# In[14]: p.71
dog = '개'
animal = '진돗' + dog
print(animal)


# In[15]:
animal = 'elephant'
print(len(animal))


# In[16]: p.72
animal = 'elephant'
print('총 개수:', animal.count('e'))


# In[17]:
animal = 'elephant'
print('앞쪽 찾기:', animal.find('e'))  # 문자나 문자열이 처음 나오는 인덱스 값을 반환
print('ep 찾기:', animal.find('ep'))
print('뒤쪽 찾기:', animal.rfind('e'))  # 문자나 문자열이 가장 나중에 나오는 인덱스 값을 반환
print('위치:', animal.index('e'))  # find()의 기능과 동일, 찾는 내용이 없으면 에러 발생
print('el 시작:', animal.startswith('el'))  # 해당 문자열로 시작하면 True, 그렇지 않으면 False 출력


# In[18]:
animal = 'elephant'
print('n이 있다.:', 'n' in animal)
print('an이 있다.:', 'an' in animal)
print('an이 없다.:', 'an' not in animal)


# In[19]: p.73
ai = 'python program'
print('선택수정:', ai.replace('p', 'P'))  # 단어 교체
print('소문자:', ai.lower())  # 모든 문자들을 소문자로 변환
print('대문자:', ai.upper())  # 모든 문자들을 대문자로 변환
print('swap대소문자:', ai.swapcase())  # 모든 대/소문자들을 역으로 변환
print('첫문자만 대문자:', ai.capitalize())  # 문자열의 첫 문자만 대문자로 수정


# In[20]:
animal = 'Elephant'
animal = animal.upper()
print(animal)


# In[21]:
animal = ' elephant '
print('왼쪽 벗겨내기:', animal.lstrip())  # 문자열의 왼쪽편 공란(들)을 삭제
print('오른쪽 벗겨내기:', animal.rstrip())  # 문자열의 오른쪽편 공란(들)을 삭제
print('좌우 벗겨내기:', animal.strip())  # 문자열의 좌우의 공란(들)을 삭제


# In[22]: p.74
import random
random.random()  # 0에서 1 사이의 무작위 실수형 값을 출력


# In[23]:
import random
print(random.randrange(1, 6))  # 1에서 5까지의 무작위 수를 출력


# In[24]:

import random
chars = '한글우수'
print(random.choice(chars))


# In[25]: p.75
import random
chars = ['한', '글', '우', '수']
print(random.choice(chars))


# In[26]:
import random
chars = ['한', '글', '우', '수']
random.shuffle(chars)  # 4개의 글자가 무작위 순으로 재배열 됨
print(chars)

