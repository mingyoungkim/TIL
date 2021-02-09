# 입력받기 test
# input() 을 이용해서
# 표준 (기본설정 : 콘솔) 입력에서 문자열로 입력받아야 함
# input 받게 되면 기본으로 문자열로 받게 됨

# map() : 인자로 주어진 collection의 요소에 각각 함수 적용
# split() : 문자열에서 띄어쓰기로 구분된 요소들을 나눔


a = list(map(int, input().split()))
# 표준 입력에서 띄어쓰기로 구분된 문자열을 받아서
# 각 구분된 문자에 int() 함수를 적용하고
# 각 요소를 list() 로 만듦

print(a)

# 다른 파일에 있는 아이를 찾아서 데꼬오기 위해서는
# sys라는 패키지에 있는 뭔가를 쓰겠다.
import sys
# 1. sys 패키지 임포트
sys.stdin = open("input.txt") # 가져오고 싶은 정보가 있는 파일이름
a = input() # input.txt에서 문자열 한 줄 읽어옴
print(a)
