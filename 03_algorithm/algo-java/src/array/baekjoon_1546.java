package array;

import java.util.Scanner;

/**
 * 백준_11720번
 * Title : 숫자의 합 구하기
 */

public class baekjoon_11720 {
    public static void main(String[] args) {
        // 1. 숫자갯수 : 100 일때, 100자리수가 나오고 해당 수를 나눠야하니까 int/long 으로는 못받음
        // 2. 그럼 String 으로 받아서 하나씩 배열로 나눠서 담기 -> toCharArray 함수 사용!
        // 3. 하나씩 나눈 String 을 int 형으로 형변환 -> 아스키코드 참고
        // 4. 자릿수 나누기 (나눈 몫을 다 더하기)

    /* 아스키코드
       문자와 숫자 아스키코드 값 차이 : 48
       ex. 문자'1' = 아스키코드값49 -> 문자 '1' 을 숫자 1로 변환하려면,,, '1'-48 ('1'-'0')
     */

        Scanner sc = new Scanner(System.in);
        int cnt = sc.nextInt();
        String numbers = sc.next();
        int result = 0;
        char[] numList = numbers.toCharArray();

        for (int i = 0; i < cnt; i++) {
            result += numList[i] - '0';
//        result += numList[i] - 48;
//        result += Integer.parseInt(String.valueOf(numList[i]));
        }
        System.out.println(result);
    }
}
