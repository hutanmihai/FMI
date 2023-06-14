package main.java.laboratoare.laborator4.siruridecaractere;

/**
 * @author cvoinea
 */
public class TestImutabilitateString {

    public static void main(String[] args) {
        String s1 = "abc";
        System.out.println("append pe String: ");
        appendString(s1, "cde");
        System.out.println(s1);

        StringBuilder sb1 = new StringBuilder(s1);
        System.out.println("append pe StringBuilder: ");
        appendString(sb1, "cde");
        System.out.println(sb1);
    }

    private static void appendString(Object existing, String toAppend) {
        if (existing instanceof String) {
            existing = existing + toAppend;
        } else if (existing instanceof StringBuilder) {
            ((StringBuilder) existing).append(toAppend);
        } else {
            System.out.println("referinta nu este de tipul String sau StringBuilder");
        }
        System.out.println(existing);
    }

}
