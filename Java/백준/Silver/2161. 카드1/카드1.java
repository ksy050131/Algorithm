import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> queue = new LinkedList<>();

        int n = sc.nextInt();
        for (int i = 1; i <= n; i++) {
            queue.offer(i);
        }

        while (queue.size() > 1) {
            System.out.printf("%d ", queue.poll());
            queue.offer(queue.poll());
        }

        System.out.println(queue.poll()); // 마지막 남은 카드 출력
    }
}