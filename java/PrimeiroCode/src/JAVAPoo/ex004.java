package JAVAPoo;

import java.util.Scanner;

public class ex004 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite seu peso em kg: ");
        double peso = sc.nextDouble();

        System.out.print("Digite sua altura em metros: ");
        double altura = sc.nextDouble();

        double imc = peso / (altura * altura);

        System.out.println("Seu IMC é: " + imc);

        if (imc < 18.5) {
            System.out.println("Abaixo do peso");
        } else if (imc < 25) {
            System.out.println("Peso normal");
        } else if (imc < 30) {
            System.out.println("Sobrepeso");
        } else {
            System.out.println("Obeso");
        }   
        sc.close();
    }
}
    

