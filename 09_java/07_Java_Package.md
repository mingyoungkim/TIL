# java.lang 패키지
 ## wrapper
 > 기본형 데이터 타입을 객체화 되도록 도와주는 클래스들
 ```java
   public class WrapperClass {
    public static void main(Stirng[] args) {
      int exNum = 5; // 기본형 타입 (객체X, 즉 참조형이 아님)
      Integer exNum2 = new Integer(5); // 실제 int를 객체로 바꿔주는 Integer라는 클래스

      Integer exNum3 = 5; // 기본데이터타입 5를 넣어도 문제 없음 (숫자 5는 기본형이지만 자동으로 Integer로 형변환됨 == AutoBoxing)

      int exNum4 = exNum3.intValue() // 객체로 감싸져있던 exNum을 int타입으로 사용 (과거)
      int exNum5 = exNum3; // java5 이후 AutoUnboxing (객체타입을 데이터를 기본형 데이터 타입으로 변환)
    } 
   }
 ```

 ## Object

 ## String, StringBuilder, StringBuffer
   ### StringBuffer
   ```java
     public class StringBufferExam {
      public static void main(String[] args) {
        StringBuffer sb = new StringBuffer();
        sb.append("Hello");
        sb.append(" ");
        sb.append("World");

        String str = sb.toString();

        StringBuffer sb2 = new StringBuffer();
        StringBuffer sb3 = sb2.append("hi");
        /* 메서드 체이닝
          자기자신을 리턴하여 계속해서 자신의 메서드를 호출하는 방식
        */
        if (sb2 == sb3) {
          System.out.println(sb2 + "||||" + sb3)
        }

        String str2 = new StringBuffer().append("Hello").append(" ").append("World").toString();
      }
     }
   ```

   ### 스트링 클래스의 문제점 
   ```java
     public class StringExam {
      public static void main(String[] args) {
        String str1 = "hello world";
        String str2 = str1.substring(5);
        String str3 = str1 + str2;
        String str4 = new StringBuffer().append(str1).append(str2).toString(); // str3의 "+ 연산자"의 프로세스와 같음

        // 나쁜 예시
        // for문 돌면서 100번 동안 String 객체를 만들어냄 (new 연산자를 많이 만들어낼 수록 속도 느려짐)
        String str5 = "";
        for (int i=0; i<100; i++) {
          str5 = str5 + "*";
        }
        // 좋은 예시
        // String을 직접 연산하게 하는 대신 StringBuffer에 append하여 만드는 것이 좋음
        StringBuffer sb = new StringBuffer();
        for (int i=0; i<100; i++) {
          sb.append("*");
        }
        String str6 = sb.toStirng();
      }
     }
   ```

 ## System
 ## Math
 > 수학 계산을 위한 클래스 (cos, sin, tan, abs, random)
   - 생성자 자체가 private로 되어 있어서 new연산자로 객체 생성 불가
   - 모든 메서드와 속성이 static으로 정의되어 았어 객체로 생성안해도 사용 가능
  ```java
     public class MathExam {
      public static void main(String[] args) {
        int value1 = Math.max(5, 30);
        int value2 = Math.min(6, 29);
        int value3 = Math.abs(-10);
        double value4 = Math.random(); // 0~1 사이 랜덤값
        double value5 = Math.sqrt(25); // 25의 제곱근
        double value6 = Math.pow(5, 2) // 5의 제곱
      }
     }
  ```

# java.util 패키지