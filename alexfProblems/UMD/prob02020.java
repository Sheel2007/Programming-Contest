class prob02020 {
    public static void main(String[] args){
        for(String s:doFizzBuzz(2)){System.out.print(s + " ");} System.out.println();
        for(String s:doFizzBuzz(3)){System.out.print(s + " ");} System.out.println();
        for(String s:doFizzBuzz(15)){System.out.print(s + " ");} System.out.println();
    }
    public static String[] doFizzBuzz(int n) {
        String[] outStrings = new String[n];
        for(int x = 1;x <=n;x++){
            outStrings[x - 1] = Integer.toString(x);
            if (x % 3 == 0) {
                outStrings[x - 1] = "Fizz";
            } if (x % 5 == 0) {
                outStrings[x - 1] = "Buzz";
            }  if (x % 15 == 0) {
                outStrings[x - 1] = "FizzBuzz";
            }
        }
        return outStrings;
    }
}