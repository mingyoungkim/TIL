package hello.core.order;

import hello.core.discount.DiscountPolicy;
import hello.core.discount.FixDiscountPolicy;
import hello.core.discount.RateDiscountPolicy;
import hello.core.member.Member;
import hello.core.member.MemberRepository;
import hello.core.member.MemoryMemberRepository;

public class OrderServiceImpl implements OrderService {
    /*
     * 현재, DIP 및 OCP 원칙을 위반 (할인정책을 변경하기 위해, 소스코드 수정 필요)
     * So, 구현체에 의존하지 않고 인터페이스만 의존하도록 수정
     * => 근데? discountPolicy는 null 이므로 discountPolicy.disount() NPE(Null Point Exception) 발생
     * [해결방안] 생성자 주입 방식으로 해결
     */
    /*
    // final 은 무조건 값이 할당되어야함 (기본으로 할당을하든, 생성자를 통해 할당을하든)
    private final MemberRepository memberRepository = new MemoryMemberRepository();
    //private final DiscountPolicy discountPolicy = new FixDiscountPolicy();
    //private final DiscountPolicy discountPolicy = new RateDiscountPolicy();
    private DiscountPolicy discountPolicy;
    */
    
    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;

    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member = memberRepository.findById(memberId);
        int discountPrice = discountPolicy.discount(member, itemPrice);

        return new Order(memberId, itemName, itemPrice, discountPrice);
    }
}
