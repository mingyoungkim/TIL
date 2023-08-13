# JAVA Class

 ## 객체지향언어
   > 프로그램을 구성하는 요소는 객체이며, 이것이 상호작용하도록 프로그래밍
   - Java는 객체를 만들기 위해 반드시 Class를 먼저 만들어야함
  ### Class
   > 객체를 만들기위한 틀
   ex. 붕어빵 : 객체, 붕어빵만들어내는 틀 : 클래스
   - 선언
  ```java
    public class 클래스명 { // 클래스 블록
      ... 
    }
  ```
   - class 파일 생성 후 저장 시, eclipse가 compile하여 car라는 class 생성
   - class를 이용해 객체를 만들 때, class가 모든 참조형 타입이 될 수 있다
  ```java
    public class CarExam {
      public static void main(String[] args) {
        Car c1 = new Car();
      }
    }
  ```
   - `new` 연산자 
   > class를 메모리에 올려주세요~!
     - new 뒤에 나오는 생성자를 이용해 메모리에 객체를 만들라는 명령어
     - `인스턴스` : 메모리에 만들어진 객체 
     - 만들어진 객체를 참조하는 객체 : `c1`
  
   - 참조형 타입
  ```java
    public class TypeClass {
      public static void main(String[] args) {
        // 정수 i라는 기본형 변수에 4 저장
        int basic = 4; 
        // String Class 
        /* str : 메모리에 올라간 instance를 가르키는 변수 (참조하는 변수, 레퍼런스하는 변수)
          즉, 변수가 instance를 가지고 있는 것이 아니라 말 그대로 가르킨다. (str에 메모리의 위치값 저장됨)
          str은 다른 메모리에 저장됨 */
        String str = new String("hello");
      }
    }
  ```
  ![java_class](Java.assets/java_class.png)

  ### String Class
   > java에서 가장 많이 사용되는 문자열을 표현하는 클래스
    - new 연산자 이용하지 않고도 인스턴스 생성가능 (이용해도 됨)
    - 한번 생성된 Class의 내부의 값은 변하지 않는다 
      (다른 class는 아님)
    - String이 가지고 있는 메서드들은 String 값 반환
      - 실행 후, 새로운 String을 만들어서 반환
  ```java
    public class StringClass {
      public static void main(String[] args) {
        // 1.
        // new연산자 사용 X
        // hello문자들이 상수가 저장되는 메모리 영역에 저장
        /* str1에서 hello가 상수영역에 변하지않는 값으로 저장되어
          str2는 똑같은 인스턴스 생성하지 않고 해당 인스턴스 참조 
          즉, str1과 str2는 같은 인스턴스를 참조함  */ 
        String str1 = "hello";
        String str2 = "hello"; 

        // 2. 
        // new연산자 사용
        /* 상수영역을 참조하지 않고 새로 인스턴스를 heap영역에 생성
          즉, str3과 str4는 heap영역에 각각 저장  */
        String str3 = new String("bye");
        String str4 = new String("bye");

        // 참조형은 값 비교X
        // == : 실제 변수가 가르키고 있는 메모리영역의 주소 비교
        // equals : 두 문자열이 같은지 비교하는 String Class Method
        if (str1 == str2) {
          System.out.println("같은 레퍼런스");
        }
        if (str2 == str3) {
          System.out.println("다른 레퍼런스");
        }
        if (str3 == str4) {
          System.out.println("다른 레퍼런스");
        }

        System.out.println(str1.substring(2));
        System.out.println(str1); // 위에서 값을 잘라도 str1 값은 변하지 않는다.
      }
    }
  ```
  
  ### Field