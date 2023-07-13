dictA = {}
dictA['武器名'] = 'SMG08/18'
dictA['射程'] = '短'
dictA['子弹数'] = 81
print(type(dictA['子弹数']))
print(dictA.keys())#输出所有的键
print(dictA.values())#输出所有的值
print(dictA.items())#输出所有的键值对
dictA.update({'武器强度':'轮椅'})#更新
print(dictA)
del dictA['武器强度']#删除特定键
#dictA.pop('武器强度')#删除特定键
print(dictA)
#给字典排序(按照key排序)
print(sorted(dictA.items(),key = lambda d:d[0]))
#给字典排序(按照value排序)
#print(sorted(dictA.items(),key = lambda d:d[1]))