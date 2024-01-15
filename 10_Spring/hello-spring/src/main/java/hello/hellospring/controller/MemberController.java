package hello.hellospring.controller;

import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

/** @Controller
 * spring 컨테이너가 뜰 때, controller 어노테이션이 있으면
 * memberController 객체를 생성해서 스프링이 관리를 함
 * == Spring Bean이 관리된다.
 */
@Controller
public class MemberController {
    //public final MemberService memberService = new MemberService();
    public final MemberService memberService;

    /* 필드 주입 */
    //@Autowired public MemberService memberService;

    /** @AutoWired
     * member 서비스를 스프링이 가져다 줌 (의존성 주입)
     */
    @Autowired
    /* 생성자 주입 (생성자를 통해서 memberService가 memberController에 주입) */
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    /* setter 주입 */
    /*
    @Autowired
    public void setMemberService(MemberService memberService) {
        this.memberService = memberService;
    }
    */
}
