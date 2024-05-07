class Solution {
    public int romanToInt(String s) {
        // Map the values of roman numbers
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int number = 0;
        int N = s.length();

        for (int i=0; i<N-1; i++) {
            // Find value of current number
            int curr_val = map.get(s.charAt(i));

            // Find value of next number
            int next_val = map.get(s.charAt(i +1));

            if (curr_val < next_val)
                number -= curr_val;
            else
                number += curr_val;
        }
        
        // Add last number and return
        return number + map.get(s.charAt(N-1));
    }
}
