package src.main.java.laboratoare.laborator8.javaio.primitivestreams;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

/**
 * @author cvoinea
 *
 * 8 bit streams -> binary streams
 */
public class Ex2 {

    private static final String BASE_PATH = "src/main/java/laboratoare/laborator8/javaio/file/files/";

    public static void main(String[] args) {

        try (FileInputStream fis = new FileInputStream(BASE_PATH + "f1.txt");
             FileOutputStream fos = new FileOutputStream(new File(BASE_PATH, "f3.txt"))) {

            // return the number of bytes within the file so that we know the size of the byte array we create
            int size = fis.available();
            byte[] buffer = new byte[size];
            fis.read(buffer);
            fos.write(buffer);

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
