class Solution {
    public int characterReplacement(String s, int k) {
        int[] freq = new int[26];
        int left = 0, maxFreq = 0, best = 0;

        for (int right = 0; right < s.length(); right++) {
            int r = s.charAt(right) - 'A';
            freq[r]++;
            maxFreq = Math.max(maxFreq, freq[r]);     // track most frequent char in window

            if ((right - left + 1) - maxFreq > k) {
                freq[s.charAt(left) - 'A']--;
                maxFreq=0;
                left++;
            }else{
                best = Math.max(best, right - left + 1);

            }
        }
        return best;
    }
}