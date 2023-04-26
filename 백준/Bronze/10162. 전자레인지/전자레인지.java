import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine(); // 한 줄의 문자열 입력
        int T = Integer.parseInt(input);
        
        int A = T / 300; // 5분
        T %= 300;
        
        int B = T / 60; // 1분
        T %= 60;
        
        int C = T / 10; // 10초
        T %= 10;
        
        if(T != 0) {
        	System.out.println(-1);
        } else {
        	System.out.println(A+" "+B+" "+C);
        }
	}
}
