class Solution {
    public int maxDistance(int[] colors) {
        int n = colors.length;
        int dist1 = 0, dist2 = 0;

        for (int i = n - 1; i >= 0; i--) {
            if (colors[i] != colors[0]) {
                dist1 = i;
                break;
            }
        }

        for (int i = 0; i < n; i++) {
            if (colors[i] != colors[n - 1]) {
                dist2 = n - 1 - i;
                break;
            }
        }

        return Math.max(dist1, dist2);
    }
}