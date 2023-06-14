package services;

import java.io.FileWriter;
import java.io.IOException;
import java.sql.Timestamp;

public class CSVService {
    FileWriter fileWriter;

    private static final CSVService INSTANCE = new CSVService();

    private CSVService() {
        try {
            this.fileWriter = new FileWriter("Proiect/src/csv/audit.csv", true);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static CSVService getInstance() {
        return INSTANCE;
    }

    public void addLine(String line) {
        try {
            this.fileWriter = new FileWriter("Proiect/src/csv/audit.csv", true);
            long datetime = System.currentTimeMillis();
            Timestamp timestamp = new Timestamp(datetime);
            this.fileWriter.write((line + "," + timestamp + "\n"));
            this.fileWriter.flush();
            this.fileWriter.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public void close() {
        try {
            this.fileWriter.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
