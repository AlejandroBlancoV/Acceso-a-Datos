package Ejercicio2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

public class Ejercicio2Alternativo {
     public static void main(String[] args) {
        JFileChooser selector = new JFileChooser();
        File fichero= null;
         String texto=JOptionPane.showInputDialog("Introduce el texto nuevo para el archivo");
        JOptionPane.showMessageDialog(null, "Selecciona archivo");
         int decision = selector.showOpenDialog(null);
         if (decision == JFileChooser.APPROVE_OPTION) {
             fichero= selector.getSelectedFile();
            
     }
        
        try {
            BufferedWriter escritor= new BufferedWriter(new FileWriter(fichero));
            escritor.write(texto);
            escritor.close();
            BufferedReader lector = new BufferedReader(new FileReader(fichero));
            String contenido = "";
            String linea;
            while((linea = lector.readLine()) != null){
                contenido += linea + "\n";
            }
            lector.close();
            System.out.println("el contenido es: "+contenido);
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
