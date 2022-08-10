import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		
		int[][] arr = new int[N][M];
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<M; j++) {				
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 테두리 개수
		int bound = Math.min(N, M)/2;
		
		int cx, cy, px, py;
		int start, n, m, l;
		
		int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
		
		int nR; // 반복 횟수
		// 테두리마다 반복
		for(int i=0; i<bound; i++) {
			n = N-1-2*i;	// 테두리 세로 길이-1
			m = M-1-2*i;	// 테두리 가로 길이-1

			nR = R%(2*(n+m));
			
			for(int r=0; r<nR; r++) {
				start = arr[i][i]; // 처음 시작 위치 값 저장
				cx = i; cy = i;
				// 테두리를 →, ↓, ←, ↑ 순으로 방문하여 반시계 방향으로 돌려줌 
				for(int d=0; d<4; d++) {
					l =(d%2==0)? m:n; 
					
					for(int j=0; j<l; j++) {
						px = cx;
						py = cy;
						
						cx += dir[d][0];
						cy += dir[d][1];

						// 반시계 방향으로 돌림
						arr[px][py] = arr[cx][cy];
					}
				}
				arr[i+1][i] = start;
			}
		}
		
		printInfo(arr, N, M);
	}
	
	public static void printInfo(int[][] arr, int N, int M) {
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
	}
}