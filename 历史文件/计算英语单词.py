f = open(r"C:\Users\92149\Desktop\罗密欧与朱丽叶(英文版)莎士比亚.txt",'r')
word = f.read().lower()
word=word.replace(',','').replace('.','').replace('!','').replace('?','')
word=word.split()
setword=set(word)
det = {}
for i in setword:
    count=word.count(i)
    det1={
        i:count
        }
    det.update(det1)
order = sorted(det.items(),key=lambda x:x[1],reverse = True)
for i in order:
    print(i)