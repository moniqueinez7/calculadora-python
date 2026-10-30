## Sobre o projeto
Minha primeira aplicação em Python, desenvolvida como parte do Desafio 1 de programação com Inteligência Artificial.

## Funcionalidades
- Adição
- Subtração
- Multiplicação
- Divisão

## Objetivo
Praticar lógica de programação, variáveis, funções e condições.

## Tecnologia
Python

Criar uma calculadora é um dos melhores projetos para quem está começando a
programar!

Abaixo está um código limpo, comentado e fácil de entender, seguido da
explicação detalhada de cada parte (incluindo o tratamento de divisão por zero).


## -m;fExplicação dos Principais Componentes

1. Funções (def)

Funções são pequenos blocos de código reaproveitáveis criados com a palavra def.

  - Elas recebem dados de entrada chamados parâmetros (no nosso caso, a e b).
  - A instrução return envia de volta o resultado do cálculo para onde a função
    foi chamada.

2. Tratamento da Divisão por Zero

Na matemática e na computação, dividir um número por zero é uma operação
indefinida. Se tentarmos fazer a / 0 no Python diretamente, o programa trava e
exibe o erro ZeroDivisionError.

  - Como resolvemos: Usamos uma verificação simples dentro da função dividir:
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    Isso garante que, se o segundo número for 0, o programa responde de forma
    amigável sem fechar inesperadamente.

3. Entrada de Dados (input() e float())

  - input(...): Lê o que o usuário digita no teclado. Qualquer coisa lida por
    padrão chega como texto (string).
  - float(...): Converte o texto digitado em um número decimal (com casas
    decimais). Se usássemos apenas input(), "5" + "5" resultaria em "55" (junção
    de textos), e não 10. O float garante que possamos calcular tanto números
    inteiros (ex: 2, 10) quanto quebrados (ex: 4.5, 3.14).

4. Controle de Fluxo (if, elif, else)

  - if opcao in ['1', '2', '3', '4']: Garante que o programa só pedirá os
    números se o usuário digitou uma opção válida.
  - elif (abreviação de else if): Permite testar várias condições em sequência
    ("se for 1 faz isso, senão se for 2 faz aquilo...").
  - else: É o caminho padrão caso nenhuma das condições anteriores seja atendida
    (ex: se o usuário digitar "9" ou uma letra).

5. Formatação de Texto (f-strings)

Ao usar um f antes das aspas (ex: f"Resultado: {num1} + {num2} = ..."), podemos
colocar variáveis diretamente dentro do texto usando chaves { }, tornando o
código mais legível e organizado.
