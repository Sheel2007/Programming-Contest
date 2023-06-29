import java.util.*;

public class AllPairsRelativelyPrime {

	public static boolean allPairsRelativelyPrime(int[] distances) {
		for (int i = 0;  i < distances.length; i ++) {
			for (int j = 0; j < distances.length; j ++) {
				if ((distances[i] % distances[j] == 0) || (distances[j] % distances[i] == 0)) {
					if (distances[i] != distances[j]) {
						return false;
					}
				}
			}
		}
		
		return true;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int numOfTestCases = sc.nextInt();
		sc.nextLine();

		for (int testCase=0; testCase < numOfTestCases; testCase++) { 
			int n = sc.nextInt();
			int[] distances = new int[n];
			for (int i = 0; i < n; i++) {
				distances[i] = sc.nextInt();
			}
			System.out.println(allPairsRelativelyPrime(distances) ? "All pairs relatively prime" : "There are some pairs that are not relatively prime");
		}

		sc.close();
	}
}
