package main.java.laboratoare.laborator4.siruridecaractere;

/**
 * @author cvoinea
 */
public class TextBlock {
    public static void main(String[] args) {

        String textBlock = """
                    În Java 15 au fost introduse clasele de tip înregistrare sau, pe scurt, înregistrari (records).
                    O înregistrare este o clasa imutabila utilizata pentru a manipula o multime fixa de valori,
                denumite componentele înregistrarii. De obicei, înregistrarile sunt utilizate pentru
                încarcarea unor date dintr-o anumita sursa - de exemplu: un fisier sau o baza de date, si 
                eventual transportarea acestora catre o anumita destinatie, folosind facilitatile limbajului
                Java pentru programarea în retea. """;

        String[] cuvinte = textBlock.split("[\\t.,:\\-()\\n\\s]+");

        // afisare cuvinte pe linii consecutive
        for (String cuvant : cuvinte) {
            System.out.println(cuvant);
        }
    }
}
