import java.util.*;

class DecodeString {
    public String decodeString(String s) {
        Stack<Integer> numStack = new Stack<>();
        Stack<String> strStack = new Stack<>();
        String curr = "";
        int num = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            } else if (c == '[') {
                numStack.push(num);
                strStack.push(curr);
                num = 0;
                curr = "";
            } else if (c == ']') {
                int k = numStack.pop();
                String prev = strStack.pop();
                curr = prev + curr.repeat(k);
            } else {
                curr += c;
            }
        }
        return curr;
    }
}
