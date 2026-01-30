//import java.util.*;
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
       
        ArrayList<Integer> list=new ArrayList<>();
        HashMap<Integer,Integer> map=new HashMap<>();
        int count=0;
        int[] copy=nums.clone();
        Arrays.sort(copy);
        for(int i=0;i<nums.length;i++){
            if (!list.isEmpty()) {
                int last = list.get(list.size() - 1);
                if (last!=copy[i]){
                    count=list.size();
                    list.add(copy[i]);
                }
                else{
                    list.add(copy[i]);
                }
                
            }
            else{
                //count+=1;
                list.add(copy[i]);
            }

            map.put(copy[i], count);
            //System.out.println(map);

        
        
    }
    
    for(int i=0;i<nums.length;i++){
        nums[i]=map.get(nums[i]);
    }
    return nums;
}
}