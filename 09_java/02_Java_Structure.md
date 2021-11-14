# Java_Structure

## 01. Operatore

### 연산자

> 산술연산자

- 사칙연산을 다루는 연산자



> 대입연산자



> 증감연산자

- ++ 숫자 : 먼저 피연산자의 값을 1 증가시킨 후에 해당 연산을 진행
- 숫자 ++ : 연산먼저, 그 후 그 숫자에 1 증가 (전체 연산에 영향을 미치지 않는다.)
- -- 숫자 : 먼저 피연산자의 값을 1 감소시킨 후에 해당 연산을 진행
- 숫자 -- : 연산먼저, 그 후 그 숫자에 1 감소 (전체 연산에 영향을 미치지 않는다.)

```java
public class test {
	public static void main(String[] args){
    int num1 = 7, num2 = 7;
    int result1, result2;   

    result1 = --num1 + 4;
    result2 = num2-- + 4;    

    System.out.println("전위 감소 연산자에 의한 결과 : "+ result1 + ", 변수의 값 : " + num1); // 10, 6
    System.out.println("후위 감소 연산자에 의한 결과 : "+ result2 + ", 변수의 값 : " + num2); // 11, 6
	}
}
```

```java
public class test {
	public static void main(String[] args){
    int x = 10;
    int y = x-- + 5 + --x;  

    System.out.println("x : "+ x + ", y : " + y);
    // 8, 23
	}
}
```



> 비교연산자

- python과 동일



> 논리연산자

- && == and
- || == or
- ! == not



> 비트연산자



> 기타연산자

- 삼항연산자 `조건식 ? 반환값1 : 반환값2`
- instanceof 연산자
  - 참조 변수가 참조하고 있는 인스턴스의 실제 타입을 반환
  - `인스턴스이름 instanceof 클래스또는인터페이스이름`



## 02. 제어문

>제어문에 속하는 명령문들은 중괄호({})로 둘러싸여 있으며, 이러한 중괄호 영역을 블록(block)



### 조건문

1. if/ else if/ else 문

   ```java
   public class test {
   	public static void main(String[] args){
       char ch = 'B';
           
       if (ch >= 'a' && ch <= 'z') {
         System.out.println("해당 문자는 영문 소문자입니다.");
           
       } else if (ch >= 'A' && ch <= 'Z') {
         System.out.println("해당 문자는 영문 대문자입니다.");
   
       } else {
         System.out.println("해당 문자는 영문자가 아닙니다.");
       }
     }
   }
   ```

2. switch 문

   -  if / else 문보다 가독성이 더 좋다.

   - 컴파일러가 최적화를 쉽게 할 수 있어 속도 또한 빠른 편

   - default 절은 위의 예제와 같이 맨 마지막에 위치하는 것이 일반

   - 각 case 절 및 default 절은 반드시 break 키워드를 포함

     전체 switch 문을 빠져나가게 해줌

     break 키워드가 없다면, 조건에 해당하는 switch 문의 case 절 이후의 모든 case 절이 전부 실행

   ```java
   switch (ch) {
       case 'a':
           System.out.println("해당 문자는 'A'입니다.");
           break;
       case 'e':
           System.out.println("해당 문자는 'E'입니다.");
           break;
       case 'i':
           System.out.println("해당 문자는 'I'입니다.");
           break;
       case 'o':
           System.out.println("해당 문자는 'O'입니다.");
           break;
       case 'u':
           System.out.println("해당 문자는 'U'입니다.");
           break;
       default:
           System.out.println("해당 문자는 모음이 아닙니다.");
           break;
   }
   ```

   

### 반복문

1. while 문

   ```java
   public class test {
   	public static void main(String[] args){
       int i = 0; 
   
       while (i < 5) {
           System.out.println("while 문이 " + (i) + "번째 반복 실행중입니다.");
           i++; // 이 부분을 삭제하면 무한 루프에 빠지게 됨.
       }
       System.out.println("while 문이 종료된 후 변수 i의 값은 " + i + "입니다.");
     }
   }
   ```

2. do / while 문

   - do 안의 명령문 : 조건식의 결과가 참인 동안 반복적으로 실행하고자 하는 명령문
   - while 뒤의 명령문 : 조건식 결과를 변경하는 명령문

   ```java
   public class test {
   	public static void main(String[] args){
       int i = 1, j = 1;    
       do {
           System.out.println("do / while 문이 " + i + "번째 반복 실행중입니다.");
           j++; // 이 부분을 삭제하면 무한 루프에 빠지게 됨.
       } while (j < 1);
   
       System.out.println("do / while 문이 종료된 후 변수 j의 값은 " + j + "입니다.");
     }
   }
   ```

3. for 문

   - 기본 문법

     - 초기식, 조건식, 증감식은 각각 생략 가능 
     - 자바에서는 for 문 안에서만 사용하는 변수를 초기식에서 직접 선언
     - for 문에서 직접 선언된 변수는 for 문이 종료되면 같이 소멸

     ```java
     for (초기식; 조건식; 증감식) {
         조건식의 결과가 참인 동안 반복적으로 실행하고자 하는 명령문;
     }
     ```

     ```java
     public class test {
     	public static void main(String[] args){
         int i;    
         for (i = 0; i < 5; i++) {
           System.out.println("for 문이 " + (i + 1) + "번째 반복 실행중입니다."); 
         } 
         System.out.println("for 문이 종료된 후 변수 i의 값은 " + i + "입니다.");
       }
     }
     ```

4. Enhanced for 문



### 루프의 제어

- continue 문

  ```java
  public class test {
  	public static void main(String[] args){
      for (int i = 1; i <= 100; i++) {
        if (i % 5 == 0 || i % 7 == 0) {  
            System.out.println(i);  
        } else {  
            continue;  
        }  
      }
    }
  }
  ```

- break 문

  ```java
  public class test {
  	public static void main(String[] args){
      int num = 1, sum = 0;
      while (true) { // 무한 루프
          sum += num;
          if (num == 100) {
              break;
          }
          num++;
      }
  
      System.out.println(sum);
    }
  }
  ```

- 이름을 가지는 반복문(break with label)

  - 일반적인 break 문은 단 하나의 반복문만을 빠져나가게 해줌

  - 여러 반복문이 중첩된 상황에서 한 번에 모든 반복문을 빠져나가거나, 특정 반복문까지만 빠져나가고 싶을 때

    => 반복문에 이름(label)을 설정

  - label은 반복문의 키워드 바로 앞에 위치

  ```java
  public class test {
  	public static void main(String[] args){
      allLoop : // 반복문의 이름 설정
      for (int i = 2; i < 10; i++) {
          for (int j = 2; j < 10; j++) {    
              if (i == 5) {
                  break allLoop; // 상위 for문인 allLoop를 찾아서 두 개의 for문 탈출
              }
              System.out.println(i + " * " + j + " = " + (i * j));
        }
      }
    }
  }
  ```

  
