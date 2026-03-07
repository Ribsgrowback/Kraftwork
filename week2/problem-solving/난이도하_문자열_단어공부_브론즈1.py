# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
data = list(input().upper())
words = list(set(data))
counts=[]
placeholder=0
dupetoggle=False
wordsave=""
for i in words:
    wordcount= data.count(i)

    if wordcount>placeholder:
        placeholder=wordcount
        wordsave=i
        dupetoggle=False
    elif wordcount==placeholder:
        dupetoggle= True
if dupetoggle==False :
    print(wordsave)
elif dupetoggle==True:
    print('?')
