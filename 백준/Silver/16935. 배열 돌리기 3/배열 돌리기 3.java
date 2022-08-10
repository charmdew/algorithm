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
			
			if(operand<=2) {
				arr = reverse(arr, N, M, operand);
			} else if(operand <=4) {
				arr = rotate(arr, N, M, operand);
				
				// 행, 열 크기 변경
				tmp = N;
				N=M; 
				M=tmp; 
			} else {
				arr = move(arr, N, M, operand);
			}
		}
		printInfo(arr, N, M);
	}
	
	public static int[][] reverse(int[][] arr, int N, int M, int operand) {
		int[][] newArr =  new int[N][M]; // 임시 배열
		
		int r, c;
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(operand==1) {
					r= N-1-i;
					c= j;
				}
				else {
					r= i;
					c= M-1-j;	
				}
				newArr[i][j] = arr[r][c];
				
			}
		}
		
		return newArr;
	}
	
	public static int[][] rotate(int[][] arr, int N, int M, int operand) {
		int[][] newArr =  new int[M][N]; // 임시 배열
		
		int r, c;
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {					
				if(operand==3) {
					r= j;
					c= N-1-i;
				}
				else {
					r= M-1-j;
					c= i;	
				}
				newArr[r][c] = arr[i][j];
			}
		}
		return newArr;
	}
	
	public static int[][] move(int[][] arr, int N, int M, int operand) {
		int[][] newArr =  new int[N][M]; // 임시 배열
		int[][] points = {{0, 0}, {0, M/2}, {N/2, M/2}, {N/2, 0}}; //부분배열 좌측 상단 꼭지점
		
		int p1, p2;
		for(int g=0; g<4; g++) {
			if(operand==5) {
				p1 = 3-g;
				p2 = (6-g)%4;
			}
			else {
				p1 = g;
				p2 = (g+1)%4;
			}
			for(int i=0; i<N/2; i++) {
				for(int j=0; j<M/2; j++) {
					newArr[points[p1][0]+i][points[p1][1]+j] = arr[points[p2][0]+i][points[p2][1]+j];
				}
			}
		}
		
		return newArr;
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
