import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
	
	private static int[][] arr = new int[9][9];
	private static List<int[]> list = new ArrayList<int[]>();
	
	public static void sudoku(int cnt) {
		if (list.size()== cnt) {
			for(int i=0; i<9; i++) {
				for(int j=0; j<9; j++) {
					System.out.print(arr[i][j]);
				}
				System.out.println();
			}
			System.exit(0);
		}
		
		int r = list.get(cnt)[0];
		int c = list.get(cnt)[1];

		boolean[] check = new boolean[10];
		
		// 행 검사
		for(int i=0; i<9; i++) {
			if(arr[i][c]!=0) {
				check[arr[i][c]] = true;
			}
		}
		
		// 열 검사
		for(int i=0; i<9; i++) {
			if(arr[r][i]!=0) {
				check[arr[r][i]] = true;
			}
		}
		
		// 사각형 검사
		for(int i=0; i<3; i++) {
			for(int j=0; j<3; j++) {
				if(arr[(r/3)*3+i][(c/3)*3+j]!=0) {
					check[arr[(r/3)*3+i][(c/3)*3+j]] = true;
				}
			}
		}
		
		for(int i=1; i<10; i++) {
			if(!check[i]) {
				arr[r][c] = i;
				sudoku(cnt+1);
				arr[r][c] = 0;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input;
		
		// 9개의 줄에 9개의 숫자
		for(int i=0; i<9; i++) {
			input = br.readLine();
			
			for (int j = 0; j < 9; j++) {
				arr[i][j] = input.charAt(j)-'0';
				
				if(arr[i][j]==0) list.add(new int[] {i, j});
			}
		}
		
		sudoku(0);
		
	}
}
