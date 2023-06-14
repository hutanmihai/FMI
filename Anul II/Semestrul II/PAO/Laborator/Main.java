class Tablou{
    static void met(int[] a, int b){
        int aux;
        aux = a[0];
        a[0] = b;
        b = aux;
    }
}

public class Main {
    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5};
        int b = 6;
        Tablou.met(a, b);
        int s = b;
        for (int i = 0; i < a.length; i++) s += a[i];
        System.out.println(s);
    }
}
