#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for interrogative_use

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_interrogative_use = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_interrogative_use.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_interrogative_use:
        print("[interrogative_use] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["interrogative"] = []
    if 'intent' not in resultDICT.keys():
        resultDICT["intent"] = []    
    if utterance == "你寫給誰呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("你寫給誰呢")
            resultDICT["intent"].append("a1")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]

    if utterance == "幸運者是誰":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("幸運者是誰")
            resultDICT["intent"].append("a4")

    if utterance == "未來又由誰來決定接班的人呢": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("未來又由誰來決定接班的人呢")
            if 'c3' not in resultDICT["intent"]:
                resultDICT["intent"].append("a3")

    if utterance == "看誰能給得更多":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("看誰能給得更多")
            resultDICT["intent"].append("a8")

    if utterance == "票投給誰只有天知、地知、我知":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("票投給誰只有天知、地知、我知")
            resultDICT["intent"].append("a6")

    if utterance == "誰是高人呢":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("誰是高人呢")
            resultDICT["intent"].append("a2")

    if utterance == "還有誰會來買本國的產品":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("還有誰會來買本國的產品")
            resultDICT["intent"].append("a5")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]

    if utterance == "那這樣你怎麼知道誰在愛你":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("那這樣你怎麼知道誰在愛你")
            resultDICT["intent"].append("a7")
            
    if utterance == "誰跟誰求婚":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("誰跟誰求婚")
            resultDICT["intent"].append("a9")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "要不然誰把你Ｆｉｒｅ": #
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("要不然誰把你Ｆｉｒｅ")
            resultDICT["intent"].append("a10")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "誰狠心":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("誰狠心")
            resultDICT["intent"].append("a11")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "究竟是其中誰的貢獻了":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("究竟是其中誰的貢獻了")
            resultDICT["intent"].append("a12")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "誰不要臉":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("誰不要臉")
            resultDICT["intent"].append("a13")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]
            
    if utterance == "我們誰又不是邁向歸途":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["interrogative"].append("我們誰又不是邁向歸途")
            resultDICT["intent"].append("a14")
            resultDICT["intent"] = [item for item in resultDICT["intent"] if "c" not in item]        

    return resultDICT