import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{

	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[][] arr = new int[N+1][N+1];
		
		for(int i=1; i<=N; i++) {
			st = new StringTokenizer(in.readLine(), " ");
			for(int j=1; j<=N; j++) {				
				arr[i][j] = Integer.parseInt(st.nextToken())+ arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1];
			}
		}
		
//		for(int i=0; i<=N; i++) {
//			System.out.println(Arrays.toString(arr[i]));
//		}
		
		int x1, y1, x2, y2, area;
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(in.readLine(), " ");
			
			x1= Integer.parseInt(st.nextToken())-1;
			y1= Integer.parseInt(st.nextToken())-1;
			x2= Integer.parseInt(st.nextToken());
			y2= Integer.parseInt(st.nextToken());
			
			// (x1, y1)부터 (x2, y2)의 합
			area = arr[x2][y2]+arr[x1][y1]-arr[x2][y1]-arr[x1][y2];
			
			System.out.println(area);
		}
	}
}
