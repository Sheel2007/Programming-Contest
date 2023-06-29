import java.util.*;

public class FindLargestNumber {

	public static int findLargestNumber(int n, int digit1, int digit2) {
		
		ArrayList<Integer> list = new ArrayList<>();

		String numberString = String.valueOf(n);
		for (int i = 0; i < numberString.length(); i++) {
			int digit = Character.getNumericValue(numberString.charAt(i));
			list.add(digit);
		}

		//use .get(index) for arraylists
		int small_digit = 0;
		int big_digit = 0;

		if (digit1 >= digit2) {
			big_digit = digit1;
			small_digit = digit2;
		} else if (digit2 > digit1) {
			big_digit = digit2;
			small_digit = digit1;
		}

		int size = list.size();

		for (int i = 0; i < size; i++) {
			if (big_digit > list.get(i)) {
				list.add(i, big_digit);
				big_digit = -5000;
			} else if (big_digit == list.get(i)) {
				if (big_digit > list.get(i + 1)) {
					list.add(i+1, big_digit);
					big_digit = -5000;
				} else if (big_digit <= list.get(i + 1)) {
					list.add(i + 2, big_digit);
					big_digit = -5000;
				}
			}
		}

		for (int i = 0; i < size; i++) {
			if (small_digit > list.get(i)) {
				list.add(i, small_digit);
				small_digit = -5000;
			} else if (small_digit == list.get(i)) {
				if (small_digit > list.get(i + 1)) {
					list.add(i+1, small_digit);
					small_digit = -5000;
				} else if (small_digit <= list.get(i + 1)) {
					list.add(i + 2, small_digit);
					small_digit = -5000;
				}
			}
		}

		if (big_digit != -5000 && small_digit != 5000) {
			if (big_digit >= small_digit) {
				list.add(big_digit);
				list.add(small_digit);
			} else {
				list.add(small_digit);
				list.add(big_digit);
			}
		} else if (big_digit != -5000) {
			list.add(big_digit);
		} else if (small_digit != -5000) {
			list.add(small_digit);
		}

		StringBuilder sb = new StringBuilder();
		for (Integer num : list) {
				sb.append(num);
		}

		String result = sb.toString();

		return Integer.parseInt(result);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int numOfTestCases = sc.nextInt();
		sc.nextLine();

		for (int testCase=0; testCase < numOfTestCases; testCase++) { 
			int n = sc.nextInt();
			int digit1 = sc.nextInt();
			int digit2 = sc.nextInt();
			System.out.println(findLargestNumber(n, digit1, digit2));
		}

		sc.close();
	}
}
