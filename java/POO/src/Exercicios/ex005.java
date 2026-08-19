package JAVAPoo;

import java.util.Scanner;

public class ex005 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o nome de usuário: ");
        String usuario = sc.nextLine();

        System.out.print("Digite a senha: ");
        String senha = sc.nextLine();

        if (usuario == "admin" && senha == "1234" ) {
            System.out.println("Login bem-sucedido");
        } else {
            System.out.println("Usuário ou senha incorretos");
        }

        sc.close();
    }
}

