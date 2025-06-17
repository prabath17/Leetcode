class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*int[] arr=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            int prod=1;
            for(int j=0;j<nums.length;j++){
                if(i!=j){
                    prod*=nums[j];
                }
                
            }
            arr[i]=prod;
        }
        return arr; */
        int[] arr=new int[nums.length];
        int zero=0,inx=-1,prod=1;
        for(int i=0;i<nums.length;i++){
            if (nums[i]==0){
                zero++;
                inx=i;
            }
            else{
                prod*=nums[i];
            }
        }
        if(zero==0){
            for(int i=0;i<nums.length;i++){
                arr[i]=prod/nums[i];
            }
        }
        else if (zero==1){
            arr[inx]=prod;
        }
        return arr;
    }
}