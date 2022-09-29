import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	
	static int[] dp;

	public static int oper(int N) {
		
		if(N==1) {
			return 0;
		}
		
		if(dp[N]==0) {
			
			if(N%6==0) { // 6으로 나눠지는 경우
				dp[N] = Math.min(oper(N-1), Math.min(oper(N/3), oper(N/2)))+ 1;
			} 
			
			else if(N%3==0) { // 3으로만 나눠지는 경우
				dp[N] = Math.min(oper(N/3), oper(N-1))+1;
			}
			
			else if(N%2==0) { // 2로만 나눠지는 경우
				dp[N] = Math.min(oper(N/2), oper(N-1))+1;
			}
			
			else { // 2와 3으로 나눠지지 않는 경우
				dp[N] = oper(N-1)+1;
			}
		}
		
		return dp[N];
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		if(N==1) {
			System.out.println(0);
			return;
		}
		
		dp = new int[N+1];
		
		System.out.println(oper(N));
	}
	
}