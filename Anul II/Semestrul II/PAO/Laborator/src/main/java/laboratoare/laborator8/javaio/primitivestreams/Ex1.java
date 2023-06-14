package src.main.java.laboratoare.laborator8.javaio.primitivestreams;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/**
 * @author cvoinea
 *
 * 16 bits streams -> character streams
 */
public class Ex1 {

    private static final String BASE_PATH = "src/main/java/laboratoare/laborator8/javaio/file/files/";

    public static void main(String[] args) {

        // use try-with-resources
        try (FileReader fr = new FileReader(BASE_PATH + "f1.txt");
             // check both situations for append = true/false
             FileWriter fw = new FileWriter(new File(BASE_PATH, "f2.txt"), false)) {

            int c;
            // read one character and store it in variable c while the end of the stream hasn't been reached (when -1 is returned by read() method)
            while ((c = fr.read()) != -1) {
                fw.write(c);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
