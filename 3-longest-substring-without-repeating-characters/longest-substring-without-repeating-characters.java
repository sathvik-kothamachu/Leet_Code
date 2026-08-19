class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();

        int left = 0;
        int max = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);

            while (map.containsKey(c)) {
                char left_ch=s.charAt(left);
                map.remove(left_ch);
                left++;
            }

            map.put(c, right);

            max = Math.max(max, right - left + 1);
        }

        return max;
    }
}