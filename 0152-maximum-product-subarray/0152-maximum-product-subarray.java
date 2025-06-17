class Solution {
    public int maxProduct(int[] nums) {
        int p=nums[0];
        
        for(int i=0;i<nums.length;i++){
            int mul=1;
            for(int j=i;j<nums.length;j++){
                
                mul*=nums[j];
                p=Math.max(p,mul);
            }
            
        }
        return p;  
    }
}