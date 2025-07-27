class Solution {
    public boolean isMonotonic(int[] nums) {
        
        int inc=0;
        for (int i=1;i<nums.length;i++){
            
            if (nums[i-1]<nums[i]){
                inc++;
            }
        }
        int dec=0;
        for (int i=1;i<nums.length;i++){
            
            if (nums[i-1]>nums[i]){
                dec++;
            }
        }
            
                
        //System.out.println(count);
        if (inc==0 || dec==0){
            return true;
        }
        else{
            return false;
        }
        
    }
}