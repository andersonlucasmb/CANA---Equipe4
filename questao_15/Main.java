public class Main {
    static void main(String[] args) {
        ListaDuplamenteEncadeada lpe = new ListaDuplamenteEncadeada();

        //Lista encadeada
        lpe.adicionar(5);
        lpe.adicionar(-5);
        lpe.adicionar(0);
        lpe.adicionar(10);
        lpe.adicionar(100);
        lpe.adicionar(-100);
        lpe.adicionar(2);
        lpe.adicionar(2);
        lpe.adicionar(20);

        lpe.print();
        System.out.println("Busca Linear:");
        System.out.println(lpe.buscaLinear(5));
        System.out.println(lpe.buscaLinear(0));
        System.out.println(lpe.buscaLinear(100));
        System.out.println(lpe.buscaLinear(99));
        System.out.println();

        lpe.ordenar().print();
        System.out.println("Busca Binaria:");
        System.out.println(lpe.buscaBinaria(2));
        System.out.println(lpe.buscaBinaria(0));
        System.out.println(lpe.buscaBinaria(-100));
        System.out.println(lpe.buscaBinaria(20));
        System.out.println(lpe.buscaBinaria(99));
    }
}
