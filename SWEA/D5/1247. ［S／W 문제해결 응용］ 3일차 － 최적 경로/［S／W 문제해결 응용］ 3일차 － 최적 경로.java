import java.util.*;
import java.io.*;

public class Solution {
	
	static int N;
	static int cx, cy, hx, hy; // 회사 좌표, 집 좌표
	static int[][] customer;
	static int[] visitOrder; // 방문 순서 저장
	static boolean[] isSelected;
	static int minDistance; // 최단 경로의 이동거리 저장
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		for(int t=1; t<=T; t++) {
			minDistance = Integer.MAX_VALUE;
			
			N = Integer.parseInt(br.readLine()); // 고객의 수 
			customer = new int[N][];
			visitOrder = new int[N];
			isSelected = new boolean[N];
			
			st = new StringTokenizer(br.readLine());
			
			// 회사 좌표
			cx = Integer.parseInt(st.nextToken());
			cy = Integer.parseInt(st.nextToken());

			// 집 좌표
			hx = Integer.parseInt(st.nextToken());
			hy = Integer.parseInt(st.nextToken());
			
			// 고객 좌표
			for(int i=0; i<N; i++) {
				customer[i] = new int[] {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
			}
			
			// 회사에서 출발 -> 고객 모두 방문 -> 집에 돌아옴 : 최단 경로 구하기
			// 모든 가능한 경로 확인 - N명 고객을 방문하는 모든 순서를 다 확인!! (순열)
			permutation(0);
			
			
			System.out.printf("#%d %d\n", t, minDistance);
		}
	}
	
	private static void permutation(int cnt) {
		if(cnt==N) {
			// 방문 순서 완성!
			// 이동 경로 확인
			int distance=0;
			// 회사-> 첫번째 고객
			distance += Math.abs(cx-customer[visitOrder[0]][0])+Math.abs(cy-customer[visitOrder[0]][1]);
			// 고객 방문
			for(int i=0; i<N-1; i++) {
				distance+= Math.abs(customer[visitOrder[i]][0]-customer[visitOrder[i+1]][0])+Math.abs(customer[visitOrder[i]][1]-customer[visitOrder[i+1]][1]);
			}
			// 마지막 고객 -> 집
			distance += Math.abs(customer[visitOrder[N-1]][0]-hx)+Math.abs(customer[visitOrder[N-1]][1]-hy);
			
			minDistance = Math.min(distance, minDistance);
			return;
		}
		
		for(int i=0; i<N; i++) {
			if(isSelected[i]) continue; // 선택되었다면
			
			visitOrder[cnt] = i;
			isSelected[i] = true;
			permutation(cnt+1);
			isSelected[i] = false;
		}
	}
}

/*
1
5
0 0 100 100 70 40 30 10 10 5 90 70 50 20
*/