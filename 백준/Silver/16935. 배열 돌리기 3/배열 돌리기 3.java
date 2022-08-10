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
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<M; j++) {				
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		st = new StringTokenizer(br.readLine(), " ");
		int operand;
		int tmp;
		for(int r=0; r<R; r++) {
			operand = Integer.parseInt(st.nextToken());
			
			int[][] newArr = null; // 임시 배열
			int[][] points = {{0, 0}, {0, M/2}, {N/2, M/2}, {N/2, 0}}; //부분배열 좌측 상단 꼭지점
			
			switch(operand) {
			case 1: // 1번 연산 : 상하 반전
				newArr = new int[N][];
				for(int i=0; i<N; i++) {
					newArr[i] = arr[N-1-i];
				}
				break;
			case 2: // 2번 연산 : 좌우 반전
				newArr = new int[N][M];
				for(int i=0; i<N; i++) {
					for(int j=0; j<M; j++) {						
						newArr[i][j] = arr[i][M-1-j];
					}
				}
				break;
			case 3: // 3번 연산 : 오른쪽으로 90도 회전
				newArr = new int[M][N];
				for(int i=0; i<N; i++) {
					for(int j=0; j<M; j++) {
						newArr[j][N-1-i] = arr[i][j];
					}
				}
				tmp = N;
				N =  M;
				M = tmp;
				break;
			case 4: // 4번 연산 : 왼쪽으로 90도 회전
				newArr = new int[M][N];
				for(int i=0; i<N; i++) {
					for(int j=0; j<M; j++) {
						newArr[M-1-j][i] = arr[i][j];
					}
				}
				tmp = N;
				N =  M;
				M = tmp;
				break;
			case 5: // 5번 연산 : 1→2→3→4→1
				newArr = new int[N][M];
				
				for(int g=0; g<4; g++) {
					for(int i=0; i<N/2; i++) {
						for(int j=0; j<M/2; j++) {
							newArr[points[3-g][0]+i][points[3-g][1]+j] = arr[points[(6-g)%4][0]+i][points[(6-g)%4][1]+j];
						}
					}
				}
				
				break;
			case 6: // 6번 연산 : 4→3→2→1→4
				newArr = new int[N][M];
				
				for(int g=0; g<4; g++) {
					for(int i=0; i<N/2; i++) {
						for(int j=0; j<M/2; j++) {
							newArr[points[g][0]+i][points[g][1]+j] = arr[points[(g+1)%4][0]+i][points[(g+1)%4][1]+j];
						}
					}
				}
				break;
				
			}
			arr = newArr;
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