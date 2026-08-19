package JAVAPoo;
import java.util.Scanner;

public class ex001 {
    public static void main(String[] args) throws Exception {
          Scanner sc = new Scanner(System.in);
          System.out.println("digite seu nome: ");
          String nome = sc.nextLine();
          System.out.println("digite sua idade: ");
          int idade = sc.nextInt();
          System.out.println(("Ola " + nome + "! Voce tem " + idade + " anos."));
          sc.close();
    }
}
