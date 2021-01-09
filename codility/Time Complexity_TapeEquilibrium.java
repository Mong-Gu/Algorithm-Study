import java.util.*;

class Solution {
    public int solution(int[] A) {
        int left_sum = A[0];
        int right_sum = 0;
        for (int i = 1; i < A.length; i++)
            right_sum += A[i];
        int answer = Math.abs(left_sum - right_sum);
        int curr;
        for (int i = 1; i < A.length - 1; i++) {
            left_sum += A[i];
            right_sum -= A[i];
            curr = Math.abs(left_sum - right_sum);
            answer = Math.min(answer, curr);
        }
        return answer;
    }
}

// https://app.codility.com/demo/results/trainingD9WPBK-9M9/
