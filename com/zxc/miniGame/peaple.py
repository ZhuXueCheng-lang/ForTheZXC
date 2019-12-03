import com.zxc.miniGame.randomUtil as r
import com.zxc.miniGame.Articles as a
'''
人物模块
'''
P={
    'sunWuKong':{'name':'孙悟空','HP':100,'MP':0,'attackPower':10,'efensiveForce':2,'Skills':['huoYanJiJi','hengSaoQianJun']},
    'zhuBaJie':{'name':'猪八戒','HP':100,'MP':0,'attackPower':10,'efensiveForce':2}
   }
E={
    'baiGuJing':{'name':'白骨精','HP':1000,'MP':20,'attackPower':100,'efensiveForce':20}
   }
class peaple:
    name = ''
    HP = 0
    MAX_HP = 0
    TemporMAX_HP = 0
    MP = 0
    attackPower = 0  # 攻击力
    TemporAryattackPower = {}
    efensiveForce = 0  # 防御力
    TemporEfensiveForce = {}
    critical_strike_rate = 0  # 暴击率
    TemporCritical_strike_rate = {}
    avoidance_rate = 0  # 闪避率
    TemporAvoidance_rate = {}

    def __init__(self, Attribute):
        self.name = Attribute.get('name','无名氏')
        self.HP = Attribute.get('HP',0)
        self.MP = Attribute.get('MP',0)
        self.attackPower=Attribute.get('attackPower',0)
        self.efensiveForce = Attribute.get('efensiveForce', 0)
        self.critical_strike_rate = Attribute.get('critical_strike_rate',0)
        self.avoidance_rate = Attribute.get('avoidance_rate',0)
        pass

    def getAttackPower(self):
        attackPower = self.attackPower
        add = self.TemporAryattackPower.get('+',[])

        for i in add:
            attackPower += i
        add = self.TemporAryattackPower.get('*',[])
        for i in add:
            attackPower *= i
        return attackPower
        pass

    def getEfensiveForce(self):
        efensiveForce = self.efensiveForce
        add = self.TemporEfensiveForce.get('+',[])

        for i in add:
            efensiveForce += i
        add = self.TemporEfensiveForce.get('*',[])
        for i in add:
            efensiveForce *= i
        return efensiveForce
        pass

    def getCritical_strike_rate(self):
        critical_strike_rate = self.critical_strike_rate
        add = self.TemporCritical_strike_rate.get('+',[])

        for i in add:
            critical_strike_rate += i
        add = self.TemporCritical_strike_rate.get('*',[])
        for i in add:
            critical_strike_rate *= i
        return critical_strike_rate
        pass

    def getAvoidance_rate(self):
        avoidance_rate = self.avoidance_rate
        add = self.TemporAvoidance_rate.get('+',[])

        for i in add:
            avoidance_rate += i
        add = self.TemporAvoidance_rate.get('*',[])
        for i in add:
            avoidance_rate *= i
        return avoidance_rate
        pass

    def getMAX_HP(self):
        MAX_HP = self.MAX_HP
        add = self.TemporMAX_HP.get('+',[])

        for i in add:
            MAX_HP += i
        add = self.TemporMAX_HP.get('*',[])
        for i in add:
            MAX_HP *= i
        return MAX_HP
        pass

    def attack(self, Enemy):
        print(f'{self.name}对{Enemy.name}发起了攻击：')
        if r.randomOne(Enemy.getAvoidance_rate()):
            print(f'{self.name}的攻击被闪避了')
        else:
            if r.randomOne(self.getCritical_strike_rate()):
                print(f'{self.name}打出了暴击')
                Effective_injury = self.getAttackPower() * 2 - Enemy.getEfensiveForce()
            else:
                Effective_injury = self.getAttackPower() - Enemy.getEfensiveForce()
            if Effective_injury < 0:
                Effective_injury = 0
            Enemy.HP -= Effective_injury
        pass

    def isDie(self):
        if self.HP <= 0:
            print(f'{self.name}死亡')
            return True
        else:
            return False
        pass

    pass
class Enemy(peaple):
    def __init__(self, Attribute):
        peaple.__init__(self,Attribute)
        # super(Enemy, self).__init__(Attribute)
        pass
    pass
class player(peaple):
    Equipment = {}  # 装备
    Props = []  # 物品
    Skills = []  # 技能

    def __init__(self, Attribute):
        self.Skills = Attribute.get('Skills', [])
        super(player, self).__init__(Attribute)
        pass
    def cleanall(self):
        self.TemporCritical_strike_rate={}
        self.TemporAvoidance_rate={}
        self.TemporEfensiveForce={}
        self.TemporAryattackPower={}
        self.TemporMAX_HP={}
        pass
    def start(self):
        a.Equipments(self.Equipment)
        pass
    pass
def showall():
    player=[]
    i=0
    for one in P:
        i+=1
        player.append(one)
        print(f'{i}:{P[one]["name"]}',end='  ')
    return player
    pass
#展示自身
def showMe(obj):
    print(obj.name)
    pass