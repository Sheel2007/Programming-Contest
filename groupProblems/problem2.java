import java.util.ArrayList;

public class problem2 {
    public static void main(String[] args){ 
        swap(9999);
    } public static int swap(int n){
        String nString = Integer.toString(n);
        Integer nLen = nString.length();
        int[] nList = new int[nLen];
        for (int i=0;i<nLen;i++) {
            nList[i] = nString.charAt(i) - 48;
        }
        int biggest = 0;
        int biggestIndex = 0;
        for (int i=0;i<nList.length; i++){
            if (nList[i] >= biggest) {
                biggest = nList[i];
                biggestIndex = i;
            }
        }
        System.out.println(biggest);
        System.out.println(biggestIndex);
        ArrayList<Integer> numList = new ArrayList<Integer>();
        return n;
    }
}
