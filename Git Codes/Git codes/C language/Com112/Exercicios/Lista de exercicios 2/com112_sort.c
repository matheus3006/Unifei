#include <stdlib.h>
#include <stdio.h>
#include "com112_sort.h"



/////////////////////////////////////////////////////////
void bubblesort(int *v){
int i = 0;
int b = 10;
int a = 1;

do{
    for(int j=0; j<10; j++){
            a++;
            if(v[j]<v[j+1]){
                int aux;    
                aux = v[j];
                v[j] = v[j+1]; 
                b++;
                v[j+1] = aux; 
                b++;
            }else{
                b--;
            }
        }
        i++;
    }while(i != 10);
    printf("\nTempo de excecucao: \nNumero de comparacoes: %d\nNumero de movimentacoes: %d\n", a, b);
}

/////////////////////////////////////////////////////////
void selectionsort(int *v){
int i, j, aux, menor;
int a = 0;
int b = 0;
for(i = 0; i < 10; i++){
        menor = i;
        for(j = i+1; j < 10; j++)
        {   
            a++;
            if(v[j] < v[menor])
                menor = j;
        }
            a++;
            if(i != menor){
                aux = v[i];
                v[i] = v[menor];
                b++;
                v[menor] = aux;
                b++;
        }
    }
    printf("\nTempo de excecucao: \nNumero de comparacoes: %d\nNumero de movimentacoes: %d\n", a, b);
}

/////////////////////////////////////////////////////////
void insertionsort(int *v) {

	int i, j;
	int aux;
	int compara=0;
	int movimenta=0;

	for (i = 1; i < 10; i++) {
		aux = v[i];
		j = i - 1;
		if(aux < v[j])
			compara++;
		while ((j >= 0) && (aux < v[j])) {
			v[j + 1] = v[j];
			j--;
			movimenta++;
		}
		v[j + 1] = aux;
	}
	printf("\nTempo de excecucao: \nNumero de comparacoes: %d\nNumero de movimentacoes: %d\n", compara, movimenta);
} 

/////////////////////////////////////////////////////////
void menu(){
    int v[] = {1,2,3,4,5,10,9,8,7,6};
    int continuar=1;
    do
    {
        printf("\n\tExercicio do cao\n\n");
        printf("1. Bubble Sort\n");
        printf("2. Seletion Sort\n");
        printf("3. Insertion Sort\n");
        printf("4. Ver o relatorio\n");
        printf("0. Sair\n");

        scanf("%d", &continuar);
        system("cls || clear");

        switch(continuar)
        {
            case 1:
                bubblesort(v);
                printf("\n\nVetor ordenado em Bubble Sort:\n");
                for(int i=0; i<10; i++){
                printf("%d ", v[i]);
                }
                break;

            case 2:
                selectionsort(v);
                printf("\n\nVetor ordenado em Selection Sort:\n");
                for(int i = 0; i < 10; i++){
                    printf("%d ", v[i]);
                    printf("\n");
                }
                break;

            case 3:
                insertionsort(v);
                printf("\n\nVetor ordenado em Insertion Sort:\n");
                for(int i = 0; i < 10; i++){
                printf("%d ", v[i]);
                printf("\n");
                }
                break;

            case 4:
                relatorio(v);
                break;

            case 0:
                
                break;

            default:
                printf("Digite uma opcao valida\n");
        }
    } while(continuar);
}


/////////////////////////////////////////////////////////
int relatorio(int *v){

    printf("\n\nNumero de elementos ordenados: 10\n\n");
    printf("\nMetodo Bubble Sort\n");
    bubblesort(v);

    printf("\nMetodo Selection Sort\n");
    selectionsort(v);

    printf("\nMetodo Insertion Sort\n");
    insertionsort(v);
}