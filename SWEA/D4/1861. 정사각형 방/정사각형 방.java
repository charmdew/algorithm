import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int roomNum, moveCnt; // 처음 출발 방번호, 최대 몇 개방 이동 가능한지
	
	public static void main(String[] args) throws Exception{
	
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		for(int t=1; t<=T; t++) {
			int N = Integer.parseInt(br.readLine());
			int[][] rooms = new int[N][N];
			
			for(int i=0; i<N; i++) {				
				st = new StringTokenizer(br.readLine(), " ");
				for(int j=0; j<N; j++) {
					rooms[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			roomNum = Integer.MAX_VALUE;
			moveCnt = 0;
			
			// 모든 방에서 시작
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					move(i, j, rooms, N);
				}
			}
			
			System.out.printf("#%d %d %d\n", t, roomNum, moveCnt);
		}
	}
	
	public static void move(int a, int b, int[][] rooms, int N) {
		// 상, 하, 좌, 우
		int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		
		int cnt = 1; // 이동 가능한 방 개수
		
		int x= a, y= b;
		int nx, ny;
		while(true) {
			boolean possible = false; // 이동 가능한 방이 있는지 체크
			
			for(int i=0; i<4; i++) {
				nx = x+dir[i][0];
				ny = y+dir[i][1];
			
				if(nx<0 || nx>=N || ny<0 || ny>=N) continue;
				
				// 현재 방에 적힌 수보다 정확히 1이 크다면
				if(rooms[x][y]+1 == rooms[nx][ny]) {
					cnt += 1;
					x = nx;
					y = ny;
					possible = true;
					break;
				}
			}
			
			// 더 이상 주변에 조건을 만족하는 방이 없다면
			if(!possible) {
				break;
			}
		}
		
		// 값이 더 큰 경우
		if(cnt > moveCnt) {
			moveCnt = cnt;
			roomNum = rooms[a][b];
		}
		
		// 값이 같은 경우
		else if(cnt==moveCnt) {
			// 방번호가 더 작은 값 저장
			if(rooms[a][b]<roomNum) {
				roomNum= rooms[a][b];
			}
		}		
	}
}
