import java.util.*;

class Solution {
    public int[] solution(int[] A, int K) {
        if (K == 0 || A.length == 0) return A;
        LinkedList<Integer> arr = new LinkedList<Integer>();
        for (int num : A) arr.add(num);
        for (int i = 0; i < K; i++) arr.addFirst(arr.removeLast());
        int[] answer = new int[arr.size()];
        for (int i = 0; i < answer.length; i++) answer[i] = arr.get(i);
        return answer;
    }
}

// https://app.codility.com/demo/results/trainingQBRF3W-EPH/
