import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), "-"); // 식 입력, '-' 부호 기준으로 자르기
		StringTokenizer st2;
		
		String ex;
		int sum, result = 0, sign = 1;
		
		do {
			sum = 0; // 부분식의 합 저장
			ex = st.nextToken(); 
			st2 = new StringTokenizer(ex, "+");
			while(st2.hasMoreTokens()) {
				sum += Integer.parseInt(st2.nextToken());
			}
			
			result += sign*sum;
			sign = -1; // -부호가 나온 후로는 모두 빼주기
		} while(st.hasMoreTokens());
		
		System.out.println(result);
	}
}