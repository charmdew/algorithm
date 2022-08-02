import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

	public static void main(String[] args) throws Exception {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(in.readLine());
		
		// 시계방향(오른쪽, 아래, 왼쪽, 위) 순으로 이동 
		int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
		
		for(int t=1; t<=T; t++) {
            System.out.println("#"+t);
            
			int N = Integer.parseInt(in.readLine());
			
			int[][] arr = new int[N][N];
			
			int d=0;		// 방향 초기화(오른쪽)
			int r=0, c=-1;	// 시작점 초기화
			int num = 1;	
			
			for(int n=N; n>0; n--) {
				for(int i=0; i<2; i++) {
					// d 방향으로 n칸 이동
					for(int k=0; k<n; k++) {
						r = r+ dir[d][0];
						c = c+ dir[d][1];
						
						arr[r][c] = num++;
					}
					
					// 이동 방향 바꾸기
					d = (d+1)%4; 
					
					// N칸 이동은 한번만
					if(n==N) break;
				}
			}
			
			for (int i = 0; i < N; i++) {
				for(int j=0; j<N; j++) {
					System.out.printf("%d ", arr[i][j]);
				}
				System.out.println();
			}
		}
	}
}
