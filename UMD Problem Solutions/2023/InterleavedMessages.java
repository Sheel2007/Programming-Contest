import java.util.*;

public class InterleavedMessages {
	public static String decrypt(String s, int k) {
		
		int word_count = s.length() / k;

		String answer = "";

		int start = 0;

		while (true) {
			for (int index = start; index < s.length(); index += word_count) {
				answer += s.charAt(index);
			}
			
			if (start + 1 < word_count) {
				start += 1;
			} else {
				break;
			}
		}

		return answer;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int numOfTestCases = sc.nextInt();
		sc.nextLine(); // skip the newline character

		for (int testCase=0; testCase < numOfTestCases; testCase++) { 
			int k = sc.nextInt();
			String s = sc.next();
			System.out.println(decrypt(s, k));
		}
		sc.close();
	}
}
