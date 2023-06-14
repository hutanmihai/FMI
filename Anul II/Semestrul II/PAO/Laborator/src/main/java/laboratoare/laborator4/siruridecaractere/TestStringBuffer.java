package main.java.laboratoare.laborator4.siruridecaractere;

/**
 * @author cvoinea
 */
public class TestStringBuffer {

    public static void main(String[] args) {

        // fata de StringBuilder, StringBuffer este thread-safe  => metodele sunt sincronizate => executie mai lenta
        StringBuffer sbf1 = new StringBuffer("adresa"); // conversie de la String la StringBuffer
        sbf1.reverse();
        System.out.println(sbf1);

        StringBuilder sb1 = new StringBuilder("test");
        StringBuffer sbf2 = new StringBuffer(sb1); // conversie de la StringBuilder la StringBuffer
        System.out.println(sbf2);

        StringBuilder sb2 = new StringBuilder(sbf1); // conversie de la StringBuffer la StringBuilder
        System.out.println(sb2.reverse());
    }
}
