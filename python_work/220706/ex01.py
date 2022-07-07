from car import Car


def main():
    c1 = Car()
    # print('main')
    while True:
        print('1. 속도입력')
        print('2. 속도출력')
        select = int(input())
        if select == 1:
            speed = input("속도를 입력하세요 ")
            c1.speed = speed
            print(" ")
        else:
            print("현재 속도는", c1.speed, "km/h 입니다.")
            print(" ")
            return


main()
