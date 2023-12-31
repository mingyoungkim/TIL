# JAVA 생성자

 ## 생성자 특징
 > 객체가 될때 필드를 초기화하는 역할
   - 리턴타입 존재 X
   - 생성자를 만들지 않으면 매개변수가 없는 생성자가 compile할때 자동으로 만들어짐
   - 기본 생성자 : 매개변수가 없는 생성자
 ![Java_생성자](Java.assets/java_constructor.png)
  ```java
  // Car Class
    public class Car {
      String name;
      int number;

    // Car 객체가 만들어질때 반드시 이름을 가지고 만들고 싶다면 하기 생성자로 가능
    // 즉, 매개변수가 있는 생성자
    public Car(String name) {
      /* this
        객체 자신을 참조 (객체 자신의 field를 바라봄)
        class 안에서 자기 자신이 가지고 있는 속성/메서드/생성자 등을 의미
      */
      this.name = name;
    }

  // CarExam Class
    public class CarExam {
      Car c1 = new Car(); // 기본 생성자 -> 사용불가!
      Car c2 = new Car("붕붕이");
    }
  }
 ```

 ## 오버로딩
  ### 메서드 오버로딩
  > 매개변수의 갯수나 타입이 다르지만 비슷한 기능을 하는 
   메서드가 여러개 일때 동일한 이름으로 메서드 여러개 정의 가능 
   - `매개변수의 타입이나 수`가 달라야 가능
  ![method_overLoading](Java.assets/java_method.png)
  
  ### 생성자 오버로딩
  > 메서드와 마찬가지로 매개변수의 수와 타입이 다르다면 동일 이름의 생성자 여러개 선언 가능


 ## 패키지
 > class 관리를 위해 사용
   - 관련된 class들을 폴더별로 관리
   - 도메인 붙여서 사용 
      => 다른 프로젝트, 회사에서 만든 파일명과 중복되지 않기 위해
   - 폴더명은 숫자로 시작 불가!
   - `import` : java의 lang 패키지를 제외하고 모든 패키지는 import 기재
     > 다른 패키지의 class를 사용하기 위한 키워드
 ![java_pacakage](Java.assets/java_package.png)

# 상속
 - public class 클래스명 extends 부모클래스명 {}
 - 부모클래스가 가지고 있는 것을 자식이 물려받을 수 있음 (사용가능)

 ```java
 // 부모클래스
  public class Car {
    public void run() {
      System.out.println("Car 클래스 상속 완")
    }
  }
 // 자식클래스
  public class Bus extends Car {
    /* 확장하였다.
      : 부모가 가지고 있는 메서드 이외에도
        추가로 메서드를 선언하는 것.
    */
    public void stop() {
      System.out.println("멈춰라 차들아")
    }
  }
 // Bus 클래스 확인하고자 만든 클래스
  public class BusExam {
    public static void main(Strig[] args) {
      Bus bus = new Bus();
      /* 
        Bus 클래스는 run 메서드 없었지만
        Car 클래스를 상속받으면서 부모클래스인 Car의 메서드 사용 가능
      */
      bus.run();
      bus.stop(); // 당연히 bus 내 메서드 사용 O

      Car car = new Car();
      car.run();
      car.stop(); // 당연히 부모클래스는 자식 클래스 사용 불가!!
    }
  }
 ```

 ## 접근제한자
   1. publc
     - 어떤 클래스든 접근 가능 (모든 접근을 허용)
     - 가장 넓은 의미
   2. protected
     - 같은 패키지인 경우 접근 허용
     - 다른 패키지라도 상속받은 경우는 허용
   3. private
     - 자기 자신만 허용
   4. default 접근지정자
     - 아무것도 쓰지 않은 경우, 자기 자신과 같은 패키지 내에서 접근 허용 
   - 접근 범위 : public > protected > default > private

  ```java
    public class AccessObj {
      public int test1 = 10;
      protected int test2 = 20;
      private int test3 = 30;
      int test4 = 40; // default 접근지정자
    }
    // 1. 동일 패키지 내
    public class AccesExam {
      public static void main(Stirng[] arsg) {
        AccessObj obj = new AccessObj();
        System.out.println(obj.test1);
        System.out.println(obj.test2);
        System.out.println(obj.test3); // 같은 패키지라도 private는 접근 불가
        System.out.println(obj.test4);
        /* 2.
          만약 다른 패키지라면, public 제외 다 접근 불가
        */
      }
    }
    // 3. 다른 패키지 내 상속 받는 경우
    public class AccessObjExam extends AccessObj {
      public static void main(Stirng[] arsg) {
        AccessObjExam obj = new AccessObjExam();
        System.out.println(obj.test1);
        System.out.println(obj.test2);
        System.out.println(obj.test3); // 접근불가
        System.out.println(obj.test4); // 접근불가
      }
    }
  ```

  ## 추상클래스
  > 모호한 개념을 가진 클래스는 부모로써 역할은 수행가능 but, 객체가 될 수는 없음
   - 추상메서드를 가진 클래스는 추상 클래스가 된다
   - 추상클래스 내, 일반 메서드도 구현 가능

  ```java
    public abstract class Bird {
      public abstract void sing();
      
      public void fly() {
        System.out.println("날다");
      }
    }
  
    public class Duck extends Bird {
      // Bird가 가지고 있었던 추상메서드에 대한 구현이 필요!
      @Override
      public void sing() {
        System.out.println("오리는 꽥");
      }
    }
    public class DuckExam {
      public static void main(String[] args) {
        Duck duck = new Duck();
        duck.sing();
        duck.fly(); // 부모클래스 메서드도 사용가능

        Bird bird = new Bird() // 오류발생!!! -> 추상클래스는 부모로써 역할은 가능하지만 추상클래스를 이용해서 객체생성 불가 !!!
      }
    }
  ```
