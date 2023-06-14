package src.main.java.laboratoare.laborator8.javaio.processingstreams;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;

/**
 *  @author cvoinea
 *
 *	DataInputStream, DataOutputStream - bytes are grouped to represent primitive data types or String
 */
public class Ex1 {

	private static final double[] DOUBLES = {1.1, 234.11, 33.434, 546.45, 43543_23.44};
	private static final String BASE_PATH = "src/main/java/laboratoare/laborator8/javaio/file/files/";

	public static void main(String[] args) {

		writeToFile();
		readFromFile();
	}

	private static void writeToFile(){
		try (DataOutputStream dataOutputStream = new DataOutputStream(new FileOutputStream(new File(BASE_PATH, "f4.txt"), false))){
			// first write the number of values inserted
			dataOutputStream.writeInt(DOUBLES.length);
			for (double d : DOUBLES) {
				dataOutputStream.writeDouble(d);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static void readFromFile(){
		try (DataInputStream dataInputStream = new DataInputStream(new FileInputStream(new File(BASE_PATH, "f4.txt")))){
			// first read the number of values (previously inserted)
			int size = dataInputStream.readInt();
			double[] doubles = new double[size];
			for (int i = 0; i < size; i++){
				doubles[i] = dataInputStream.readDouble();
			}
			System.out.println(Arrays.toString(doubles));
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
