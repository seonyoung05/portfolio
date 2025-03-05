import random
number = random.sample(range(10), 3)

for count in range(10):
    while True:
        guess = input("추측한 세자리 숫자를 입력하세요")
        if len(guess) == 3:
            break
    strike, ball, out = 0, 0, 0
    secret = ''
    for i in range(3):
        secret += str(number[i])

    for i in range(3):
        if secret[i] == guess[i]:
            strike += 1
        elif secret[i] in guess:
            ball += 1

    if strike == 3:
        print("성공!!")
        break
    else:
        if strike == 0 and ball == 0:
            out += 1
        print("strike:%d ball:%d out:%d" %(strike, ball, out))