#!/user/bin/env python
# -*- coding: utf-8 -*-

import re
import json
from pprint import pprint

with open("corpus_op_re.json","r",encoding="utf-8") as f:
    corpus_op_re = json.load(f)
regexLIST = list(corpus_op_re.items())
print(regexLIST)

def sinica_purger(i):
    with open('../Corpus/{}_sinica_raw.txt'.format(regexLIST[i][0]),encoding="utf-8") as f:
        raw = ''.join(f.readlines())
        purge = re.findall(r'{}'.format(regexLIST[i][1]), raw)
    with open('../Corpus/{}_sinica_purged.txt'.format(regexLIST[i][0]),'w',encoding="utf-8") as g:
        for j in range(len(purge)):
            g.write(purge[j].replace("\t","").replace("\s","").replace(" ","")+"\n")
            

def main(i):
    resultDICT = {"shei_status":True,
                  "shenMe_status":True
                  }
    try:
        sinica_purger(i)
    except:
        resultDICT["{}_status".format(regexLIST[i][0])] = False


    return resultDICT

if __name__ == "__main__":
    for i in range(len(corpus_op_re)):
        main(i)
