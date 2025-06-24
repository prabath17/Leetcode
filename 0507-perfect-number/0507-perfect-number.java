class Solution {
    public boolean checkPerfectNumber(int num) {
    int res=0;
    for(int i=1;i<(num/2)+1;i++){
        if(num%i==0){
            res+=i;
        }
    }
    if(num==res){
        return true;
    } 
    else{
        return false;
    }  
    }
}