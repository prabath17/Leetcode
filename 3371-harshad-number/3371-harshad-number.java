class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
    int ref=x;
    int sum=0;
    while(x>0){
        int rem =x%10;
        sum=sum +rem;
        x/=10;
    }
    System.out.println(ref);
    System.out.print(sum);
    return    ref%sum==0 ? sum :-1;
    }
}