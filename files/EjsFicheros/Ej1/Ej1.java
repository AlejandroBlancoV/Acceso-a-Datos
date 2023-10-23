package files.EjsFicheros.Ej1;

import java.io.File;
import java.io.IOException;

import javax.swing.JFileChooser;

public class Ej1 {
    public static void main(String[] args) throws IOException{
        JFileChooser chooser= new JFileChooser();
        chooser.setMultiSelectionEnabled(true);
        int result = chooser.showOpenDialog(null);
        if(result!= JFileChooser.APPROVE_OPTION){
            System.exit(1);
        }
        File[] ficheros= chooser.getSelectedFiles();
        
    }

}