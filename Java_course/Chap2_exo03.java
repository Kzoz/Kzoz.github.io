
public class Chap2_exo03 {

    public static void main(String[] args) {
        
        int array[] = {1,23,14,205,48};
        int ind = 0;
        for (int i = 1; i < array.length; i++){
            if (array[i] >= array[ind]){
                ind = i;
                    }
            }
        System.out.println(ind);
    }
}