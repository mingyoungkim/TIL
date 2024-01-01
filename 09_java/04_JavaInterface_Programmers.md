# 인터페이스
 > 클래스의 꼭 필요한 기능들을 구현은 하지 않고 선언만해서 가지고 있는 것
  즉, 객체를 선언하기 전에 해당 객체의 기능들을 모아둔 것

 ```java
    public interface TV {
      // 인터페이스에 정의한 변수는 상수 (변경 불가)
      public int MIN_VOLUMN = 0;
      public int MAX_VOLUMN = 100;

      public void turnOn();
      public void turnOff();
      public void changeVolumn(int volumn);
      public void changeChannel(int channel);
    }

    /* implements
      interface TV를 구현하겠다.
      martTv말고 interface 기능을 구현하는 다른 클래스(ex. LedTv)로 TV 메서드 구현 가능
    */
    public class SmartTv implements TV {
      @Override
      public void turnOn() {
        System.out.println("스마트 tv를 키다.");
      }
      @Override
      public void turnOff() {
        System.out.println("스마트 tv를 끄다.");
      }
      @Override
      public void changeVolumn(int volumn) {
        System.out.println("볼륨 조절");
      }
      @Override
      public void changeChannel(int channel) {
        System.out.println("채널 변경");
      }
    }

    public class SmartExam {
      public static void main(String[] args) {
        // interface도 타입이 될 수 있다. -> 이 경우, 인터페이스가 가지고 있는 메서드만 사용 가능
        TV tv = new SmartTv();
        tv.turnOn();
        tv.changeVolumn(20);
        tv.changeChannel(3);
        tv.turnOff();
      }
    }
 ```

 ## default method & static method
 - java8 이전 : 추상메서드만 정의 가능
 - java8 이후 : default, static 메서드 정의 가능
 - 인터페이스가 변경이 되면, 그 인터페이스 구현하고 있는 모든 클래스들이 해당 메서드 구현해야함.
   so, 이 문제를 해결하기 위해 인터페이스 내에 메서드를 구현할 수 있도록 추가됨

 ```java
    public interface Caculator {
      public int plus(int num1, int num2);
      public int multiple(int num1, int num2);

      /* 인터페이스 내에 기능 열거 + 구현 가능한 메서드 */
      // 1. default method
      default int exec(int num1, int num2) {
        return num1 + num2;
      }
      // 2. static method
      public static int exec2(int num1, int num2) {
        return num1 * num2;
      }
    }

    public class MyMath implements Caculator {
      @Override
      public int plus(int num1, int num2) {
        return num1 + num2;
      }
      @Override
      public int multiple(int num1, int num2) {
        return num1 * num2;
      }
    }

    public class MyMathExam {
      public static void main(String[] args) {
        Calculator cal = new MyMath();
        int test1 = cal.plus(1, 2);
        int test2 = cal.exec(3, 4);

        // interface에 정의한 static 메서드는 무조건 interface.메서드명 으로 호출 가능
        Calculator.exec2(5, 6);
      }
    }
 ```

 ## 내부클래스
 > 클래스 내부에 선언된 클래스
 1. 중첩클래스 == 인스턴스클래스(instance class)
 2. 정적 중첩클래스 == 스태틱클래스(static class)
 3. 지역 중첩클래스 == 지역클래스(local class)
   - 내부 클래스가 인스턴스 변수로 선언되는 것이 아니라, 메서드 안에서 선언되는 경우
   - 해당 클래스는 `선언된 메서드 안에서만` 사용가능
 4. 익명클래스 == 익명 중첩클래스

  ```java
    public class InnerExam {
      /****** 중첩클래스 ******/
      class Cal {
        int value = 0;
        public void plus() {
          value ++;
        }
      }
      /****** 정적 중첩클래스 ******/
      // 정적인 field와 같음
      static class Cal2 {
        int value = 0;
        public void minus() {
          value --;
        }
      }
      /****** 지역 중첩클래스 ******/
      public void exec() {
        class Cal3 {
          int value = 0;
          public void multiple() {
            value * 2;
          }
        }
        Cal3 cal = new Cal3();
        cal.multiple();
      }

      public static void main(String[] args) {
        /****** 중첩클래스 ******/
        // 중첩 클래스 사용하기 위해 먼저, 외부 클래스 먼저 생성되어야 함
        InnerExam test = new InnerExam();
        InnerExam.Cal cal = test.new Cal();
        cal.plus();

        /****** 정적 중첩클래스 ******/
        InnerExam.Cal2 cal2 = new InnerExam.Cal2();
        cal2.minus();

        /****** 지역 중첩클래스 ******/
        test.exec();\
      }
    }
  ```
  ```java
  /****** 익명 중첩클래스 ******/
  public abstract class Action {
    public abstract void doAction();
  }

  public class MyAction extends Action {
    @Override
    public void doAction() {
      System.out.println("얍");
    }
  }

  public class ActionExam {
    public static void main(String[] args) {
      //Action action = new MyAction();
      //action.doAction();

      /* 익명클래스
        상속받는 클래스를 굳이 만들어낼 필요가 없는 경우 사용 (ActionExam 클래스에서만 사용)
        즉, 이름없는 객체를 만듦
      */
      Action action = new Action() {
        @Override
        public void doAction() {
          System.out.println("익명클래스다잉")
        }
      }
      action.doAction();
    }
  }
  ```
  

