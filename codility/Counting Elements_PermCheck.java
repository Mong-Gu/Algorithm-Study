import java.util.*;

// 마지막 코드 : https://app.codility.com/demo/results/trainingA65V3Y-ZUX/
// 문제를 잘 좀 읽자...

class Solution {
    public int solution(int[] A) {
        Arrays.sort(A);
        int answer = 1;
        for (int i = 0; i < A.length; i++) {
            if (A[i] != i + 1) {
                answer = 0;
                break;
            }
        }
        return answer;
    }
}

// 두 번째 코드 : https://app.codility.com/demo/results/trainingPRKQ5R-KS9/
// class Solution {
//     public int solution(int[] A) {
//         Arrays.sort(A);
//         int answer = 1;
//         HashMap<Integer, Boolean> hm = new HashMap<Integer, Boolean>();
//         for (int i = 1; i < A.length; i++) {
//             if ((A[i-1] + 1 != A[i]) || hm.containsKey(A[i])) {
//                 answer = 0;
//                 break;
//             }
//             hm.put(A[i], true);
//         }
//         return answer;
//     }
// }

// 맨 처음 코드 : // https://app.codility.com/demo/results/trainingPXNCUW-9Z6/
// class Solution {
//     public int solution(int[] A) {
//         TreeMap<Integer, Boolean> tm = new TreeMap<Integer, Boolean>();
//         int answer = 1;
//         for (int num : A) {
//             if (tm.containsKey(num)) {
//                 answer = 0;
//                 break;
//             }
//             tm.put(num, true);
//         }
//         if (answer == 1) {
//             int curr = tm.firstKey();
//             for (Integer key : tm.keySet()) {
//                 if (curr++ != key) {
//                     answer = 0;
//                     break;
//                 }
//             }
//         }
//         return answer;
//     }
// }
