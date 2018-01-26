#encoding='utf-8'

"""
生成200个序列号码，并将起保存到redis非关系型数据库中 
"""

import random, redis
str = "qwertyuiopasdfghjklzxcvbnm!@#$%^&*1234567890_+"

def create_seq(seqNum, seqLen, r):
    
    for i in xrange(seqNum):
        seq = ''
        for j in xrange(seqLen):
            seq += (random.choice(str))
        r.set(name=i, value=seq)
    
if __name__ == '__main__':
    r = redis.Redis(host='127.0.0.1', port=80, db=0)
    create_seq(200, 10, r)
    