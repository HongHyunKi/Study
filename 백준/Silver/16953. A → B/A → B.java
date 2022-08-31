import java.util.*;
import java.io.*;

public class Main {
    static long a,b;
    static int cnt;

    static int bfs(){
        Queue<Long> q = new LinkedList<>();
        q.add(a);

        while(!q.isEmpty()){
            int size = q.size();

            for(int i = 0; i < size; i++){
                long temp = q.poll();
                if(temp==b)
                    return cnt+1;

                if(temp*2<=b) 
                	q.add(temp*2);                	
                
                if(temp*10+1<=b) 
                	q.add(temp*10+1);
            }
            cnt++;
        }
        return -1;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        a = Long.parseLong(st.nextToken());
        b = Long.parseLong(st.nextToken());

        System.out.println(bfs());
    }
}