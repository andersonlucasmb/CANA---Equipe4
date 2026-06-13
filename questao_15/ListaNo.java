public class ListaNo {
    ListaNo(int valor){
        this.valor = valor;
        this.anterior = null;
        this.proximo = null;
    }

    public ListaNo anterior;
    public ListaNo proximo;
    public int valor;
}
