import java.util.*;

// 알고리즘 문제 환경세팅
class Solution {
    public int[] solution(int[] arr, int divisor) {


        int[] answer = {};
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i=0; i<arr.length; i++){
            if(arr[i] % divisor == 0){
                list.add(arr[i]);
            }
        }

        if(list.isEmpty()){
            list.add(-1);
        }

        // 왜 배열의 크기를 지정해야되는지??
        // 사용할 때는 배열의 크기를 지정
        answer = new int[list.size()];

        for(int i=0; i<list.size(); i++){
            answer[i] = list.get(i);
        }
        Arrays.sort(answer);
        System.out.println(Arrays.toString(arr)); // sout를 해야 console창에 값이 나옴
        return answer;
    }
}

//Main 클래스에서 Solution클래스 선언해주기
public class Main {
    public static void main(String[] ars) {
        Solution s = new Solution();
        //입력요소를 선언해줘야 출력값이 나옴
        int[] a = {5, 9, 7, 10};
        s.solution(a, 5);
    }
}
