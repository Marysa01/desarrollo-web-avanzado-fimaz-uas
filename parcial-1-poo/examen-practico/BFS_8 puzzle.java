import java.util.*;

class Nodo {
    String estado; // Ej: "123456780"
    int cero; // posición del 0
    Nodo padre;

    public Nodo(String estado, Nodo padre) {
        this.estado = estado;
        this.padre = padre;
        this.cero = estado.indexOf('0');
    }
}

public class BFS8Puzzle {

    static final String OBJETIVO = "123456780";

    // Movimientos posibles
    static final int[][] movimientos = {
        {-1, 0}, {1, 0}, {0, -1}, {0, 1}
    };

    public static void main(String[] args) {
        String inicio = "123406758"; // puedes cambiarlo
        resolver(inicio);
    }

    public static void resolver(String inicio) {

        if (!esSoluble(inicio)) {
            System.out.println("El puzzle NO tiene solución");
            return;
        }

        Queue<Nodo> cola = new LinkedList<>();
        Set<String> visitados = new HashSet<>();

        Nodo inicial = new Nodo(inicio, null);
        cola.add(inicial);
        visitados.add(inicio);

        int pasos = 0;

        while (!cola.isEmpty()) {
            Nodo actual = cola.poll();

            if (actual.estado.equals(OBJETIVO)) {
                System.out.println("Solución encontrada en " + pasos + " pasos:");
                imprimirCamino(actual);
                return;
            }

            for (String vecino : generarVecinos(actual.estado)) {
                if (!visitados.contains(vecino)) {
                    cola.add(new Nodo(vecino, actual));
                    visitados.add(vecino);
                }
            }
            pasos++;
        }

        System.out.println("No se encontró solución");
    }

    // Generar movimientos
    public static List<String> generarVecinos(String estado) {
        List<String> vecinos = new ArrayList<>();

        int pos = estado.indexOf('0');
        int x = pos / 3;
        int y = pos % 3;

        for (int[] m : movimientos) {
            int nx = x + m[0];
            int ny = y + m[1];

            if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
                int nuevaPos = nx * 3 + ny;
                vecinos.add(intercambiar(estado, pos, nuevaPos));
            }
        }

        return vecinos;
    }

    // Intercambiar posiciones
    public static String intercambiar(String s, int i, int j) {
        char[] arr = s.toCharArray();
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        return new String(arr);
    }

    // Verificar si es resoluble
    public static boolean esSoluble(String estado) {
        int inversiones = 0;

        for (int i = 0; i < estado.length(); i++) {
            for (int j = i + 1; j < estado.length(); j++) {
                if (estado.charAt(i) != '0' && estado.charAt(j) != '0' &&
                    estado.charAt(i) > estado.charAt(j)) {
                    inversiones++;
                }
            }
        }

        return inversiones % 2 == 0;
    }

    // Imprimir solución
    public static void imprimirCamino(Nodo nodo) {
        List<String> camino = new ArrayList<>();

        while (nodo != null) {
            camino.add(nodo.estado);
            nodo = nodo.padre;
        }

        Collections.reverse(camino);

        for (String estado : camino) {
            imprimir(estado);
            System.out.println("-----");
        }
    }

    public static void imprimir(String estado) {
        for (int i = 0; i < 9; i++) {
            System.out.print(estado.charAt(i) + " ");
            if ((i + 1) % 3 == 0) System.out.println();
        }
    }
}