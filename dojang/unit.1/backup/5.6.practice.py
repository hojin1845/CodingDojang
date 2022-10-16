# 5.6.퀴즈 4
#from random import *
#lst = [1,2,3,4,5]
#print(lst)
#shuffle(lst)
#print(lst)
#print(sample(lst, 1))

from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
#print(type(users))
users = list(users)
#print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명중에면서 1한명은 치킨 3명은 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")











