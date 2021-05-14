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

#5
f1 = open("test.txt", 'w') #write 버전으로 파일열기
f1.write("Life is too short!")  #그 파일에 뭐라고 쓸지 적어줌
f1.close()  #파일 다시 닫아줌

f2 = open("test.txt", 'r') # read 버전으로 파일열기
print(f2.read())    #f2의 내용 전체 읽기
f2.close()  #파일닫기

#6
user_input = input("저장할 내용을 입력하세요:") # 새로운 객체에 질문 input해주기
f = open('test.txt', 'a')   #append버전으로 파일열기  
f.write(user_input) #아까 인풋받은 내용을 파일에 추가하기
f.write("\n")  # 인풋받은 내용을 추가할 때 줄바꾸기            

#7
f = open('test.txt', 'r')   
body = f.read() #새로운 객체에 파일 전체 읽히기
f.close()

body = body.replace('java', 'python') 

f = open('test.txt', 'w')
f.write(body)
f.close()