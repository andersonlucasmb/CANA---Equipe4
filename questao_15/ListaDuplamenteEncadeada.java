public class ListaDuplamenteEncadeada {
    ListaDuplamenteEncadeada(){
        this.inicio = null;
        this.ultimo = null;
        this.quantidade = 0;
    }

    //complexidade O(n)
    int buscaLinear(int valor){
        ListaNo it = inicio;
        boolean encontrado = false;
        int i = 0;

        while(!encontrado && it != null)
        {
            if(it.valor == valor)
                encontrado = true;
            else
            {
                it = it.proximo;
                i++;
            }
        }

        return encontrado ? i : -1;
    }

    //essa implementacao eh foi feita em O(n)
    //O(n) eh a melhor implementacao possivel para busca binaria
    //em uma lista duplamente encadeada, a implementacao da busca binaria
    //na lista duplamente encadeada em O(log n) nao eh possivel pois nao se
    //tem acesso direito aos elementos em O(1),acessar o meio da lista e feito em O(n),
    //isso por si so ja torna impossivel a busca binaria em O(n) sem usar uma estrutura auxiliar
    int buscaBinaria(int valor){
        int indexEsquerda = 0;
        ListaNo esquerda = this.inicio;

        int indexDireita = quantidade - 1;
        ListaNo direita = this.ultimo;

        ListaNo metade = esquerda;
        int indexMetade = 0;

        while(indexEsquerda < indexDireita){
            int auxMetade = indexMetade;
            indexMetade =  (indexEsquerda + indexDireita) /2;

            auxMetade =  indexMetade - auxMetade;

            //decisao se move a metade pra esquerda ou direita
            //isso depende se o index da nova metade eh maior ou menor que a nova metade
            if(auxMetade > 0)
                for(int i = 0; i < auxMetade; i++)
                    metade = metade.proximo;
            else
                for(int i = 0; i < -auxMetade; i++)
                    metade = metade.anterior;

            //verifica se a esquerda ou direita eh a nova metade
            if(metade.valor < valor){
                indexEsquerda = indexMetade + 1;
                esquerda = metade;
            }
            else{
                indexDireita = indexMetade;
                direita = metade;
            }
        }

        return (direita.valor == valor ? indexDireita : -1);
    }

    void adicionar(int valor){
        ListaNo no = new ListaNo(valor);
        no.anterior = this.ultimo;
        no.proximo = null;

        if(this.inicio == null)
        {
            this.inicio = no;
        }
        else
        {
            this.ultimo.proximo = no;
        }

        this.ultimo = no;
        quantidade++;
    }

    void print(){
        ListaNo it = inicio;
        int i = 0;
        while(it != null)
        {
            System.out.println( i + " - "+ "[" + it.valor + "]");
            it = it.proximo; i++;
        }

    }

    ListaDuplamenteEncadeada ordenar(){
        ListaNo it = inicio;

        while(it != null)
        {
            ListaNo jt = it.proximo;
            while(jt != null)
            {
                if(it.valor > jt.valor)
                {
                    int aux = it.valor;
                    it.valor = jt.valor;
                    jt.valor = aux;
                }
                jt = jt.proximo;
            }
            it = it.proximo;
        }
        return this;
    }

    private ListaNo inicio;
    private ListaNo ultimo;
    private int quantidade;
}
