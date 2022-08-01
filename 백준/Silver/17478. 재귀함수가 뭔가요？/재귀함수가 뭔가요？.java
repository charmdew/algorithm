import java.util.Scanner;

public class Main {

	static int N;	// 출력을 원하는 재귀 횟수	
	static String front="_";
	
	static void printContent(int cnt, String content) {
		for (int i = 0; i < 4*cnt; i++) {
			System.out.print("_");
		}
		System.out.println(content);
	}
	
	static void recur(int n) { 
		printContent(n, "\"재귀함수가 뭔가요?\"");
		if (n==N) {
			printContent(n, "\"재귀함수는 자기 자신을 호출하는 함수라네\"");
			printContent(n, "라고 답변하였지.");
			return;
		}
		
		printContent(n, "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.");
		printContent(n, "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.");
		printContent(n, "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"");
		recur(n+1);
		printContent(n, "라고 답변하였지.");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		
		System.out.println("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
		recur(0);
	}

}
