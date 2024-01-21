package hello.hellospring;

import hello.hellospring.apo.TimeTraceAop;
import hello.hellospring.repository.*;
import hello.hellospring.service.MemberService;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.sql.DataSource;
import javax.xml.crypto.Data;

/**
 * 스프링 빈 직접 등록하기
 */
@Configuration
public class SpringConfig {
    /*
    private DataSource dataSource;
    @Autowired
    public SpringConfig(DataSource dataSource) {
        this.dataSource = dataSource;
    }
     */

    /*
    @PersistenceContext
    private EntityManager em;

    @Autowired
    public SpringConfig(EntityManager em) {
        this.em = em;
    }

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        // memberRepository 는 인터페이스 , MemoryMemberRepository 가 구현체
        // 인터페이스는 new 안됨
        // return new MemoryMemberRepository(); 가능!
        // return new JdbcMemberRepository(dataSource);
        // return new JdbcTemplateMemberRepository(dataSource);
         return new JpaMemberRepository(em);
    }
    */

    private final MemberRepository memberRepository;

    public SpringConfig(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    // JpaRepository extends 하는 interface만 있으면, spring-data-jpa가 인터페이스에 대한 구현체를 자동으로 만들어냄
    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository);
    }

    /*
    // AOP같은 경우, @Component로 등록하기 보다는
    // config에 등록해서 사용하는 것이 명시하기 좋다.
    @Bean
    public TimeTraceAop timeTraceAop() {return new TimeTraceAop();}
    */
}
