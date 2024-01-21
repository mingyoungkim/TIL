package hello.hellospring.apo;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect // 해당 어노테이션으로 AOP로 인식해서 사용가능
@Component
public class TimeTraceAop {
    // 공통관심사항을 타게팅하기
    @Around("execution(* hello.hellospring..*(..))")
    public Object execute(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        // 어떤 메서드 수행한지 알 수 있는 함수
        System.out.println("Strat : " + joinPoint.toString());
        try {
            // 다음 메서드로 진행
            return joinPoint.proceed();
        }
        finally {
            long finish = System.currentTimeMillis();
            long timeMs = start - finish;
            System.out.println("AOP reulst == " + timeMs + "ms");
        }
    }
}
