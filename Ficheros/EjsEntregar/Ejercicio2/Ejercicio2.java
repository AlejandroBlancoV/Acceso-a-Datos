package Ejercicio2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ejercicio2 {
    public static void main(String[] args) {
         Scanner sc = new Scanner(System.in); 
         String texto=JOptionPane.showInputDialog("Introduce el texto nuevo para el archivo");
        System.out.println("Escribe la ruta del archivo");
        String ruta= sc.nextLine();
        
        try {
            BufferedWriter escritor= new BufferedWriter(new FileWriter(ruta));
            escritor.write(texto);
            escritor.close();
            BufferedReader lector = new BufferedReader(new FileReader(ruta));
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
