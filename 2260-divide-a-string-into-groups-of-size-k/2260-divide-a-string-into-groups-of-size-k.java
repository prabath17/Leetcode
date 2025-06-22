class Solution {
    public String[] divideString(String s, int k, char fill) {
       int remainder = s.length() % k;
        if (remainder != 0) {
            int toFill = k - remainder;
            for (int i = 0; i < toFill; i++) {
                s += fill;
            }
        }

        int n = s.length() / k;
        String[] arr = new String[n];
        int ind = 0;

        for (int i = 0; i < s.length(); i += k) {
            arr[ind++] = s.substring(i, i + k);
        }

        return arr;
    }
}