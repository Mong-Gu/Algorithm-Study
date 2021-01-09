import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> tmp = new ArrayList<Integer>();
        for(int i : arr) {
            if (i % divisor == 0) {
                tmp.add(i);
            }
        }
        if(tmp.isEmpty()) {
            tmp.add(-1);
        }
        int[] answer = new int[tmp.size()];
        for (int i = 0; i < tmp.size(); i++) {
            answer[i] = tmp.get(i);
        }
        Arrays.sort(answer);
        return answer;
    }
}

