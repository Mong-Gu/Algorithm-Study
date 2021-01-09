import java.util.*;

class Solution {
    public int solution(int[] A) {
        HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
        int answer = 0;
        for (int num : A) {
            if (hm.containsKey(num)) hm.replace(num, hm.get(num) + 1);
            else hm.put(num, 1);
        }
        for (int key : hm.keySet()) {
            if (hm.get(key) % 2 != 0) {
                answer = key;
                break;
            }
        }
        return answer;
    }
}

// https://app.codility.com/demo/results/training5YQBC8-ZSR/
