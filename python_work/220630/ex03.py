height = input("What is your height?")

print(type(height))

fheight = float(height)
print(type(fheight))

try:
    fheight = float(10/0)
    print(type(fheight))
except Exception as e:
    pass
print("ㅇㅣㅂㅜㅂㅜㄴ")