class Solution {
    public int trap(int[] height) {
        int area = 0;
        int l = 0, r = height.length-1;
        int lmax = height[l], rmax = height[r];

        while (l < r) {
            if (lmax < rmax) {
                ++l;
                lmax = Math.max(lmax, height[l]);
                area += lmax - height[l];
            } else {
                --r;
                rmax = Math.max(rmax, height[r]);
                area += rmax - height[r];
            }
        }
        return area;
    }
}
