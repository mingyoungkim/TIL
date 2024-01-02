# Object 클래스
 - 모든 클래스의 최상위 클래스
 - 아무것도 상속받지 않으면 자동으로 상속받는 클래스
 - Object가 가지고 있는 메서드는 모든 클래스에서 사용 가능

 ## 메서드
 > 사용시 반드시 오버라이딩
   1. equals
     - 객체가 가지고 있는 값 비교
   2. toString
     - 객체가 가지고 있는 값을 문자열로 반환
   3. hashCode
     - 객체의 hashCode를 구하는 메서드
     - 자료구조에서 많이 사용
     - 

  ```java
    public class Student {
      String name;
      String number;
      int age;

      public static void main(String[] args) {
        Student s1 = new Student();
        s1.name = "홍길동";
        sl.number = "1234";
        sl.age = 20;

        Student s2 = new Student();
        s2.name = "홍길동";
        s2.number = "1234";
        s2.age = 20;

        if (s1.equals(s2)) System.out.println("같음");
        else System.out.println("다름");

        System.out.println("s1 hashCode == " + sl.hashCode());
        System.out.println("s2 hashCode == " + s2.hashCode()));

        System.out.println("s1 == " + s1);
        System.out.println("s1 toString() == " + s1.toString());
      }
    }
  ```
