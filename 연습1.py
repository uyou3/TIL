# 연산자 
# "처리"

#1. 산술 연산자 

a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b) 

# 정수 나누기 정수를 하면 한 번 더 생각안하고 float로 나타냄 
a = 4
b = 2
print(a / b) 

# 몫 / 나머지 / 제곱 
print(a // b) # 2 / int 
print(a % b) # 0 / int 
print(a ** b) #16 / int 
# 모두 int의 형태를 가짐. 왜?  

# 복합연산자는
# 산술연자와 할당연사자를 함께 쓰는 것
# +=, -=, *=, /= 
a = a + b 
a += b 
print(a)

# 3. 비교연산자 (값과 값을 비교한다고 보면 됨)
# 비교 연산의 결과는 True 혹은 false -> bool자료형이 됨 
a=5
b=2
print(type(a<b))

a='a'
b='b'
print(a==b) 


# 논리연산자 (and, or not)
# a and b : a와 b 둘다 true여야만 true
print(True and True) # True / bool 
print(True and False) # false 

a = 'a'
b = ''
print(a and b) #false 

a = 20 > 10               #비교연산자 true
b = 'hello'=='Hello'      #비교연산자 false 
print(a and b)  # false
print(a or b)  # true 
print( not a )

a = ''
print(not a) # true 


# 수정함 0723