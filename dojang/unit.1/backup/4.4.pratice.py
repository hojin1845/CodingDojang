#4.4.문자열포맷
#print("a" + "b")
#print("a", "b")

# 방법 1
#print("나는 %d살입니다." % 20)
#print("나는 %d을 좋아해요." % "파이썬")
#print("Apple 은 %c로 시작해요."%"A")
# %s
# print("나는 %s살 입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))