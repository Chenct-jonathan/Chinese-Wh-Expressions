#!/user/bin/env python
# -*- coding: utf-8 -*-

import re
import json

# 讀取 re
with open("corpus_op_re.json","r",encoding="utf-8") as e:
    corpus_op_re = json.load(e)
regexLIST = list(corpus_op_re.items())

# 依 re 處理語料並寫入 _purged.txt 檔
def sinica_purger(i):
    with open('../Corpus/purged/{}_sinica_purged.txt'.format(regexLIST[i][0]), 'w') as g: # 新增空的 .txt 檔，若有相同檔案會將之清空
        pass    
    with open('../Corpus/raw/{}_sinica_raw.txt'.format(regexLIST[i][0]),encoding="utf-8") as f: # 配合 sinica 格式將 raw 語料重新依 'more' 切分
        raw = ''.join(f.readlines())
        rawLIST = raw.split('more\n')        
    with open('../Corpus/purged/{}_sinica_purged.txt'.format(regexLIST[i][0]),'a',encoding="utf-8") as g: # 逐句依 re 取出含有標的詞彙的部分並寫入_purged.txt 檔
        lineCount = 1
        for j in rawLIST:  
            purge = '\n'.join(re.findall(r'{}'.format(regexLIST[i][1]), j))
            g.write(purge.replace("\t","").replace("\s","").replace(" ","")+"\n")            
            print("{}. {} ==> {}".format(lineCount, j, purge)) # 此處將顯示 {句數}. {raw 語料} ==> {取出部分}
            lineCount += 1
        

def main(i):
    resultDICT = {"shei_status":True, # 方便了解執行狀態
                  "shenMe_status":True
                  }
    try:
        sinica_purger(i)
    except Exception as e:
        resultDICT["{}_status".format(regexLIST[i][0])] = False
        print(f"Error occurred when processing '{regexLIST[i][0]}': {type(e).__name__}.")
        
    return resultDICT

if __name__ == "__main__":
    for i in range(len(corpus_op_re)):
        main(i)
