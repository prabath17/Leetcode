import java.util.*;
class Solution {
    public int sumOfUnique(int[] nums) {
        HashMap<Integer,Integer> freq=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            freq.put(nums[i],freq.getOrDefault(nums[i],0)+1);
        }
        int sum=0;
        for(int i:freq.keySet()){
            if(freq.get(i)==1){
            sum+=i;
        }
        }
        return sum; 
        
    }
}