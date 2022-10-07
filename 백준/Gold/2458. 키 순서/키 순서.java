import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, M;
	static boolean[][] d;
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		d = new boolean[N][N];
		
		int a, b;
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			
			d[a-1][b-1] = true;
		}
		for (int i = 0; i < N; i++) {
			d[i][i] = true;
		}
		
		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if(d[i][j]) continue;
					
					if(d[i][k] && d[k][j])
						d[i][j] = true;
				}
			}
		}
		
		boolean know;
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			know = true;
			
			for (int j = 0; j < N; j++) {
				if(!d[i][j] && !d[j][i]) {
					know = false;
					break;
				}
			}
			
			if(know) {
				cnt++;
			}
		}
		
		System.out.println(cnt);
	}

}