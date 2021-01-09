import java.util.*;

class Solution {
    public int solution(int N) {
        String binary = Integer.toBinaryString(N);
        int answer = 0;
        int cnt = 0;
        for (int i = 1; i < binary.length(); i++) {
            if (binary.charAt(i) == '0') {
                cnt += 1;
            }
            else {
                if (cnt > answer) {
                    answer = cnt;
                }
                cnt = 0;
            }
        }
        return answer;
    }
}

// https://app.codility.com/demo/results/trainingC63HF5-PQ3/
