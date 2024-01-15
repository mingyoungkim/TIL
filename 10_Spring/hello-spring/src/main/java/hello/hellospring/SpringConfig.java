package hello.hellospring;

import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import hello.hellospring.service.MemberService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * 스프링 빈 직접 등록하기
 */
@Configuration
public class SpringConfig {

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        // memberRepository 는 인터페이스 , MemoryMemberRepository 가 구현체
        // 인터페이스는 new 안됨
        return new MemoryMemberRepository();
    }
}
