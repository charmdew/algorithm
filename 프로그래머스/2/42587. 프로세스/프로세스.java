import java.util.*;

class Solution {
    class Process {
        private int idx;
        private int priority;
        
        Process(int idx, int priority){
            this.idx = idx;
            this.priority = priority;
        }
        
        public int getIdx(){
            return idx;
        }
        public int getPriority(){
            return priority;
        }
    }
    
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        LinkedList<Process> queue = new LinkedList<Process>();
        
        int n = priorities.length;
        System.out.println(n);
        for(int i=0; i<n; i++){
            queue.add(new Process(i, priorities[i]));
        }
        
        // 몇번째로 실행되는지 저장
        int step = 1;
        
        // 프로세스 관리
        while(queue.size()>0){            
            Process process = queue.poll();
            
            // 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있는지 확인
            boolean check = false;
            for(int i=0; i<queue.size(); i++){
                if(process.getPriority() < queue.get(i).getPriority()){
                    check = true;
                }
            }
            
            // 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면
            if (check) {
                // 다시 큐에 넣기
                queue.add(process);
            }
            else {
                // 꺼낸 프로세스 실행
                if (process.getIdx() == location){
                    answer = step;
                    break;
                }
                step ++;
            }
        }
        
        return answer;
    }
}