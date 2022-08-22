import java.util.*;
import java.io.*;

public class Main {

	static int L, C;
	static char[] alphabet;
	static char[] pwd;
	static char[] vowel = {'a', 'e','i','o','u'};
	
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		pwd = new char[L]; // 암호 저장
		alphabet = new char[C]; // 알파벳 저장
		st = new StringTokenizer(br.readLine(), " ");
		for(int i=0; i<C; i++) {
			alphabet[i] = st.nextToken().charAt(0);
		}
		
		// 알파벳 배열 정렬
		Arrays.sort(alphabet);
		
		// C개의 알파벳 중에서 L개를 뽑는 경우(조합)
		comb(0, 0);
	}

	private static void comb(int cnt, int start) {
		// 암호 후보 완성
		if(cnt == L) {
			// 암호 조건을 만족하면 출력
			if(check()) {
				for(int i=0; i<L; i++) {
					System.out.print(pwd[i]);
				}
				System.out.println();
			}
			return;
		}
		
		for(int i=start; i<C; i++) {
			pwd[cnt] = alphabet[i];
			comb(cnt+1, i+1);
		}
	}
	
	// 암호 조건 확인
	private static boolean check() {
		int vowelCnt=0; // 모음 개수
		
		for(int i=0; i<L; i++) {
			// 모음인지 확인
			for(int j=0; j<5; j++) {
				if(pwd[i]==vowel[j]) {
					vowelCnt++;
					break;
				}
			}
		}
		
		// 최소 한 개의 모음과 최소 두 개의 자음
		if(vowelCnt>=1 && L-vowelCnt>=2) {
			return true;
		}
		return false;
	}
}