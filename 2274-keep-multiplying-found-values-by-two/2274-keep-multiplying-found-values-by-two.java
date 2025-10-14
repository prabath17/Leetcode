import java.util.*;
class Solution {
    public int findFinalValue(int[] nums, int original) {
        Arrays.sort(nums);
        boolean flag=true;
        while(flag){
            for(int i=0;i<nums.length;i++){
                if(original==nums[i]){
                    original=original*2;
                    flag=true;
                    break;
                }
                else{
                    flag=false;
                }
                
            }
        }
        return original;
    }
}