import java.util.*;
import java.lang.*;
import java.io.*;

// 2. 알파벳 읽어와서 움직이는 move method 만들기 (return new location)
// 3. 킹 먼저 움직이고 돌 계산해서 움직이기

// The main method must be in a class named "Main".
class Main {
    static class Point {
        int row;
        int col;
        
        public Point(int row, int col) {
            this.row = row;
            this.col = col;
        }

        public Point copy() {
            return new Point(this.row, this.col);
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String kingPos = sc.next();
        String ballPos = sc.next();
        int moveCnt = sc.nextInt();
        sc.nextLine(); // clean buffer

        Point king = readLocation(kingPos);
        Point ball = readLocation(ballPos);

        for (int i = 0; i < moveCnt; i++) {
            String moveDir = sc.nextLine();

            // king 먼저 움직이기 근데 혹시 모르니까 이전 king 놔두기
            Point beforeKing = king.copy();
            
            king = move(king, moveDir);

            // king 움직인 곳에 ball 있으면 같은 방향으로 이동
            if (king.row == ball.row && king.col == ball.col) {
                ball = move(ball, moveDir);
            }

            if (king.row == ball.row && king.col == ball.col) {
                // 또 같으므로 롤백
                king = beforeKing.copy();
            }
            
        }

        System.out.println(returnLocation(king));
        System.out.println(returnLocation(ball));
    }

    public static Point readLocation(String location) {
        int row = location.charAt(1) - '0' - 1; // row
        int col = location.charAt(0) - 'A'; // col
        
        return new Point(row, col);
    }

    public static String returnLocation(Point current) {
        String back = String.valueOf(current.row + 1);
        String front = String.valueOf((char)(current.col + 'A'));

        return front + back;
    }

    public static Point move(Point current, String direct) {
        Point moved = current.copy();
        
        switch (direct) {
            case "R":
                moved.col++;
                break;
            case "L":
                moved.col--;
                break;
            case "B":
                moved.row--;
                break;
            case "T":
                moved.row++;
                break;
            case "RT":
                moved.row++;
                moved.col++;
                break;
            case "LT":
                moved.row++;
                moved.col--;
                break;
            case "RB":
                moved.row--;
                moved.col++;
                break;
            case "LB":
                moved.row--;
                moved.col--;
                break;
        }
        
        if ((moved.row < 0 || moved.row > 7) || (moved.col < 0 || moved.col > 7)) {
            // 범위 벗어나면 롤백
            return current;
        }
        return moved;
    }
}