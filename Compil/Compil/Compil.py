

def remove_direc():
    G.append('dir')


def remove_indir():
    G.append('in')


def format(number):
    G_format[number].append(G[number][0])

    for i in range(1,len(G[number])):
        if G[number][i].isalpha():
            j = i
            while G[number][j].isalpha():
                if j==len(G[number])-1:
                    break
                j+=1
            if i != j:
                G_format[number].append(G[number][i:j])
                i = j +1





n = input('请输入文法的数量n：')
n=int(n)
print('文法格式为：S:Qc|c')
G = []
G_format = []
for i in range(n):
    G.append(input())
    G_format.append([])
    format(i)

# print(G_format)


#for i in range(1,n + 1):
#    for j in range(1,i):
        # 把形如Pi→Pjγ的规则改写成
        # Pi→δ1γ|δ2γ|……|δkγ。其中Pj→δ1|δ2|……|δk是关于Pj的所有规则
    # 消除关于Pi规则的直接左递归性