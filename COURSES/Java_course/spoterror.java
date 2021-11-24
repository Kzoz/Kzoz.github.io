
public class spoterror {

    public static void main(String[] args) {
        
       int data_array[] = {19,11,2,3,4,6,22,15,2,8};
       int i, size = 10;
       int evenNum = 0;
       for (i = 0; i < size;i++){
           if (data_array[i]%2 == 0){
               evenNum++;
           }
       } 
       System.out.println(evenNum);
    }
}