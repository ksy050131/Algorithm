import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long sum = 0;
        long xor = 0;
        
        int phase = sc.nextInt();
        sc.nextLine(); // buffer clear

        for (int i = 0; i < phase; i++) {
            String line = sc.nextLine(); // 한 줄 통째로 읽기
            String[] token = line.split(" "); // 공백 기준 분리

            int command = Integer.parseInt(token[0]);
            long target = -1;
            if (token.length == 2) {
                target = Long.parseLong(token[1]);
            }
            
            switch(command) {
                case 1:
                    sum += target;
                    xor ^= target;
                    break;
                case 2:
                    // 이미 xor 값은 제거하고자 하는 값과 xor 연산이 되어 있으므로 다시 target과 xor 연산 -> 그 값 비트를 0으로 만들기 
                    sum -= target;
                    xor ^= target;
                    break;
                case 3:
                    System.out.println(sum);
                    break;
                case 4:
                    System.out.println(xor);
                    break;
            }
        }  

        sc.close();
    }
}