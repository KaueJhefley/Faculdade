package JAVAPoo;

import java.util.Scanner;

public class ex006 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("1-Gasolina \n 2-Alcool");
        int combustivel = sc.nextInt();
        System.out.println("Quantos litros deseja abastecer?");
        double quantidade = sc.nextDouble();

        if (combustivel == 1) {
            double preço = quantidade * 5.50;
            System.out.println("voce pagara " + preço);
        }
        else if (combustivel == 2) {
            double preço = quantidade * 4.00;
            System.out.println("voce pagara " + preço);
            
        }
        sc.close();

    }

}
