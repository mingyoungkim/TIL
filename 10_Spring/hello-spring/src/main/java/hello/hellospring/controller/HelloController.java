package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {
    // "~/hello" 진입 시, 해당 메서드 호출
    @GetMapping("hello")
    public String Hello(Model model) {
        model.addAttribute("data", "hello~!!!");
        return "hello";
    }

    @GetMapping("hello-mvc")
    // @RequestParam : 외부에서 파라미터 전달 받음
    // 옵션 : required(필수인지 기재 -> default : true)
    public String helloMvc(@RequestParam(value = "name", required = true) String name, Model model) {
        model.addAttribute("name", name);
        return "hello-template";
    }

    @GetMapping("hello-string")
    @ResponseBody // http에서 응답 headr와 body중, body부에 return 되는 데이터를 직접 넣어주겠다는 의미
    public String helloString(@RequestParam("name") String name) {
        return "hello " + name; // 템플릿엔진과의 차이 : view가 없음 (문자 그대로 내려감)
    }

    @GetMapping("hello-api")
    @ResponseBody
    // hello라는 객체 만들기
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello; // json으로 리턴됨
    }

    static class Hello {
        private String name;

        // 단축키 : control+n
        /* getter, setter
          - java bean 규약
          - property 접근방식
        */
        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
}
