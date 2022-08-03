import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		// M 이상 N이하의 소수 모두 출력
		Scanner sc = new Scanner(System.in);
		int M = sc.nextInt();
		int N = sc.nextInt();
				
		// isPrime[n] : n이 소수이면 1, n이 소수가 아니면 0
		int[] isPrime = new int[N+1];
		Arrays.fill(isPrime, 1);
		
		// 0, 1은 소수 아님!
		isPrime[0] = 0;	
		isPrime[1] = 0;
		
		for (int i = 2; i < Math.sqrt(N)+1; i++) {
			if(isPrime[i]==0) continue;
			
			int j=2;
			while (i*j<=N) {
				if(isPrime[i*j]==1) isPrime[i*j]=0;
				j++;
			}
		}
		
		for (int n=M; n<=N; n++) {
			if(isPrime[n]==1) System.out.println(n);
		}
	}

}
