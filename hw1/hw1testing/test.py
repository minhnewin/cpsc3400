def is_diff_one(str1, str2):
    if len(str1) != len(str2):
        return False

    count = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count = count + 1

            if count == 1:
                return True

            return False


potential_ans = []


def transform(english_words, start, end, count):
    global potential_ans
    if count == 0:
        count = count + 1
        potential_ans = [start]
        
        if start == end:
            print (potential_ans)
            return potential_ans
        
        for w in english_words:
            if is_diff_one(w, start) and w not in potential_ans:
                potential_ans.append(w)
                transform(english_words, w, end, count)
                potential_ans[:-1]
                
                return None

l = []
f1 = open('words.txt','r')
data = f1.readlines()
for line in data:
    word = line.split()
    for w in word:
        if len(w)<=7:
            l.append(w)
            f1.close()

lis = [1, 2, 3, 4, 5]
for i in range(len(lis)):
    print(l[i])
    i += 1
            
english_words = set(l)
f2 = open('pairs.txt','r')
a = f2.readlines()
for b in a:
    test = b.split()
    if(len(test[0])==len(test[1])):
        if transform(english_words,test[0],test[1],0)!='':
            print(transform(english_words,test[0],test[1],0))
        else:
            print('no ladder possible')
    else:
        print('given test words are not of equal lengths')
        f2.close()
                    
