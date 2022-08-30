import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		List<Integer> list[] = new ArrayList [N+1]; //이부분 신기하네
		
		for(int i=0; i<list.length; i++) {
			list[i] = new ArrayList<Integer>();
		}
		
		for(int i=0; i < N-1; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			list[a].add(b);
			list[b].add(a);
		}
		
		boolean visit[] = new boolean[N+1];
		Queue<Integer> queue = new LinkedList<Integer>();
		
		queue.add(1);
		visit[1] = true;
		
		int answer[] = new int[N+1];
		while(!queue.isEmpty()) {
			Integer num = queue.poll();
			for(Integer i : list[num]) {
				if(!visit[i]) {
					visit[i] = true;
					answer[i] = num;
					queue.add(i);
				}
			}
		}
		for(int i=2; i < answer.length; i++) {
			System.out.println(answer[i]);
		}
		
	}
}
