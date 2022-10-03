import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int K = Integer.parseInt(br.readLine());

		st = new StringTokenizer(br.readLine());
		int W = Integer.parseInt(st.nextToken()); // 격자판 가로길이
		int H = Integer.parseInt(st.nextToken()); // 격자판 세로길이
		
		if(W==1 && H==1) {
			System.out.println(0);
			return;
		}

		int[][] board = new int[H][W];
		// 0: 평지, 1: 장애물
		// 시작점 (0, 0), 도착점 (H-1, W-1)
		for (int i = 0; i < H; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < W; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 말의 움직임
		int[][] hdir = { { -1, -2 }, { -2, -1 }, { -2, 1 }, { -1, 2 }, { 1, -2 }, { 2, -1 }, { 2, 1 }, { 1, 2 } };

		// 인접한 칸으로 움직임 (상하좌우)
		int[][] dir = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
		
		int[] monkey;
		
//		int arr[][][] = new int[H][W][K+1];
//		for (int i = 0; i < H; i++) {
//			for (int j = 0; j < W; j++) {
//				for (int k = 0; k < K+1; k++) {
//					arr[i][j][k] = Integer.MAX_VALUE;
//				}
//			}
//		}
		
		// 방문 배열
		boolean visited[][][] = new boolean[H][W][K+1];
		visited[0][0][0] = true;
		
		// 위치, 남은 k수
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[]{0, 0, 0, K});
		
		int min = Integer.MAX_VALUE;
		int nr, nc;
		while(!queue.isEmpty()) {
			
			monkey = queue.poll();
			
			if(monkey[0]==H-1 && monkey[1]==W-1) {
				min = monkey[2];
				break;
			}
			
			if(monkey[3]>0) {
				// 말 움직이기
				
				for (int i = 0; i < 8; i++) {
					nr = monkey[0]+hdir[i][0];
					nc = monkey[1]+hdir[i][1];
					
					if(checkBoundary(nr, nc, H, W) && board[nr][nc]==0  && !visited[nr][nc][monkey[3]-1]) {
						visited[nr][nc][monkey[3]-1] = true;
						
						queue.add(new int[] {nr, nc, monkey[2]+1, monkey[3]-1});
					}
				}
			}
			
			for (int i = 0; i < 4; i++) {
				nr = monkey[0]+dir[i][0];
				nc = monkey[1]+dir[i][1];
				
				if(checkBoundary(nr, nc, H, W) && board[nr][nc]==0 && !visited[nr][nc][monkey[3]]) {
					visited[nr][nc][monkey[3]] = true;
					
					queue.add(new int[] {nr, nc, monkey[2]+1, monkey[3]});
				}
			}
		}
		
		System.out.println(min<Integer.MAX_VALUE ? min: -1);
	}

	public static boolean checkBoundary(int r, int c, int H, int W) {
		return 0 <= r && r < H && 0 <= c && c < W;
	}
}