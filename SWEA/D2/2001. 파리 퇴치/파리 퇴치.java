import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(in.readLine());
		
		StringTokenizer st;
		int N, M;
		for(int t=1; t<=T; t++) {
			st = new StringTokenizer(in.readLine(), " ");
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			int[][] sum = new int[N+1][N+1];
			
			for(int i=1; i<=N; i++) {
				st = new StringTokenizer(in.readLine(), " ");
				for(int j=1; j<=N; j++) {
					sum[i][j] = sum[i-1][j]+ sum[i][j-1] - sum[i-1][j-1] + Integer.parseInt(st.nextToken());
				}
			}
			
			int max = -1;
			int area;
			// M x M 크기의 파리채
			for(int i=M; i<=N; i++) {
				for(int j=M; j<=N; j++) {
					area = sum[i][j]-sum[i-M][j]-sum[i][j-M]+sum[i-M][j-M];
					if (area> max) max = area;
				}
			}
			
			System.out.printf("#%d %d\n", t, max);
		}
	}

}
