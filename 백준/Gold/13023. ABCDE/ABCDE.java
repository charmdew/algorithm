import java.util.*;
import java.io.*;

public class Main {

	static int N, M, depth;
	static ArrayList<Integer>[] adjList;
	static boolean[] visited;
	static boolean abcde;
	
	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		adjList = new ArrayList[N];
		for(int i=0; i<N; i++) {
			adjList[i] = new ArrayList<Integer>();
		}
	
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			
			adjList[from].add(to);
			adjList[to].add(from);
		}
		
//		dfs(0, 0);
		for(int i=0; i<N; i++) {
			visited = new boolean[N];
			dfs(i, 0);
			if(abcde) break;
		}
		System.out.println(abcde? 1:0);
	}

	private static void dfs(int x, int depth) {	
		if(depth==4) {
			abcde = true;
			return;
		}
		
		visited[x] = true;
		
		for(Integer to: adjList[x]) {
			if(visited[to]) continue;
			
			dfs(to, depth+1);
		}
		visited[x] = false;
	}
}