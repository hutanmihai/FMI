package src.main.java.laboratoare.laborator8.javaio.processingstreams;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;

/**
 * @author cvoinea
 *
 * BufferedReader, BufferedWriter -  processing streams that operate on character buffers
 * BufferedInputStream, BufferedOutputStream – processing streams that operate on byte buffers
 */
public class Ex2 {
    private static final String BASE_PATH = "src/main/java/laboratoare/laborator8/javaio/file/files/";

    public static void main(String[] args) {

        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(BASE_PATH + "f1.txt"));
             BufferedWriter bufferedWriter = new BufferedWriter((new FileWriter(new File(BASE_PATH, "f5.txt"))))) {

            String line;
            while ((line = bufferedReader.readLine()) != null) {
                // split lines in words
                String[] words = line.split("[ ,.:;!?/()\\[\\]\"={}*-]+");
                Arrays.sort(words);
                for (String s : words) {
                    bufferedWriter.write(s);
                    bufferedWriter.write("\n");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
