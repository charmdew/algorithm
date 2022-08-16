import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	private static int N;
	private static int[][] paper = new int[128][128];
	private static int[] count = {0, 0}; // 색종이 개수 - [0]: 하얀색, [1]: 파란색 
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		N = Integer.parseInt(br.readLine());
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			
			for(int j=0; j<N; j++) {
				paper[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		makeColoredPaper(0, 0, paper[0][0], N);
		System.out.println(count[0]);
		System.out.println(count[1]);
	}
	
	// 색종이 만들기
	private static void makeColoredPaper(int r, int c, int color, int size) {
		// 칸이 1개라면
		if(size==1) {
			count[color]++;
			return;
		}

		// 좌측 상단 좌표 (r, c)
		for(int i=r; i<r+size; i++) {
			for(int j=c; j<c+size; j++) {
				// 만약 색이 같지 않다면
				if(color!= paper[i][j]) {
					// 분할
					makeColoredPaper(r, c, paper[r][c], size/2);
					makeColoredPaper(r+size/2, c, paper[r+size/2][c], size/2);
					makeColoredPaper(r, c+size/2, paper[r][c+size/2], size/2);
					makeColoredPaper(r+size/2, c+size/2, paper[r+size/2][c+size/2], size/2);
					return;
				}
			}
		}
		
		// 만약 모든 칸의 색이 같다면 색종이 개수 증가
		count[color]++;
	}
}