#include <stdio.h>
#include <stdlib.h>
/*2. Considere um programa que armazena as notas dos alunos de uma turma. Pede-se: 
a) Ler e armazenar em um vetor de tamanho máximo de 100 elementos os valores das notas. 
Esse processo deve ser feito enquanto o vetor não atingir o tamanho máximo ou até que um valor negativo seja informado;
 b) Calcular e exibir a médias das notas; 
 c) Exibir as notas que ficaram acima da média calculada anteriormente. 
*/

int main(){
    int MAX;
    printf("Digite o numero total de alunos: ");
    scanf("%d", &MAX);

    float notas[MAX];
    float media;
    float soma;

    //a)
    printf("Digite agora a nota dos alunos. OBS: Nao digite numeros negativos!\n");
    for(int i=0; i<MAX; i++){
        printf("Digite a nota do aluno %d: ", i+1);
        scanf("%f", &notas[i]);      
    }

    //b)
    for(int i=0; i<MAX; i++){
        soma = soma + notas[i];
    }
    media = soma/MAX;
   
    printf("Esta e' a media das notas: %f.\n", media);

    //c
    printf("Estas sao as notas acima da media:\nSe nao aparecerem notas a seguir, e' porque nao ha' notas acima da media (%f)\n", media);

    for(int i = 0; i<MAX; i++){
        if(notas[i]>media){
            printf("%f\n", notas[i]);
        }
    }
    return 0;
}
