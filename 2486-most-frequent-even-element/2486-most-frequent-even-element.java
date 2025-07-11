import java.util.*;
class Solution {
    public int mostFrequentEven(int[] nums) {
      HashMap<Integer,Integer> freq=new HashMap<>();
        for (int i:nums){
            if (i%2==0){
            freq.put(i,freq.getOrDefault(i,0)+1);
            }
        }
        if (freq.size()==0){
            return -1;
        } 
        int val=Integer.MAX_VALUE;
        int max=0;
        for (int i : freq.keySet()) {
            int f = freq.get(i);
            if (f > max || (f == max && i < val)) {
                max = f;
                val = i;
            }
        }
        return val;
    }
}