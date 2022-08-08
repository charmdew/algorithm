import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws Exception {
		
		// System.setIn(new FileInputStream("res/input_sw_1225.txt"));
		
		// 8 자리 숫자를 입력 받는다
		int N = 8;
		
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		Queue<Integer> password = new LinkedList<>();;
		int test_case;
		while(true) {
			String input = in.readLine();

			if(input== null) {
				break;
			}
			
			test_case = Integer.parseInt(input);
			st = new StringTokenizer(in.readLine(), " ");
			
			for(int i=0; i<N; i++) {
				password.add(Integer.parseInt(st.nextToken()));
			}
			
			int x = 1; // 감소하는 크기
			int last;
			// 첫번 째 숫자를 1 감소한 뒤 맨 뒤로 보냄
			while(true) {			
				last = password.poll();
				last -= x;
				x = (x==5)? 1: x+1;
				
				// last <=0 일경우 0으로 저장되고, 해당 숫자 배열이 암호가 됨
				if (last <= 0) {
					password.add(0);
					break;
				}
				password.add(last);
			}
			
			System.out.printf("#%d ", test_case);
			for (Integer integer : password) {
				System.out.printf("%d ", integer);
			}
			System.out.println();
			password.clear();
		}
	}
}