import java.util.*;

public class Main {
    private static int convertStringToSecond(String time) {
        String[] times = time.split(":");

        return Integer.parseInt(times[0]) * 60 + Integer.parseInt(times[1]);
    }

    private static String convertSecondToString(int totalTime) {
        int min = totalTime / 60;
        int sec = totalTime % 60;

        String strTime = String.format("%02d:%02d", min, sec);
        return strTime;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int goalCount = sc.nextInt();
        sc.nextLine(); // clear buffer

        int team1 = 0;
        int team2 = 0;
        int totalTime1 = 0;
        int totalTime2 = 0;
        int prevTime = 0;
        int totalGameTime = 48 * 60;

        for (int i = 0; i < goalCount; i++) {
            String line = sc.nextLine();
            String[] tokens = line.split(" ");
            int team = Integer.parseInt(tokens[0]);
            int currentTime = convertStringToSecond(tokens[1]);

            // debug
            // System.out.println(team);

            // 득점 전까지 누가 이겼는지
            if (team1 > team2) {
                totalTime1 += currentTime - prevTime;
            } else if (team2 > team1) {
                totalTime2 += currentTime - prevTime;
            }

            if (team == 1) {
                team1++;
            } else if (team == 2) {
                team2++;
            }

            prevTime = currentTime;
        }

        // 경기 종료 시각까지 마지막 리드팀 시간 추가
        if (team1 > team2) {
            totalTime1 += totalGameTime - prevTime;
        } else if (team2 > team1) {
            totalTime2 += totalGameTime - prevTime;
        }

        System.out.println(convertSecondToString(totalTime1));
        System.out.println(convertSecondToString(totalTime2));

        sc.close();
    }
}
