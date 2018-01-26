# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 23:56:47 2018

@author: Kevin
"""
import re

#方法一
def cnt_word_1(fileName):
    word_dict = dict()
    mark = ' ,.!*\n'
    with open(fileName, "r") as f:
        article = f.read()
        words = re.split(r"[ ,.!*\n-]", article)
        for word in words:
            word = word.lower()
            if word == '': 
                continue
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        for word in word_dict:
            print (word + ":" + str(word_dict[word]))


#方法二
def cnt_word_2(fileName):
    #word_dict = dict()
    return

if __name__ == '__main__':
    fileName = "resource/article.txt"
    cnt_word_1(fileName)        