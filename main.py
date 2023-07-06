name = input("이름 입력: ")
print(name)

#에러 가능성 있을때 필요한 작업
try:
	age = int(input("나이 입력: "))
	print(age + 1)
except:
	print("문제 발생")
    print("프로그램 종료")

#여러 개 입력
hobbies = input("취미를 ,로 구분해서 입력: ").split(",")
for hobbies in hobbies:
	print(hobbies)