package main.java.laboratoare.laborator4.imutabilitate;

/**
 * @author cvoinea
 */
public class TestClient {

    public static void main(String[] args) {

        Adresa adresa = new Adresa("Maniu", 33);

        Client client = new Client(adresa);

        System.out.println("client initial: " + client);

        Adresa adresaDeLaClient = client.getAdresa();
        adresa.setNumar(66);

        System.out.println("adresa initiala dupa modificare:" + adresa);
        System.out.println("client dupa modificare numar adresa: " + client);

        ClientRecord clientRecord = new ClientRecord(adresa);
        System.out.println(clientRecord.adresa());
        System.out.println(clientRecord.toString());

    }
}
