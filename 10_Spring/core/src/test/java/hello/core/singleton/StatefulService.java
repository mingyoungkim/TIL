package hello.core.singleton;

public class StatefulService {
    private int price; // 상태를 유지하는 필드

    public void order(String name, int price) {
        System.out.println("name == " + name + " price == " + price);
        // intelliJ 중간에서 다음줄 넘기기 단축키 : shift + command + enter
        this.price = price; // 여기가 문제 !!
    }

    public int getPrice() {
        return price;
    }
}
