#include <stdio.h>
#include <stdlib.h>

#define MAX 100

/*Graduação: 
1. Uma empresa resolveu dar um aumento de salário aos seus colaboradores seguindo 
os seguintes critérios: 
● Aumento de 20% para quem ganha menos de um salário mínimo; 
● Aumento de 15% para quem ganha entre um e três salários mínimo; 
● Aumento de 5% para quem ganha mais do que três salários mínimo. 
Com base nos dados apresentados, faça: 
a) Uma função que recebe o valor do salário mínimo e o valor do salário atual como parâmetro.
 Esta função deve calcular o reajuste e retornar o valor do novo salário.
 b) Uma função que receba um vetor contendo os salários dos colaboradores, o valor do salário mínimo e o tamanho do vetor.
  A função deve exibir o salário atual do colaborador e o valor do salário após o reajuste.
   Para o cálculo do reajuste, utilize a função implementada anteriormente. 
*/

float novo_salario(int minimo, float atual);
void salario_novo(float sal[], int minimo, int tamanho);

int main(){
    float atual;
    int minimo = 1045; //SALARIO MINIMO VALE 1045 REAIS
    printf("Digite seu salario: ");
    scanf("%f", &atual);
    printf("Seu novo salario e' %f.\n", novo_salario(minimo, atual));

    int tamanho;
    printf("Digite o numero de colaboradores: ");
    scanf("%d", &tamanho);
    float *sal[tamanho];

    printf("Agora voce vai digitar os salarios dos colaboradores. Pense nos colaboradores numerados de 1 a %d.\nMemorize o numero de cada um.\n", tamanho);
    for(int i = 0; i<tamanho; i++){
        printf("Digite o salario do colaborador %d: ", i+1);
        scanf("%f", sal[i]);
    }

    salario_novo(sal[tamanho], minimo, tamanho); 
    

    return 0;
}
//alternativa a)
float novo_salario(int minimo, float atual){
    float novo;
    if(atual<minimo){
        novo = atual * 0.2 + atual;
    }
    if(atual>minimo && atual<(minimo*3)){
        novo = atual * 0.15 + atual;
    }
    if(atual>(minimo*3)){
        novo = atual * 0.05 + atual;
    }
    return novo;
}

//alternativa b)
void salario_novo(float sal[], int minimo, int tamanho){
    
    printf("Estes sao os colaboradores e os novos salarios:\n");
    for(int i=0; i<tamanho; i++){
        
        float atual = sal[i];
        printf("Colaborador %d: %f.\n", i+1, novo_salario(minimo, atual));
       
    }
}
