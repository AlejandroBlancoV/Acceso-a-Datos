package Ejercicio3;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

public class Ejercicio3 {
    public static String reemplazarPalabras(String texto, String palabraBuscada, String palabraReemplazo) {
        return texto.replaceAll(palabraBuscada, palabraReemplazo);
    }
    public static void main(String[] args) {
        JFileChooser selector = new JFileChooser();
        File fichero= null;
        JOptionPane.showMessageDialog(null, "Selecciona archivo");
         int decision = selector.showOpenDialog(null);
         if (decision == JFileChooser.APPROVE_OPTION) {
             fichero= selector.getSelectedFile();
            
     }
     String reemplazar=JOptionPane.showInputDialog("Introduce la palabra a reemplazar");
     String remplazo=JOptionPane.showInputDialog("Introduce una nueva palabra para sustituir la anterior");

      try {
            BufferedWriter escritor= new BufferedWriter(new FileWriter("reemplazo.txt"));
            BufferedReader lector = new BufferedReader(new FileReader(fichero));
            String linea;
            String modificado="";
            while ((linea = lector.readLine()) != null) {
               modificado= reemplazarPalabras(linea, reemplazar,remplazo)+"\n";
                escritor.write(modificado);
                escritor.newLine();
            }

            lector.close();
            escritor.close();
      }catch (Exception e){
        e.printStackTrace();
      }
    }
}
