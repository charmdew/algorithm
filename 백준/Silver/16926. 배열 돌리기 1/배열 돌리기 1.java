import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int R = Integer.parseInt(st.nextToken());
		
		int[][] arr = new int[N][M];
		int[][] newArr = new int[N][M];
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<M; j++) {				
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
//		printInfo(arr, N, M);
		
		int bound = Math.min(N, M)/2;
		
		int cx, cy, px, py;
		int start, n, m;
		
		int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
		
		for(int r=0; r<R; r++) {
			for(int i=0; i<bound; i++) {
				start = arr[i][i];
				n = N-1-2*i;
				m = M-1-2*i;
				
				cx = i;
				cy = i;
				for(int d=0; d<4; d++) {
					if (d%2==0) {
						for(int j=0; j<m; j++) {
							px = cx;
							py = cy;
							
							cx += dir[d][0];
							cy += dir[d][1];
//							System.out.println(px+", "+py+"<-"+ cx+", "+cy);
							
							arr[px][py] = arr[cx][cy];
						}
					}
					
					else {
						for(int j=0; j<n; j++) {
							px = cx;
							py = cy;
							
							cx += dir[d][0];
							cy += dir[d][1];
//							System.out.println(px+", "+py+"<-"+ cx+", "+cy);
							arr[px][py] = arr[cx][cy];
						}
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