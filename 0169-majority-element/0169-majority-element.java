import java.util.*;
class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> freq=new HashMap<>();
        for (int i:nums){
            freq.put(i,freq.getOrDefault(i,0)+1);

        }
        int max=0;
        int val=0;
        for(int i:freq.keySet()){
            if (freq.get(i)>max){
                max=freq.get(i);
                val=i;
            }
        }
        return val;
    }
}