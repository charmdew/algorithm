import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception{
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	
		StringTokenizer st;
		
		st = new StringTokenizer(in.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] nums = new int[N+1];
		int[] sum = new int[N+1]; // sum[i]: 구간(1)~구간(i)까지의 합 저장
		sum[0] = 0;
		st = new StringTokenizer(in.readLine(), " ");
		for(int i=1; i<=N; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
			sum[i] = sum[i-1]+nums[i];
		}
		
//		System.out.println(Arrays.toString(nums));
//		System.out.println(Arrays.toString(sum));
		
		int s, e;	// 구간 시작, 끝
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(in.readLine(), " ");
			
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			
			
			System.out.println(sum[e]-sum[s-1]);
		}
	}
}
