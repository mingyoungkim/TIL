package hello.core;

import hello.core.AppConfig;
import hello.core.member.Grade;
import hello.core.member.Member;
import hello.core.member.MemberService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.util.Arrays;

public class MemberApp {
    /*
    public static void main(String[] args) {
        MemberService memberService = new MemberServiceImpl();
        Member member = new Member(1L, "memberA", Grade.VIP);
        memberService.join(member);

        Member findMember = memberService.findMember(1L);
        System.out.println("member = " + member.getName());
        System.out.println("finde Member = " + findMember.getName());
    }
    */

    public static void main(String[] args) {
//        AppConfig appConfig = new AppConfig();
//        MemberService memberService = appConfig.memberService();

        /* ApplicationContext : spring Container 라고 생각하면됨 (모든 객체들, Bean들을 관리함) */
        /* AnnotationConfigApplicationContext : Annotation 기반으로 Config 하고 있는 AppConfig */
        // AppConfig 에 있는 환경 설정정보를 가지고 spring 이 Bean으로 잡힌애들을 spring container에 객체 생성한 것을 집어 넣어서 관리
        ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class);
        MemberService memberService = applicationContext.getBean("memberService", MemberService.class);

        Member member = new Member(1L, "memberA", Grade.VIP);
        memberService.join(member);

        Member findMember = memberService.findMember(1L);
        System.out.println("member = " + member.getName());
        System.out.println("finde Member = " + findMember.getName());
    }
}
