package hello.core.beanFind;

import hello.core.AppConfig;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.NoSuchBeanDefinitionException;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import static org.assertj.core.api.Assertions.*;

class AppllicationContextBasicFindTest {

    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("빈 이름으로 조회")
    void findBeanByname() {
        MemberService memberService = ac.getBean("memberService", MemberService.class);
        System.out.println("memberService == " + memberService);
        System.out.println("memberService.getClass == " + memberService.getClass());
        // isInstanceOf() : 해당 인스턴스 객체인지 확인
        //Assertions.assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
        // option+enter (Assertions 축약)
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("이름없이 타입으로만 조회")
    void findBeanByType() {
        MemberService memberService = ac.getBean(MemberService.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("구체타입으로 조회")
    void findBeanByType2() {
        // interface인 MemeberService가 아닌 Impl로 조회
        // => 좋은 코드는 아님 (역할과 구현을 구분해야함... 역할에 의존해야함... 이 코드는 구현에 의존)
        MemberServiceImpl memberService = ac.getBean("memberService", MemberServiceImpl.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("빈 이름으로 조회 실패")
    void findBeanByNameX() {
        //ac.getBean("xxxx", MemberService.class);
        //MemberService xxxx = ac.getBean("xxxx", MemberService.class);
        // java8 lamda
        // () 이후 로직을 실행 시, 해당 에러터지면 예외가 던저져야함
        org.junit.jupiter.api.Assertions.assertThrows(NoSuchBeanDefinitionException.class,
                () -> ac.getBean("xxxx", MemberService.class));
    }
}
