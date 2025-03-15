import java.util.Scanner;

class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        String[] words = s.split("\\s+");
        StringBuilder result = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            result.append(words[i]).append(" ");
        }
        return result.toString().trim();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine(); 
        Solution solution = new Solution();
        String reversed = solution.reverseWords(input);

        System.out.println(reversed);

        sc.close();
    }
}
