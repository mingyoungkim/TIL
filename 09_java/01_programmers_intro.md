# JAVA

 ## JAVA 특징
   - 플랫폼에 독립적 (JVM : java로 만들어진 프로그램을 실행해주는 프로그램)
   - 객체지향 프로그래밍
     - 재활용성
     - 직관성
   - Garbage Collector : 메모리 관리
  
 ## JAVA 개발 환경
   - JDK 설치 (Java Development Kit)
   - 환경변수 설정
     - JAVA_HOME
     - CLASSPATH
     - PATH
   - IDE 설치

 ## JAVA 개발 순서
   - 코드 작성 -> Compile -> JVM으로 실행
   `IDE없이 cmd로 compile : javac ~.java / 실행 : java ~`
   - Compiler
     - 작성한 코드를 실행가능한 코드로 변환하는 프로그램 (Language Code to Machine Code)


 ## 변수와 계산
  ### 변수
   - 값(data)을 저장할 수 있는 메모리 공간
   - type
     - 문자리터럴 : char
     - 실수리터럴 : float, double
     - 정수리터럴 : int, long, char, short, byte
     - 논리리터럴 : boolean
     `리터럴 : 특정한 값 자체`
   - 식별자 : 변수의 이름
   - 명명규칙 : 첫번째 문자 `소문자`, `camelCase`
  
  ### 상수
   - 변수처럼 값을 저장할 수 있는 메모리 공간
   - but, 한번 저장한 값은 변경 불가
   - `final` 
   - 명명 규칙 : `대문자`, `SNAKE_CASE`
   - 값의 변경이 크리티컬한 case에 사용

  ### 기본형의 타입변환
   - 묵시적 형변환 : 범위 작은 타입 -> 큰 타입 변환 가능
   - 강제(명시적) 형변환 : 큰 타입 -> 작은 타입
    ```java
      long x = 5L;
      int y = (int) x;
    ```
  ### 연산자와 연산식
   - 연산 : 데이터를 처리하여 결과를 산출하는 것
    `x = y + z` : 연산식
    => =, + : 연산자 (연산에 사용되는 표시나 기호) == Operations
    => y, z : 피연산자 (연산대상이 되는 데이터 리터럴,변수) == Operand
   - 연산자
     - 부호 연산자 : +, -
      `변수 앞에 부호연산자 붙는경우, + : 부호비트 유지 / - : 음수 및 양수 변환`
     - 산술 연산자 : +, -, /, %, *
     - 증감 연산자 : ++ , -- 
      `후위연산자 ++8 : 8+1 / 전위연산자 8++ : 값 먼저 변수에 대입 후, +1`
     - 비교 연산자 : ==, !=, <, >, <=, >= (결과값 : boolean)
     - 복합 대입 연산자 : +=, -=, *=, /=
     - 논리 연산자 : &&, ||, !, ^(exclusive or)
   - 연산자 우선순위
     ![java_operator](Java.assets/java_operator.png)
  
 ## 조건문
   - 수행하고자 하는 코드 제어
  ### If
   - if/ else if/ else
  
  ### 삼항 연산자
  ```java
    (x < y) ? true : false;
  ``` 
  ### Switch
   - switch/ case/ default/ break
   - case : 처음 만난 case부터 쫙 실행 => break로 컨트롤
   - default : else 와 같은 역할
  ```java
    int value = 1;

    switch (value) {
      case 1 :
        System.out.println("1입니다.");
        break; // 아래 case 실행X
      case 2 : case 3 :
        System.out.println("2보다 크거나 같고 4보다 작습니다.");
      case 4 :
        System.out.println("4입니다.");
      default :
        System.out.println("끝.");
    }
  ```

 ## 반복문
  ### while
   - 조건이 만족되지 않을 때 수행 X
  
  ### do while
   - 무조건 1번은 수행
   ```java
    int value = 0;
    // java.util 패키지 안에 만들어져있는 Class (~로부터 값을 입력받고 싶을때 사용)
    Scanner scan = new Scanner(System.in); // System.in : 키보드 입력 값

    do {
      // 맨 처음 실행 후, while에서 조건이 맞으면 do로 와서 반복
      // 반복할 문장들
      value = scan.nextInt(); 
    } while (value != 10);
   ```

  ### for
   - 구문 자체에 변수 초기화, 조건식, 증감식이 한줄로 표현
   ```java
    int value = 0;
    
    for (int i=0; i<10; i++) {
      if (i%2 == 0) {
        value ++;
        continue; // 아래 문장 실행 않고 바로 다시 for문 돌리기
      }
      value -= 1;
    }
   ```


 ## Python 과 차이
   1. 
    - python : 0은 false/ 나머지 true
    - java : 불가
   2. 
    - python : 1 < 변수 < 10
    - java : 변수 > 1 && 변수 < 10
    