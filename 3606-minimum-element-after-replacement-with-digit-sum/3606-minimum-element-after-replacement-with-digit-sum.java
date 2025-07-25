class Solution {
    public int minElement(int[] nums) {
        for (int i=0;i<nums.length;i++){
            int val=nums[i];
            int sum=0;
            while(val>0){
                int rem=val%10;
                sum+=rem;
                val/=10;
            }
            nums[i]=sum;
        }
        int min=nums[0];
        for (int i=0;i<nums.length;i++){
            if (min>nums[i]){
                min=nums[i];
            }
        }
        return min;
    }
}