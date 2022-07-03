# 가능한 스킬스티 개수
def solution(skill, skill_trees):
    answer = 0
    
    not_skill = [chr(ord('A')+i) for i in range(26)]
    skill = list(skill)
    for sk in skill:
        not_skill.remove(sk)
    
    for skill_tree in skill_trees:
        for s in not_skill:
            skill_tree = skill_tree.replace(s, "")
            
        answer += 1
        for i in range(len(skill_tree)):
            if skill_tree[i] != skill[i]:
                answer -= 1
                break
                
    return answer