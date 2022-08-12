import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		// 우선순위 큐를 이용 (배열 담기 : [절댓값, 부호])
		PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				// 절댓값이 같다면, 2번째 원소 기준으로 오름차순 정렬(음수: -1, 양수: 1)
				if(Math.abs(o1[0]) == Math.abs(o2[0])) {
					return o1[1]-o2[1];
				}
				
				// 절댓값으로 오름차순 정렬한다.
				return Math.abs(o1[0])-Math.abs(o2[0]);
			}
			
		});
		
		int x;
		int[] value;
		for(int n=0; n<N; n++) {
			x = Integer.parseInt(br.readLine());
			
			// x==0 이면 절댓값이 가장 작은 값 출력, 그 값 제거
			if(x==0) {
				value = pq.poll();
				
				// 비어있는 경우 '0' 출력, 값이 있는 경우 '절댓값*부호' 
				System.out.println(value==null? 0: value[0]*value[1]);
				
			}
			
			// x!=0 이면 배열에 값을 넣는 연산
			else {
				// [절댓값, 부호]
				pq.add(new int[]{Math.abs(x), x>=0? 1:-1});
			}
		}	
	}
}