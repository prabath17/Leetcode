class Solution {
    public int rob(int[] nums) {
        /*int odd=0;
        int even=0;
        for(int i=0;i<nums.length;i++){
            if(i%2==0){
                even+=nums[i];
            }
            else{
                odd+=nums[i];
            }
        }
        return Math.max(odd,even); */
        if (nums.length == 0) {
            
            return 0;
        }

        if (nums.length == 1) {
            
            return nums[0];
        }
        int prev2=nums[0];
        int prev1=Math.max(nums[0],nums[1]);
        for(int i=2;i<nums.length;i++){
            int curr=Math.max(prev1,prev2+nums[i]);
            prev2=prev1;
            prev1=curr;
        }
        return prev1;
    }
}