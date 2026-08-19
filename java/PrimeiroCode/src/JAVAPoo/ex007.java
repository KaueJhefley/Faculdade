package JAVAPoo;

import java.util.Scanner;

public class ex007 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite um número de 1 a 10: ");
        int numero = sc.nextInt();

        if (numero >= 1 && numero <= 10) {
            System.out.println("Tabuada do " + numero + ":");
            for(int i = 1; i <= 10; i++) {
                System.out.println(numero + " x " + i + " = " + (numero * i));
            }
        }
        else{
            System.out.println("Numero invalido.");
        }
        sc.close();
    }
}