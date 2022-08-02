import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class Main {
	public static void main(String[] args) throws Exception{
			
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	
		int sSize = Integer.parseInt(in.readLine());
		int[] state = new int[sSize+1];
		
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		for (int i = 1; i <= sSize; i++) {
			state[i] = Integer.parseInt(st.nextToken());
		}
	
		int pSize = Integer.parseInt(in.readLine());
		for (int p = 0; p < pSize; p++) {
			st = new StringTokenizer(in.readLine(), " ");
			
			int gender = Integer.parseInt(st.nextToken());
			int n = Integer.parseInt(st.nextToken());

			// 남학생인 경우
			if (gender == 1) {
				// 받은 수의 배수 번호 스위치 상태변경
				for (int k = n; k <= sSize; k += n) {
					state[k] = 1 - state[k];
				}
			}
	
			// 여학생인 경우
			else {
				// 자기 자신 상태변경
				state[n] = 1 - state[n];
	
				int k = 1;
				int left = n-k, right= n+k;
				// 좌우 대칭인 부분 스위치 상태변경
				while (0 < left&& right <= sSize && state[left] == state[right]) {
					// 좌우 같으면 상태변경
					state[left] = 1 - state[left];
					state[right] = 1 - state[right];
					k++;
					left = n-k; 
					right= n+k;
				}
			}
		}
	
		// 스위치 상태 출력
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= sSize; i++) {
			sb.append(state[i]).append(" ");
			if(i%20==0) sb.append("\n");
		}
		System.out.println(sb);
	}
}