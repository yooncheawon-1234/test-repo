#1
def is_odd():
    if num%2==1:
        return 'odd'
    else:
        return 'not odd'
    
#2
def ave(s):
    sMean=sum(s)/len(s)
    print('평균:', sMean)
print(ave([1,2,3]))

#3
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)

#4
print('정답은 3번 이유는 +가 아닌 ,로 연결되면 띄어쓰기가 적용됨')