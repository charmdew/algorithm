import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		// 최대한 적은 봉지를 들고 가려고 함
		// 3kg, 5kg 봉지 - 5kg 봉지를 최대한 많이 들고 가기!
		
		int bag3Cnt = -1; // 3kg 봉지 개수
		int bag5Cnt = -1; // 5kg 봉지 개수
		
		int weight;
		for(int i=N/5; i>=0; i--) {
			weight = 5*i; // 5kg 봉지로 채운 무게

			// 남은 무게가 3kg로 떨어지지 않으면 다음 경우
			if((N-weight)%3!=0) continue;
			
			bag5Cnt = i;
			bag3Cnt = (N-weight)/3;
			break; // 조건을 만족하면서 5kg 봉지가 제일 많은 경우이므로 break!
		}
		
		// 정확하게 N킬로그램을 만들 수 없다면 -1 출력
		if(bag3Cnt==-1 && bag5Cnt==-1) {
			System.out.println(-1);
		}
		else {
			System.out.println(bag3Cnt+bag5Cnt);
		}
	}
}