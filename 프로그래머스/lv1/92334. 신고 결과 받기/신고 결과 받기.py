def solution(id_list, report, k):
    # ============ 간단한 코드 ====================
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    # ============================================
    
#     answer = []
     
#     # 유저가 신고한 ID 정보
#     report_info = {id:[] for id in id_list}
    
#     # 각 유저별 신고당한 횟수
#     report_cnt = {id:0 for id in id_list}
    
#     # 각 유저가 받은 결과 메일 수
#     result = {id:0 for id in id_list}
    
#     for x in report:
#         user, to = x.split()
        
#         if to not in report_info[user]:
#             report_info[user].append(to)
        
#             # 신고당한 횟수 증가
#             report_cnt[to]+= 1
    
#     for key, value in report_info.items():
#         for v in value:
#             # 정지당한 ID인 경우
#             if report_cnt[v]>=k:
#                 result[key]+=1
    
#     answer = list(result.values())
    
    return answer