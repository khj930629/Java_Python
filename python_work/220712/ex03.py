try:
    age = int(input('나이입력'))
    a = age / 0
except Exception as e:
    print('모든 에러가 발생했습니다.',e)
# except ValueError:
#     print("한글로 입력하면 안됩니다.")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
finally:
    print("종료합니다.")

    