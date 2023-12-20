import sys 

sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

N = int(input())

def append_star(x):
    if x == 1:
        return ['*']
    
    stars = append_star(x//3)
    st = []

    for s in stars:
        st.append(s*3)
    for s in stars:
        st.append(s+' '*(x//3)+s)
    for s in stars:
        st.append(s*3)
    return st

print('\n'.join(append_star(N)))