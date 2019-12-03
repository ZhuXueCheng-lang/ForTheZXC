import math

import com.zxc.miniGame.Articles as a
import random

'''
随机模块
'''
def randomOne(i):
    a = random.random()
    if a <= i:
        return True
    else:
        return False
    pass


def getNewEquipment():
    Equipment=random.choice(a.E)
    i=0
    s=0
    attributes=Equipment.get('attribute')
    for attribute in attributes:
        if attribute.count('*')==0:
            b = math.ceil(random.uniform(0, 6)) - 1
            s+=1
            i+=b
            attributes[attribute]+=b
    i=i/s
    if i<=2:
        Equipment['Quality']='普通'
    elif 2<i<4:
        Equipment['Quality'] = '稀有'
    elif 4<=i<4.5:
        Equipment['Quality'] = '史诗'
    else:
        Equipment['Quality'] = '传说'

    return Equipment
    pass
def getNewProps():
    return random.choice(a.P)
    pass
if __name__=='__main__':
    print(getNewEquipment())
    pass
