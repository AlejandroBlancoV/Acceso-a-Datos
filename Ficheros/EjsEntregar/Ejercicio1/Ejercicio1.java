package Ejercicio1;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
public class Ejercicio1 {
    public static void main(String[] args) {
        JFileChooser selector = new JFileChooser();
        File ficheroEntrada1= null;
        File ficheroEntrada2=null;
        File ficheroSalida=null;
        JOptionPane.showMessageDialog(null, "Selecciona el primer archivo de entrada ");
        
        int decision = selector.showOpenDialog(null);
        if (decision == JFileChooser.APPROVE_OPTION) {
            ficheroEntrada1= selector.getSelectedFile();
           
    }
        
         JOptionPane.showMessageDialog(null, "Selecciona el segundo archivo de entrada ");
        
        decision = selector.showOpenDialog(null);
        if (decision == JFileChooser.APPROVE_OPTION) {
             ficheroEntrada2= selector.getSelectedFile();
        }
        JOptionPane.showMessageDialog(null, "Selecciona el archivo de salida ");
        
        decision = selector.showSaveDialog(null);
        if (decision == JFileChooser.APPROVE_OPTION) {
             ficheroSalida= selector.getSelectedFile();
        }
 try {
    BufferedReader lector1 = new BufferedReader(new FileReader(ficheroEntrada1));
     BufferedReader lector2 = new BufferedReader(new FileReader(ficheroEntrada2));
     BufferedWriter escritor= new BufferedWriter(new FileWriter(ficheroSalida));

    String linea1= lector1.readLine();
    String linea2= lector2.readLine();

    while (linea1 != null || linea2 != null) {
        if (linea1 != null) {
            escritor.write(linea1);
            escritor.newLine();
            linea1 = lector1.readLine();
        }

        if (linea2 != null) {
            escritor.write(linea2);
            escritor.newLine();
            linea2 = lector2.readLine();
        }
    }

    lector1.close();
    lector2.close();
    escritor.close();
} catch (FileNotFoundException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
} catch (IOException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
}



    }
    }

