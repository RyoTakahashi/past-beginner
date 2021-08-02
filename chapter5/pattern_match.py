# 第二回PAST　D問題 (https://atcoder.jp/contests/past202004-open/tasks/past202004_d)
s = input()
s_lst = list(s)

m_lst = ['.']

for i in range(0,len(s_lst)):
    # T=1のケース
    m_lst.append(s_lst[i])
    
    # T=2のケース
    if i + 2 <= len(s_lst):
        m_lst.append('..')
        t2 = ''.join(s_lst[i:i+2])
        m_lst.append(t2)
        
        for j in range(len(t2)):
            t2_lst = list(t2)
            t2_lst[j] = '.'
            m_lst.append(''.join(t2_lst))
    # T=3のケース
    if i + 3 <= len(s_lst):
        m_lst.append('...')
        t3 = ''.join(s_lst[i:i+3])
        m_lst.append(t3)
        
        for j in range(len(t3)):
            for k in range(len(t3)):
                t3_lst = list(t3)
                t3_lst[j] = '.'
                t3_lst[k] = '.'
                m_lst.append(''.join(t3_lst))

print(len(list(set(m_lst))))
