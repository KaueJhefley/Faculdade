package JAVAPoo;

import java.util.Scanner;

public class ex002 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("informe um numero: ");
        int numero = sc.nextInt();
        int conta = numero % 2;

        if (conta == 0){
            System.out.println("numero e par.");
            
        }
        else{
            System.out.println("numero e impar.");
        }
        sc.close();
    }
}
