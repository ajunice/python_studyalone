# 변수 선언
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외 처리
try:
    # 숫자를 입력받는다.
    number_input = int(input("정수 입력> "))
    # 리스트 요소 출력
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    # ValueError 발생
    print("정수를 입력해 주세요!")
except IndexError:
    # IndexError 발생
    print("리스트의 인덱스를 벗어났어요!")
