package hello.core.beanFind;

import hello.core.AppConfig;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

class ApplicationContextInfoTest {
    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("모든 빈 출력하기")
    // Junit5 이상부터는 public 기재 안해줘도 됨
    void findAllBean() {
        // Bean으로 정의된 이름을 다 등록
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();
        // list 같은 배열이 있는경우, iter : for 문 자동완성 단축키
        for (String beanDefinitionName : beanDefinitionNames) {
            // option + command + V : 변수 자동완성 단축키
            Object bean = ac.getBean(beanDefinitionName); // 현재 type 을 지정안해서 object로 꺼내짐
            System.out.println("name = " + beanDefinitionName + " object = " + bean);
        }
    }

    // 드래그한 부분 자동 복붙 단축키 : command + D
    @Test
    @DisplayName("애플리케이션 빈 출력하기")
    void findApplicationBean() {
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();
        for (String beanDefinitionName : beanDefinitionNames) {
            // getBeanDefinition : Bean 하나하나에 대한 메타데이터 정보
            BeanDefinition beanDefinition = ac.getBeanDefinition(beanDefinitionName);

            // BeanDefinition.ROLE_APPLICATION : spring이 내부에서 알아서 등록한 빈들이 아니라, 내가 등록한 빈
                // findAllBean 해서 나오는 빈들 중, SpringFramework Factory같은 빈 제외
            // ROLE_APPLICATION : 직접 내가 개발하면서 등록한 빈
            // ROLE_INFRASTRUCTURE : 스프링이 내부에서 사용하는 빈
            if (beanDefinition.getRole() == BeanDefinition.ROLE_APPLICATION) {
                Object bean = ac.getBean(beanDefinitionName);
                System.out.println("name = " + beanDefinitionName + " object = " + bean);
            }
        }
    }
}
