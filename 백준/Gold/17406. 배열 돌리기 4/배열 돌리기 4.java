import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main{

	public static int[][] originArr = new int[50][50];
	public static int[][] arr = new int[50][50];
	public static int[][] info = new int[6][3];
	public static int[] numbers = new int[6];
	public static boolean[] isSelected = new boolean[6];
	public static int N, M, K, rowMin=Integer.MAX_VALUE;
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<M; j++) {				
				originArr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		
		int r, c, s;
		// R번 회전
		for(int k=0; k<K ; k++) {
			st = new StringTokenizer(br.readLine(), " ");
			
			r = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			s = Integer.parseInt(st.nextToken());
			
			info[k][0] = r;
			info[k][1] = c;
			info[k][2] = s;
		}
		
		permutation(0);
		System.out.println(rowMin);
	}
	
	public static void printInfo(int[][] arr) {
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println();
	}
	
	public static void permutation(int cnt) {
		
		if(cnt == K) {
			for(int i=0; i<N; i++) {
				for(int j=0; j<M; j++) {
					arr[i][j] = originArr[i][j];
				}
			}
			
			rotate(numbers, arr);
		}
		
		for(int i=0; i<K; i++) {
			if(isSelected[i]) continue;
			
			numbers[cnt] = i;
			isSelected[i] = true;
			permutation(cnt+1);
			isSelected[i] = false;
		}
	}
	
	public static void rotate(int[] operand, int[][] arr) {
		int idx;
		int sr, sc;
		int r, c, s;
		int cx, cy, px, py;
		int start;
		int[][] dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
		
		for(int k=0; k<K; k++) {
			
			idx = operand[k];
			r = info[idx][0];
			c = info[idx][1];
			s = info[idx][2];
			
			// 시작 위치
			sr= r-s-1;
			sc= c-s-1; 
			
			// 테두리마다 반복
			for(int i=0; i<s; i++) {
				start = arr[sr+i][sc+i]; // 처음 시작 위치 값 저장

				cx = sr+i; cy = sc+i;
				// 테두리를 ↓, →, ↑, ← 순으로 방문하여 반시계 방향으로 돌려줌 
				for(int d=0; d<4; d++) {
					
					for(int j=0; j<2*(s-i); j++) {
						px = cx;
						py = cy;
						
						cx += dir[d][0];
						cy += dir[d][1];

						// 시계 방향으로 돌림
						arr[px][py] = arr[cx][cy];
					}
				}
				arr[sr+i][sc+i+1] = start;
			}
		}
		
		int rowSum=0;
		for(int i=0; i<N; i++) {
			rowSum=0;
			for(int j=0; j<M; j++) {
				rowSum+=arr[i][j];
			}
			rowMin = Math.min(rowMin, rowSum);
		}
	}
}
