package array;

import java.util.Arrays;
import java.util.Scanner;

/**
 * 백준_1546번
 * Title : 평균 구하기
 */

public class baekjoon_1546 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double result;
        double maxScore;
        double sumScore = 0;
        int testCnt = sc.nextInt();
        int[] scores = new int[testCnt];
        double[] newScores = new double[testCnt];

        for (var i=0; i<testCnt; i++) {
            scores[i] = sc.nextInt();
        }

        Arrays.sort(scores);
        maxScore = scores[testCnt-1];

        /*
        for (var i=0; i<testCnt; i++) {
            newScores[i] = (scores[i]/maxScore) * 100.0;
            System.out.println("1 + " + scores[i] + "----" + maxScore);
            System.out.println("scores==== " + scores[i]/maxScore);
            sumScore += newScores[i];
        }
        result = sumScore / testCnt;
        */

        // Simple Solution
        for (var i=0; i<testCnt; i++) {
            sumScore += scores[i];
        }

        result = (sumScore * 100.0) / maxScore / testCnt;

        // 소수점 계산은 곱하기나 나누기할 때, 자연수로 안하고 ".0" 으로 계산하면 double 형태로 소수점 표시됨
        System.out.println(result);
    }
}
