from random import randint

n = randint(1, 100)

c = 0

while c < 7:
    c += 1
    a = int(input("یک عدد وارد کن!"))
    if n == a:
        print("یاختی ! شوخی کردم یردی")
    elif n > a:
        print("بزرگتر بزن")
    elif n < a:
        print("دقت کن کوچیک تره")
        
