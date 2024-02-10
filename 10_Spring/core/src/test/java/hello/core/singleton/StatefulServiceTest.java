package hello.core.singleton;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;

import static org.junit.jupiter.api.Assertions.*;

class StatefulServiceTest {
    @Test
    void statefulServiceSingleton() {
        ApplicationContext ac = new AnnotationConfigApplicationContext(TestConfig.class);
        StatefulService statefulService1 = ac.getBean(StatefulService.class);
        StatefulService statefulService2 = ac.getBean(StatefulService.class);

        // ThreadA : A 사용자가 10000원 주문
        statefulService1.order("userA", 10000);
        // ThreadB : B 사용자가 20000원 주문
        statefulService2.order("userB", 20000);
        // ThreadA : A 사용자가 주문 금액 조회
        int price1 = statefulService1.getPrice();
        /* 결과
         20000원임.... Why????? 중간에 사용자B 가 price 바꿔버림
         service1이든 2든, 싱글톤 패턴으로 같은 인스턴스를 사용하고 있기 때문
         */
        System.out.println("price1 == " + price1);
        Assertions.assertThat(statefulService1.getPrice()).isEqualTo(20000);
    }

    static class TestConfig {
        @Bean
        public StatefulService statefulService() {
            return new StatefulService();
        }
    }

}