# Refatoração de uma Calculadora Simples

## Base do código
  
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    resultado_soma = n1 + n2
    resultado_subtracao = n1 - n2
    resultado_multiplicacao = n1 * n2
    resultado_divisao = n1 / n2
    
    print("Resultado dos números:")
    print(f"{resultado_soma}")
    print(f"{resultado_subtracao}")
    print(f"{resultado_multiplicacao}")
    print(f"{resultado_divisao}")

## Refatoração do código feito pela IA

Refatorei o código da sua calculadora para focar em performance e evitar mutações de estado desnecessárias. 

**As alterações incluem:**

- **Encapsulamento em uma função calculadora_basica():** Melhora a modularidade e organização do código.
- **Uso de float(input())**: Permite cálculos com números decimais, tornando a calculadora mais versátil.
- **Cálculo e impressão diretos:** Em vez de armazenar cada resultado em uma variável intermediária (como resultado_soma), o cálculo é feito diretamente dentro do print(). Isso reduz a criação de variáveis que seriam usadas apenas uma vez, minimizando mutações de estado desnecessárias.
- **Verificação de divisão por zero:** Adiciona robustez ao prevenir erros em caso de divisão por zero.
Tratamento de erros try-except: Melhora a experiência do usuário ao lidar com entradas não numéricas.

      def calculadora_basica():
          """
          Calculadora básica que realiza soma, subtração, multiplicação e divisão.
          Evita mutação de estado desnecessária ao calcular e imprimir os resultados
          diretamente, sem armazená-los em variáveis intermediárias que não seriam
          reutilizadas.
          """
          try:
              # Converte a entrada para float para permitir números decimais
              n1 = float(input("Digite o primeiro número: "))
              n2 = float(input("Digite o segundo número: "))
      
              print("\nResultado dos números:")
      
              # Soma: cálculo e impressão diretos
              print(f"Soma: {n1 + n2}")
      
              # Subtração: cálculo e impressão diretos
              print(f"Subtração: {n1 - n2}")
      
              # Multiplicação: cálculo e impressão diretos
              print(f"Multiplicação: {n1 * n2}")
      
              # Divisão: verifica se o segundo número é zero antes de dividir
              if n2 != 0:
                  print(f"Divisão: {n1 / n2}")
              else:
                  print("Divisão: Não é possível dividir por zero.")
          except ValueError:
              # Captura erros de entrada inválida (não numérica)
              print("Entrada inválida. Por favor, digite números válidos.")
      
      # Chama a função da calculadora
      calculadora_basica()

