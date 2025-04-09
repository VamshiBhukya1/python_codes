import java.util.Scanner;

import javax.print.DocFlavor.STRING;

class exp{
    public static void main(String[] args) {
        Scanner sc = new Scanner((System.in));

        String s = "Coding in CodeChef";

        String[] ar = s.split(" ");
        int siz = 0;
        for(int i = 0; i < ar.length;i++){
            System.out.println(ar[i]+" :"+ar[i].length());
            siz += ar[i].length();
        }
        System.out.println("String size : "+siz);
    }
}