# -*-coding:utf8
# http://learnpythonthegardway.org/book/ex40.html

mystuff =  {'apple': "IAM APPLES!"}
print(mystuff['apple'])

import mystuff

mystuff.apple()
print(mystuff.tangerine)


class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


# end class MyStuff

thing = MyStuff()
thing.apple()
print(thing.tangerine)


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_body = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_aprade.sing_me_a_song()

# 입력후 add.commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit  # 오류노트에 각자 오류노트 작성