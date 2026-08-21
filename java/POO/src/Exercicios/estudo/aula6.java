
import java.util.Scanner;

import javax.swing.JOptionPane;

public class aula6 {
    public static void main(String[] args) {
        String filme = JOptionPane.showInputDialog(null, "voce e gueba? ", "TESTE DE GUEBISSE", JOptionPane.ERROR_MESSAGE);
        if (filme.equals("nao")) {
        JOptionPane.showMessageDialog(null, "mentira", "o caba mentiroso", JOptionPane.INFORMATION_MESSAGE);
        }
        else if (filme.equals("sim")) {
        JOptionPane.showMessageDialog(null, "Tudo bem cara", "ok", JOptionPane.INFORMATION_MESSAGE);
        }
        

    }

}