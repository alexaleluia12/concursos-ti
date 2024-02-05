public class Main {

    public static boolean um_f(int v) {
        if (v % 2 != 0) {
            if (v >= 77 && v <= 81) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(um_f(79)); // Saida: true
        System.out.println(um_f(78)); // Saida: false
        System.out.println(um_f(50)); // Saida: false
    }
}
