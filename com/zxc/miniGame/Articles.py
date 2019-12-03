import com.zxc.miniGame.peaple as p

'''
装备模块
'''
E=[{'name':'龙鳞甲','attribute':{'MAX_HP':100,'*MAX_HP':1.1},'doc':'特性增加最大血量1/10','type':'body','Quality':''},
   {'name':'金箍棒','attribute':{'AryattackPower':10,'*AryattackPower':1.1,'Critical_strike_rate':10},'doc':'特性：攻击提高1/10','type':'arms','Quality':''}]
P=[{'name':'血药','attribute':{'HP':20},'doc':'回复20点血','type':'Props'},{'name':'大血药','attribute':{'HP':50},'doc':'回复50点血','type':'Props'}]
def util(attribute,obj):
    obj.HP.get('+',[]).append(attribute.get('HP',0))
    obj.HP.get('*',[]).append(attribute.get('*HP', 1))
    obj.MP.get('+',[]).append(attribute.get('MP', 0))
    obj.MP.get('*',[]).append(attribute.get('*MP', 1))
    obj.TemporMAX_HP.get('+',[]).append(attribute.get('MAX_HP',0))
    obj.TemporMAX_HP.get('*',[]).append(attribute.get('*MAX_HP', 1))
    obj.TemporAryattackPower.get('+',[]).append(attribute.get('AryattackPower', 0))
    obj.TemporAryattackPower.get('*',[]).append(attribute.get('*AryattackPower', 1))
    obj.TemporEfensiveForce.get('+',[]).append(attribute.get('EfensiveForce', 0))
    obj.TemporEfensiveForce.get('*',[]).append(attribute.get('*EfensiveForce', 1))
    obj.TemporAvoidance_rate.get('+',[]).append(attribute.get((attribute.get('Avoidance_rate', 0)+100)/100))
    obj.TemporAvoidance_rate.get('*',[]).append(attribute.get('*Avoidance_rate', 1))
    obj.TemporCritical_strike_rate.get('+',[]).append(attribute.get((attribute.get('Critical_strike_rate', 0)+100)/100))
    obj.TemporCritical_strike_rate.get('*',[]).append(attribute.get('*Critical_strike_rate', 1))
    pass
def useProps(Props,Index,obj):
    props=Props.pop(Index)
    util(props['attribute'],obj)
    pass
def wearEquipment(Equipment,obj):
    print(f'{obj.name}穿戴了 *{Equipment["name"]}* ({Equipment["Quality"]})')
    obj.Equipment[Equipment['type']]=Equipment
    pass
def Equipments(objEquipments,obj):
    Equipments=objEquipments.values()
    for Equipment in Equipments:
        util(Equipment['attribute'],obj)
    pass
