class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0, fuel = 0, start = 0;
        for (int i = 0; i < gas.length; i++) {
            total += gas[i] - cost[i];
            fuel += gas[i] - cost[i];

            if (fuel < 0) {
                fuel = 0;
                start = i + 1;
            }
        }
        if (total < 0) return -1;
        return start;
    }
}
