import java.util.*;

public class Main {
    public static class BNP {
        int money;
        int stockPrice[];
        int stockCount;

        public BNP(int money, int stockPrice[]) {
            this.money = money;
            this.stockPrice = stockPrice;
            this.stockCount = 0;
        }

        public void getStockCount() {
            for (int price : stockPrice) {
                if (money >= price) {
                    while (money >= price) {
                        money -= price;
                        stockCount++;
                    }
                }
            }
        }

        public int getTotalMoney() {
            getStockCount();
            return money + (stockPrice[stockPrice.length - 1] * stockCount);
        }
    }

    public static class Timing {
        int money;
        int stockPrice[];
        int stockCount;

        public Timing(int money, int stockPrice[]) {
            this.money = money;
            this.stockPrice = stockPrice;
            this.stockCount = 0;
        }

        public void getStockCount() {
            for (int i = 3; i < 14; i++) {
                // 3일 연속 상승
                if (stockPrice[i - 3] < stockPrice[i - 2] && stockPrice[i - 2] < stockPrice[i - 1] ) {
                    money += stockCount * stockPrice[i];
                    stockCount = 0;
                }
                // 3일 연속 하락
                else if (stockPrice[i - 3] > stockPrice[i - 2] && stockPrice[i - 2] > stockPrice[i - 1]) {
                    // 전량 매수
                    while (money >= stockPrice[i]) {
                        money -= stockPrice[i];
                        stockCount++;
                    }
                }
            }
        }

        public int getTotalMoney() {
            getStockCount();
            return money + (stockPrice[stockPrice.length - 1] * stockCount);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int money = sc.nextInt();
        int stockPrice[] = new int[14];

        for (int i = 0; i < 14; i++) {
            stockPrice[i] = sc.nextInt();
        }

        BNP bnp = new BNP(money, stockPrice);
        Timing timing = new Timing(money, stockPrice);

//        System.out.println("BNP: " + bnp.getTotalMoney());
//        System.out.println("Timing: " + timing.getTotalMoney());

        if (bnp.getTotalMoney() > timing.getTotalMoney()) {
            System.out.println("BNP");
        } else if (timing.getTotalMoney() > bnp.getTotalMoney()) {
            System.out.println("TIMING");
        } else {
            System.out.println("SAMESAME");
        }

        sc.close();
    }
}