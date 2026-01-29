class Solution {
    public int[] distinctDifferenceArray(int[] nums) {
        int n = nums.length;
        HashSet<Integer> a = new HashSet<>();
        int[] pre = new int[n];
        HashSet<Integer> b = new HashSet<>();
        int[] suff = new int[n];

        int i = 0;
        int j = n - 1;

        while (i < n || j >= 0) {
            suff[j] = b.size();
            a.add(nums[i]);
            pre[i] = a.size();
            b.add(nums[j]);

            i++;
            j--;
        }
        //return suff;

        for (int x = 0; x < n; x++) {
            nums[x] = pre[x] - suff[x];
        }

        return nums;

    }
}