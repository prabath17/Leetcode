class Solution {
    public int sumOfEncryptedInt(int[] nums) {
    int total=0;
    for(int i=0;i<nums.length;i++){
        int count=0;
        int max=0;
        int val=nums[i];
        while(val>0){
            int rem=val%10;
            count=count*10 +1;
            if(rem>max){
                max=rem;
            }
            val/=10;
        }
        total+=(count*max);
    }
    return total;
    }
}