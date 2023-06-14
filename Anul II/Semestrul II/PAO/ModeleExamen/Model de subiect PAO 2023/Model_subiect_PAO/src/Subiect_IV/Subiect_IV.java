package Subiect_IV;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class Subiect_IV {

    public static void main(String[] args) {

        try (Connection conn = DriverManager.getConnection("jdbc:mysql://sql7.freemysqlhosting.net:3306/sql7620469" , "sql7620469" , "ATZWkKKaN5");) {

            Scanner in = new Scanner(System.in);

            System.out.println("Salariul minim: ");
            float s = in.nextFloat();

            System.out.println("Varsta maxima: ");
            int v = in.nextInt();

            PreparedStatement pst = null;
            ResultSet rs = null;

            pst = conn.prepareStatement("SELECT * FROM angajati WHERE Salariu > ? AND Varsta < ?");
            pst.setFloat(1, s);
            pst.setInt(2, v);

            rs = pst.executeQuery();

            while (rs.next()) {
                System.out.println(rs.getString("Nume") + " " + rs.getFloat("Salariu") + " " + rs.getInt("Varsta"));
            }

        } catch (SQLException ex) {
            System.out.println("Eroare JDBC: " + ex);
        }
    }
}
