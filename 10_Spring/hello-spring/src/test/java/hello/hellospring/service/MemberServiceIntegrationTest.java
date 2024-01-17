package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import static org.junit.jupiter.api.Assertions.assertThrows;

// 순수java코드로 테스트하는 것이 아닌, spring이 가지고 있는 test
// 스프링 컨테이너와 테스트를 함께 실행 (진짜 spring을 띄워서 test)
@SpringBootTest
/** @Transactional
 * database는 transaction 이라는 개념..!
 * so, commit을 해야 db에 반영
 * db에 insert 후, rollback을 하면 db에 반영은 안됨 (그러면 clear 필요 X)
 * -> 이 프로세스로 테스트하는 어노테이션
 */
@Transactional
class MemberServiceIntegrationTest {
    // spring container 한테 memberService, memberRepository 내놔!
    @Autowired MemberService memberService;
    @Autowired MemberRepository memberRepository;

    @Test
    void join() {
        // given
        Member member = new Member();
        member.setName("hello");
        // when
        Long saveId = memberService.join(member);
        // then
        Member findMember = memberService.findOne(saveId).get();
        Assertions.assertThat(member.getName()).isEqualTo(findMember.getName());
    }

    @Test
    public void 중복_회원_예외() {
        // given
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        //when
        memberService.join(member1);
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));
        Assertions.assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
    }
}