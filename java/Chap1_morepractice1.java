
public class Chap1_morepractice1 {

    public static void main(String[] args) {
        String a = "I am learning Java.";
        String b = "You are learning Java.";

        if (a.length() > b.length()) {
            System.out.println(a);
        } else if (b.length() > a.length()) {
            System.out.println(b);
        } else {
            System.out.println(a+b);
        }
    }
}