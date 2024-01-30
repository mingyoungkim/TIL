package hello.core;


import hello.core.discount.DiscountPolicy;
import hello.core.discount.FixDiscountPolicy;
import hello.core.discount.RateDiscountPolicy;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import hello.core.member.MemoryMemberRepository;
import hello.core.order.OrderService;
import hello.core.order.OrderServiceImpl;

public class AppConfig {

    // 생성자 주입 (생성자를 통해서 객체가 생성된 것을 주입)
    // 구현체에 의존하지 않고 인터페이스에만 의존하도록 하기 위함
    /*
    public MemberService memberService() {
        return new MemberServiceImpl(new MemoryMemberRepository());
    }

    public OrderService orderService() {
        return new OrderServiceImpl(new MemoryMemberRepository(), new FixDiscountPolicy());
    }
    */

    // 역할과 구현 클래스 분리
    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }

    private static MemoryMemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }

    public OrderService orderService() {
        return new OrderServiceImpl(memberRepository(), discountPolicy());
    }

    private static DiscountPolicy discountPolicy() {
        // 할인정책이 변경되면 이제, AppConfig에 해당 부분만 바꾸면됨
//        return new FixDiscountPolicy();
        return new RateDiscountPolicy();
    }
}
