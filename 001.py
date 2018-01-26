#encoding='utf-8'
"""
生成200个序列号码
"""
import random
str = "qwertyuiopasdfghjklzxcvbnm!@#$%^&*1234567890_+"

def create_seq(seqNum, seqLen):
    
    for i in xrange(seqNum):
        seq = ''
        for j in xrange(seqLen):
            seq += (random.choice(str))
        print seq
    
if __name__ == '__main__':
    create_seq(200, 10)
