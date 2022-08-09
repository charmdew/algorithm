import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 색종이 수 입력
		int N = Integer.parseInt(br.readLine());
		
		// 도화지 
		int[][] paper = new int[100][100];
		
		StringTokenizer st;
		int r, c;
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			// 넗이를 구하는 것이므로 행, 열로 받아와도 상관없다!
			r = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			
			// 색종이 붙인 영역 도화지에 표시
			for(int dr=0; dr<10; dr++) {
				for(int dc=0; dc<10; dc++) {
					if(paper[r+dr][c+dc]==0) paper[r+dr][c+dc] = 1;
				}
			}
		}
		
		// 색종이가 붙은 검은 영역의 넓이 저장
		int area = 0;
		// 영역 더하기
		for(int i=0; i<100; i++) {
			for(int j=0; j<100; j++) {
				area += paper[i][j];
			}
		}
		System.out.println(area);
	}
}