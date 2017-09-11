def simpli(number):
    G_simed.append(G_format[number][0])
    for i in G_format[number][1:]:
        if not i in G_simed and (i.islower() or G[number][0] in i):
            G_simed.append(i)

def remove_direc():
    G_output.append(G_simed[0])
    G_none.append(G_simed[0] + "'")
    for i in G_simed[1:]:
        if i.islower():
            G_none.append(i + G_simed[0] + "'")
        else:
            G_output.append(i[1:]+i[0]+"'")
    G_output.append("ε")

def remove_indir(i,j):
    # 循环每个Pi的元素
    for now in range(1,len(G_format[i])):
        # 若此元素是从Pi→Pj
        if G_format[j][0] in G_format[i][now]:
            # 记录γ
            gama = G_format[i][now][1:]
            # 向Pi中添加δ1γ
            for jNum in range(len(G_format[j])):
                G_format[i].append(G_format[j][jNum] + gama)
            # 删除原有的Pjγ
            del G_format[i][now]
    # 删除原有的Pjγ的后，后添加的规则就会被循环遍历到。会假如重复结果。
    # 只需在简化时删除即可
def format(number):
    lastAlp = 0
    now = 0
    while now < len(G[number]):
        if not G[number][now].isalpha():
            G_format[number].append(G[number][lastAlp:now])
            lastAlp = now + 1
        now+=1
    G_format[number].append(G[number][lastAlp:now])


# n = input('请输入文法的数量n：')
n = 3
n = int(n)
# print('文法格式为：S:Qc|c')
# G = []
G = ['R:Sa|a','Q:Rb|b','S:Qc|c']
G_format = []
G_simed = []
G_output = []
G_none = []
for i in range(n):
    #G.append(input())
    G_format.append([])
    format(i)

# 显示整理后的结果
# print(G_format)
for i in range(n):
    for j in range(i):
        remove_indir(i,j)
simpli(i)
remove_direc()
print(G_none)
print(G_output)
        # 把形如Pi→Pjγ的规则改写成
        # Pi→δ1γ|δ2γ|……|δkγ。其中Pj→δ1|δ2|……|δk是关于Pj的所有规则
    # 消除关于Pi规则的直接左递归性