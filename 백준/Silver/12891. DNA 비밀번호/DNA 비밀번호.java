import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception{

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(in.readLine(), " ");
		
		int S = Integer.parseInt(st.nextToken());
		int P = Integer.parseInt(st.nextToken());
		
		String DNA = in.readLine();
		
		st = new StringTokenizer(in.readLine(), " ");
		// 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수 저장
		int[] cnt = new int[4];
		for(int i=0; i<4; i++) {
			cnt[i] = Integer.parseInt(st.nextToken());
		}
		
		HashMap<Character, Integer> code = new HashMap<>();
		code.put('A', 0);
		code.put('C', 1);
		code.put('G', 2);
		code.put('T', 3);

		// 만들 수 있는 비밀번호의 종류의 수
		int kindCnt = 0;
		
		// 부분문자열 저장 - Character를 담은 큐 사용
		Queue<Character> queue = new LinkedList<>();

		// 부분 문자열의 {‘A’, ‘C’, ‘G’, ‘T’} 개수
		int[] subCnt = new int[4];
		
		for(int i=0; i<P; i++) {
			queue.add(DNA.charAt(i));
			subCnt[code.get(DNA.charAt(i))] += 1;
		}
		if (check(cnt, subCnt)) kindCnt += 1;
//		System.out.println(queue+", "+kindCnt);
		
		char s, e;
		for(int i= P; i<S; i++) {
			// 처음 문자 빼기
			s = queue.poll();
			// 맨 뒤 문자 넣기
			e = DNA.charAt(i);
			queue.add(e);
			
			subCnt[code.get(s)]-=1;	// 뺀 문자 개수 -1
			subCnt[code.get(e)]+=1;	// 넣은 문자 개수 +1
		
			// 가능한 비밀번호인지 체크
			if (check(cnt, subCnt)) kindCnt += 1;
//			System.out.println(queue+", "+kindCnt);
		}
		System.out.println(kindCnt);
		
	}
	
	// 사용할 수 있는 비밀번호인지 체크
	public static boolean check(int[] cnt, int[] subCnt) {
		for(int i=0; i<4; i++) {	
			// 최소 개수를 만족하지 못한다면
			if(subCnt[i]<cnt[i]) {
				return false;
			}
		}
		return true;
	}

}
