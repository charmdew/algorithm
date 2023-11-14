class Solution {
    int answer = 0;
    
    public void dfs(int[] numbers, int target, int n, int idx, int result) {
        if (idx == n) {
            // 타겟 넘버를 만든 경우
            if(result == target){
                answer++;
            }
            return;
        }
        
        // 더하는 경우
        dfs(numbers, target, n, idx+1, result+numbers[idx]);
        // 빼는 경우
        dfs(numbers, target, n, idx+1, result-numbers[idx]);
    }
    
    
    public int solution(int[] numbers, int target) {
        dfs(numbers, target, numbers.length, 0, 0);
        return answer;
    }
}