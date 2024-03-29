package hello.core.discount;

import hello.core.member.Grade;
import hello.core.member.Member;

// 정액할인정책
public class FixDiscountPolicy implements DiscountPolicy {
    private int discountFixAmount = 1000; // 1000원 할인

    @Override
    public int discount(Member member, int price) {
        // eNum type은 == 사용
        if (member.getGrade() == Grade.VIP) {
            return discountFixAmount;
        }
        return 0;
    }
}
