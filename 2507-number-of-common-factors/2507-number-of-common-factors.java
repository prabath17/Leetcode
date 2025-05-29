class Solution {
    public int commonFactors(int a, int b) {
        int count=0;
        int l=0;
        if (a>b){
            l=b;
        }
        else{
            l=a;
        }
        for (int i=1;i<l+1;i++){
            if (a%i==0 && b%i==0){
                count++;
            }

        }
        return count;
    }
}