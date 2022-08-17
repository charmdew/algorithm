import java.io.*;
import java.util.*;

public class Solution {

	static int M, A;
	static int[][][] map;
	static int[][] BC;
	static List<Integer> abc= new ArrayList<>();
	static List<Integer> bbc= new ArrayList<>();
	
	public static void main(String[] args) throws Exception{

		// System.setIn(new FileInputStream("res/input_sw_5644.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine()); 
		
		// 이동 (이동 X, 상, 우, 하, 좌)
		int[][] dir = {{0, 0}, {-1, 0}, {0, 1}, {1, 0}, {0, -1}};
		
		int sum; // 모든 사용자가 충전한 양의 합의 최댓값
		
		for(int t=1; t<=T; t++) {
			map = new int[11][11][2];
			
			st = new StringTokenizer(br.readLine(), " ");
			M = Integer.parseInt(st.nextToken()); // 총 이동 시간
			A = Integer.parseInt(st.nextToken()); // BC의 개수

			int[] inputA = new int[M];
			int[] inputB = new int[M];
			BC = new int[A][];
			
			st = new StringTokenizer(br.readLine(), " ");
			for(int i=0; i<M; i++) {
				inputA[i] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine(), " ");
			for(int i=0; i<M; i++) {
				inputB[i] = Integer.parseInt(st.nextToken());
			}
			sum = 0;
			// BC 정보
			int X, Y, C, P;
			for(int i=0; i<A; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				X = Integer.parseInt(st.nextToken());
				Y = Integer.parseInt(st.nextToken()); 
				C = Integer.parseInt(st.nextToken()); // 충전 범위
				P = Integer.parseInt(st.nextToken()); // 충전량
			
				BC[i] = new int[] {X, Y, C, P};
			}
			
			// BC 충전량 내림차순 정렬
			Arrays.sort(BC, (o1, o2)-> o2[3]-o1[3]);
			
			// 초기 위치 확인
			int ax=1, ay=1, bx = 10, by=10;

			checkBC(ax, ay, bx, by);
			sum += calc();
			
			for (int i = 0; i < M; i++) {
				ay += dir[inputA[i]][0];
				ax += dir[inputA[i]][1];
				by += dir[inputB[i]][0];
				bx += dir[inputB[i]][1];
				
				checkBC(ax, ay, bx, by);
				sum += calc();
			}
			System.out.printf("#%d %d\n", t, sum);
		}
	}

	private static void checkBC(int ax, int ay, int bx, int by) {
		for(int i=0; i<A; i++) {
			// 거리 확인
			if( (Math.abs(ay-BC[i][1])+ Math.abs(ax-BC[i][0]))<= BC[i][2]) {
				abc.add(i);
			}
			if( (Math.abs(by-BC[i][1])+ Math.abs(bx-BC[i][0]))<= BC[i][2]) {
				bbc.add(i);
			}
		}
	}
	
	private static int calc() {
		int sizeA = abc.size();
		int sizeB = bbc.size();
		int ap = 0, bp = 0;
		int max = 0;
		
		if(sizeA == 0 && sizeB == 0) {
			return 0;
		} else if(sizeA == 0) {
			for(int b : bbc) {
				int sum = BC[b][3];
				bp = sum > bp ? sum : bp;
			}
		} else if(sizeB == 0) {
			for(int a : abc) {
				int sum = BC[a][3];
				ap = sum > ap ? sum : ap;
			}
		} else {
			for(int a : abc) {
				for(int b : bbc) {
					int sum = 0;
					
					if(a == b) {
						sum = BC[a][3];
						
						if(sum > max) {
							ap = sum / 2;
							bp = sum / 2;
							max = sum;
						}
					} else {
						sum = BC[a][3] + BC[b][3];

						if(sum > max) {
							ap = BC[a][3];
							bp = BC[b][3];
							max = sum;
						}
					}
				}
			}
		}
		
		abc.clear();
		bbc.clear();
		
		return ap+bp;
	}
}