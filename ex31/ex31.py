# -*-coding:utf8
# http://learnpythonthegardway.org/book/

if "raw_input" not in dir(__builtins__):
    raw_input = input

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = raw_input("> ")

if door == "1":
    print("There's a giant bear eating a cheese cadke. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear")

    bear = raw_input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away."% bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    instanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print("You body survives powered by a mind of jello. Good job!")
    else:
        print("You stumble around and fall on a knife and die. Good job!")

# 여기까지 입력 후 add. commit # 각 행 주석 입력 후 commmit

# 각자 Study drills 시도 후 필요시 commit # 오류노트 에 각자 오류노트 작성