package ejs;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class ConexionBD extends JFrame{
	
	private Connection con;
	
	
	/**
	 * @wbp.parser.entryPoint
	 */
	public ConexionBD(String host, String puerto, String user, String pswd) {
		
		this.con=conectar(host, puerto, user, pswd);
	}
	
	/**
	 * @wbp.parser.entryPoint
	 */
	private Connection conectar(String host,String puerto,String user,String pswd) {
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			String URL="jdbc:mysql://"+host+":"+puerto;
			Connection con=DriverManager.getConnection(URL,user,pswd);
			JOptionPane.showMessageDialog(null, "Conexión establecida");
			return con;
		} catch (ClassNotFoundException | SQLException e) {
			// TODO Auto-generated catch block
			JOptionPane.showMessageDialog(null, "Conexión fallida");
			e.printStackTrace();
			System.out.println(e.getMessage());
			return null;
		}
	}
	
	/**
	 * @wbp.parser.entryPoint
	 */
	public Connection getCon() {
		return this.con;
	}

}
