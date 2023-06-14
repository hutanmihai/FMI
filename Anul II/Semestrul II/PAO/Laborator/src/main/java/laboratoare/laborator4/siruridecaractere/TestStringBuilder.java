package main.java.laboratoare.laborator4.siruridecaractere;

/**
 * @author cvoinea
 */
public class TestStringBuilder {

    public static void main(String[] args) {

        // inlocuire caracter index 3 cu *
        String s1 = "abcde"; // -> abc*e

        String s2 = s1.substring(0, 3) + "*" + s1.substring(4); // utilizare ineficienta a memoriei, se creaza in total 4 obiecte String
        System.out.println(s2);

        //Clasa mutabila, nu este thread-safe
        StringBuilder sb1 = new StringBuilder(s1); // pasam referinta catre obiectul String anterior creat s1
        sb1.replace(3, 4, "*");
        System.out.println("string builder: " + sb1);
        System.out.println("inversare ordine: " + sb1.reverse());

        // inlantuire apel metode
        StringBuilder sb2 = new StringBuilder();
        // se returneaza aceeasi instanta de StringBuilder, se adauga caracterele la final
        sb2.append('f').append(s1).append(s2).append(3).append(true).append(33).append(2.2d).append(new Object());
        System.out.println("inlantuire metode append(): " + sb2);

        String s3 = sb1 + s1; // concatenare String si StringBuilder
        System.out.println("s3 = " + s3);
    }
}
