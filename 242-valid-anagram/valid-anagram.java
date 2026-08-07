import java.util.*;

class Solution {
    public boolean isAnagram(String s, String t) {
        char arr_s[]=s.toCharArray();
        char arr_t[]=t.toCharArray();
        if(s.length()!=t.length()){
            return false;
        }

        Arrays.sort(arr_s);
        Arrays.sort(arr_t);
        return Arrays.equals(arr_s,arr_t);
        
    }
}