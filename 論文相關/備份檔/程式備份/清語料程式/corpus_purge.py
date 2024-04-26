'''
with open('../a.txt', mode = 'r', encoding = 'utf-8') as f: #r+ read and write, w+ write and read
    content = f.read()
    print(content) 
# ./ 上一層 ../上上一層 ../../上上上層

with open('b.txt', mode = 'w', encoding = 'utf-8') as g:
    g.write('早安')

with open('corpus.txt', mode = 'r', encoding = 'utf-8') as f: 
    content = f.readline() #逐行閱讀
    print(content) 
with open('corpus.txt', mode = 'r', encoding = 'utf-8') as f: 
    content = f.read() 
    content = content.replace('\n','').replace('\t','') #替代
    content = content.split('moremore') #string split了之後變成list[]
    #"1a2a3a4a" str.split("a") ["1","2","3","4"]  #/t是空格的意思，在python顯示/t
    content = '\n'.join(content) #join是split的reverse #c=['1','2','3'] c=''(或是'a').join(c)-->"123"("1a2a3")
    #第19句是把list變回string
    content = content.replace('more','' ) #replace只能用在string 
    print(content) 

with open('ok corpus.txt', mode = 'w', encoding = 'utf-8') as a:
    a.write(content) 
'''    
# 重複利用的函式:def functionName(可自訂)(參數(可自訂))
def preprocess(who):
    with open('{}.txt'.format(who), mode = 'r', encoding = 'utf-8') as f: 
        content = f.read() 
        content = content.replace('\n','').replace('\t','') #替代
        content = content.split('moremore') #string split了之後變成list[]
        #"1a2a3a4a" str.split("a") ["1","2","3","4"]  #/t是空格的意思，在python顯示/t
        content = '\n'.join(content) #join是split的reverse #c=['1','2','3'] c=''(或是'a').join(c)-->"123"("1a2a3")
        #第19句是把list變回string
        content = content.replace('more','' ) #replace只能用在string 
    with open('{}_purge.txt'.format(who), mode = 'w', encoding = 'utf-8') as a: #{}_purge.txt乾淨的檔案
        a.write(content) 

preprocess('who')