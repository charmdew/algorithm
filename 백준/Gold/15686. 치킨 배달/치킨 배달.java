import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{

	private static int N, M, chickCnt; // 도시 크기(NxN), 치킨집 최대 개수(M), 치킨집 후보 개수(chickCnt) 
	private static int[] chickHouse = new int[13]; 
	private static int[][] city = new int[50][50]; // 도시의 정보
	private static int[][] chickPos = new int[50][2]; // 치킨집 위치
	private static int minDist = Integer.MAX_VALUE;
	
	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j=0; j<N; j++) {
				city[i][j] = Integer.parseInt(st.nextToken());
				
				if(city[i][j] == 2) {
					chickPos[chickCnt][0] = i;	// 치킨집 행
					chickPos[chickCnt][1] = j;	// 치킨집 열
					chickCnt+=1;
				}
			}
		}
		
		combination(0, 0);
		
		System.out.println(minDist);
	}
	
	// 조합 (치킨집 M개를 뽑는 경우)
	public static void combination(int cnt, int start) {
		
		if(cnt == M) {
			// 도시의 치킨 거리 : 모든 집의 치킨 거리의 합 계산
			int cityDist = 0;
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(city[i][j]==1) { // 집인 경우
						cityDist+= dist(i, j);
					}
				}
			}
			minDist = Math.min(minDist, cityDist);
		}
		 
		for(int i=start; i<chickCnt; i++) {
			chickHouse[cnt] = i;
			combination(cnt+1, i+1);
		}
	}
	
	
	
	// 치킨 거리: 집에서 치킨집까지 거리 계산 
	public static int dist(int r1, int c1) {
		int minDistance = Integer.MAX_VALUE;
		// 반복문 돌면서 최단거리 찾기
		int distance;
		
		int r2, c2;
		for(int i=0; i<M; i++) {
			// 행 : chickPos[chickHouse[i]][0] , 열 : chickPos[chickHouse[i]][1]
			r2 = chickPos[chickHouse[i]][0];
			c2 = chickPos[chickHouse[i]][1];
			
			// 치킨 거리
			distance = Math.abs(r1-r2)+Math.abs(c1-c2);
			// 가장 가까운 치킨집 사이의 거리
			minDistance = distance < minDistance? distance: minDistance;
		}
		return minDistance;
	}
}