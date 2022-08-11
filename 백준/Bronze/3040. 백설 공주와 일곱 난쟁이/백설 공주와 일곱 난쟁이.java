import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main{

	public static int[] dwarfs = new int[9];
	public static int[] numbers = new int[7];
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		for(int i=0; i<9; i++) {
			dwarfs[i] = Integer.parseInt(br.readLine());
		}
		
		combination(0, 0);
	}
	
	public static void combination(int cnt, int start) {
		
		// 난쟁이를 7명 뽑은 경우
		if(cnt==7) {
			int sum = 0;
			for(int i=0; i<7; i++) {
				sum += numbers[i];
			}
			if (sum==100) {
				for(int i=0; i<7; i++) {
					System.out.println(numbers[i]);
				}
			}
			return;
		}
		
		for(int i=start; i<9; i++) {
			numbers[cnt] = dwarfs[i];
			combination(cnt+1, i+1);
		}
	}
}