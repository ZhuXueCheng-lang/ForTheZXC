import com.zxc.miniGame.peaple as p
import com.zxc.miniGame.randomUtil as r
import com.zxc.miniGame.Skills as s
import com.zxc.miniGame.Articles as a
'''
主模块
'''
Now='START'
player={}
#敌人顺序
Enemys=['baiGuJing']
#关卡
Checkpoint=0
#当前敌人
Enemy={}
a=p.peaple({'avoidance_rate':2})
print(a.getAvoidance_rate())
'''
循环体
'''
def dowhat():
    if Now=='START':
        doStart()
        pass
    elif Now=='NEXT':
        next()
        pass
    elif Now=='Fight':
        Fight()
        pass
    elif Now == 'showPlayer':
        showPlayer()
        pass
    elif Now == 'showProps':
        showProps()
        pass
    pass
def doStart():
    global Now
    global player
    print('游戏开始：')
    players=p.showall()
    i=int(input('你要选谁？'))-1
    Attribute = p.P[players[i]]
    player=p.player(Attribute)
    p.showMe(player)
    Now='NEXT'
    pass
def next():
    global Now
    global Enemys
    global Enemy
    global Checkpoint
    print('请选择你要做的事：')
    print('1:前进  2：查看状态  3：查看道具')
    i=input('你选择？')
    if i=='1':
        #生成敌人
        Enemy = p.Enemy(p.E[Enemys[Checkpoint]])
        Checkpoint += 1
        Now='Fight'
        pass
    elif i=='2':
        Now = 'showPlayer'
        pass
    elif i=='3':
        Now = 'showProps'
        pass
    pass

def Fight():
    global Enemy
    global player
    global Now
    print('展示双方状态')
    #我方行动
    i=input("1：攻击  2：技能  3：道具")
    if i=='1':
        player.attack(Enemy)
        pass
    elif i=='2':
        useSkills()
        pass
    elif i=='3':
        useProps()
        pass
    else:
        print('你跳过了回合')
        pass
    if Enemy.isDie():#敌人死亡
        Now = 'NEXT'
    player.MP+=1
    #敌方行动
    Enemy.attack(player)
    if player.isDie():#我方死亡
        Now = 'Die'
    pass
def showPlayer():
    global player
    global Now
    print('展示属性')
    Now = 'NEXT'
    pass
def showProps():
    global player
    global Now
    print('展示物品,可使用物品，穿戴装备')
    Now = 'NEXT'
    pass
def useProps():
    global Enemy
    global player
    global Now
    print('战斗中使用道具')

    pass
def useSkills():
    global Enemy
    global player
    global Now
    print('战斗中使用技能')
    s.showSkills(player.Skills)
    i=int(input('你要使用？'))-1
    s.doSkills(player.Skills[i],player,Enemy)
    pass

if __name__=='__main__':
    while Now!= 'Die' and Now!='Win':
        dowhat()
    pass
if Now == 'Die':
    print('你死了游戏结束')
    pass
if Now == 'Win':
    print('恭喜你赢了')
    pass