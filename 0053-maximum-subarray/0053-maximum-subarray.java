class Solution {
    public int maxSubArray(int[] nums) {
        int c=nums[0];
        int g=nums[0];
        for(int i=1;i<nums.length;i++){
            c=Math.max(c+nums[i],nums[i]);
            g=Math.max(c,g);
        }
        return g;
    }
}