import java.util.Arrays;
class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        Arrays.sort(capacity);
        int total_apple=0;
        for(int i: apple){
            total_apple+=i;
        }
        int count=0;
        for(int i=capacity.length-1;i>=0;i--){
            if(total_apple>0){
                count+=1;
                total_apple-=capacity[i];
            }
            else{
                break;
            }
        }
        return count;
    }
}