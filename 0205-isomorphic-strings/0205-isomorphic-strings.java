import java.util.HashMap;
import java.util.HashSet;

public class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) return false;

        HashMap<Character, Character> map = new HashMap<>();
        HashSet<Character> mapped = new HashSet<>();

        for (int i = 0; i < s.length(); i++) {
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);

            if (map.containsKey(c1)) {
                if (map.get(c1) != c2) {
                    return false;  // inconsistent mapping
                }
            } else {
                if (mapped.contains(c2)) {
                    return false;  // c2 already mapped to another char
                }
                map.put(c1, c2);
                mapped.add(c2);
            }
        }

        return true;
    }
}