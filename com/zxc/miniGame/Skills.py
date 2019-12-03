import com.zxc.miniGame.peaple as p
'''
技能模块
'''
Skills={
    'huoYanJiJi':{'name':'火眼金睛','MP':5,'doc':'暴击和闪避翻倍消耗5MP'},
    'hengSaoQianJun':{'name':'横扫千军','MP':3,'doc':'造成攻击力*3+敌人最大血量1/20的伤害'},
    'nvWaShenShi':{'name':'女娲神石','MP':3,'doc':'回复最大生命值5分之1的血量'}
        }
def doSkills(SkillsName,obj,other):
    eval(SkillsName)(obj,other)
    pass
def showSkills(Skis):
    global Skills
    i=0
    for ski in Skis:
        i+=1
        skills=Skills[ski]
        print(f'{i}:{skills["name"]}  消耗{skills["MP"]}  {skills["doc"]}')
    pass
def huoYanJiJi(obj,other):
    print(f'{obj.name}使用了火眼金睛')
    if obj.MP>=5 :
        obj.MP-=5
        obj.TemporCritical_strike_rate['*']=2
        obj.TemporAvoidance_rate['*']=2
        print(f'{obj.name}的暴击率翻倍，闪避率翻倍')
    else:
        print(f'MP为{obj.MP}不足,使用失败')
    pass
def hengSaoQianJun(obj,other):
    if obj.MP>=3 :
        print(f'{obj.name}使用了横扫千军')
        obj.MP -= 3
        a = obj.getAttackPower() * 2 + other.HP // 20
        other.HP -= a
        print(f'{other.name}受到了{a}点伤害')
    else:
        print(f'MP为{obj.MP}不足,使用失败')
    pass
def nvWaShenShi(obj,other):
    if obj.MP>=3 :
        print(f'{obj.name}使用了女娲神石')
        obj.MP -= 3
        obj = p.player
        other = p.Enemy
        a=obj.getMAX_HP() // 5
        obj.HP += a
        print(f'{obj.name}回复了{a}点血')
    else:
        print(f'MP为{obj.MP}不足,使用失败')
    pass


