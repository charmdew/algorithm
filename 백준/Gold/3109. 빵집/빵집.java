import java.util.*;
import java.io.*;

// 시간초과 뜨는 코드입니다..
public class Main {
	
	static int R, C, pipeCnt;
	static char[][] arr;
	// 오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선
	static int[][] dir = {{-1, 1},{0, 1},{1, 1}};

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
	
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		arr = new char[R][];
		for(int i=0; i<R; i++) {
			arr[i] = br.readLine().toCharArray();
		}

		for(int i=0; i<R; i++) {
			if(pipeline(i, 0)) pipeCnt++;
		}
		System.out.println(pipeCnt);
		
//		for(int i=0; i<R; i++) {
//			for(int j=0; j<C; j++) {
//				System.out.print(arr[i][j]);
//			}
//			System.out.println();
//		}
	}
	
	private static boolean pipeline(int r, int c) {		
//		System.out.println(r+", "+c);
		// 방문체크
		arr[r][c] = '-';

		if(c==C-1) { // 마지막 열에 도착했을때
			return true;
		}
		
		int nr, nc;
		// 오른쪽 위 대각선, 오른쪽, 오른쪽 아래 대각선 확인
		for(int i=0; i<3; i++) {
			nr = r+ dir[i][0];
			nc = c+ dir[i][1];
			
			// 경계 확인, 파이프라인 놓을 수 있는 곳인지 
			if (nr>=0 && nr<R && arr[nr][nc]=='.') {
				if(pipeline(nr, nc))
					return true;
			}
		}
		
		return false;
	}
}