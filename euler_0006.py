# -*-coding:utf8
a =0
b=0
#a와 b를 0으로 초기화
for i in range(1,101):
    a +=i*i#i의 제곱
    b += i #i를 b에 더한다
print (a) # 제곱
print(b*b) #합의 제곱중
print((b*b)-a) # (합의 제곱)-(제곱의 합)