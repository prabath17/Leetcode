class Solution {
    public int maxProduct(int[] nums) {
        /*int p=nums[0];
        
        for(int i=0;i<nums.length;i++){
            int mul=1;
            for(int j=i;j<nums.length;j++){
                
                mul*=nums[j];
                p=Math.max(p,mul);
            }
            
        }
        return p;
        */
        int currmax=nums[0];
        int currmin=nums[0];
        int prodmax=nums[0];
        for(int i=1;i<nums.length;i++){
            
            int temp=Math.max(nums[i],Math.max(currmin*nums[i],currmax*nums[i]));
            currmin=Math.min(nums[i],Math.min(currmin*nums[i],currmax*nums[i]));
            currmax=temp;
            prodmax=Math.max(prodmax,currmax);
        }  
        return prodmax;
    }
}