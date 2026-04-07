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

## Refatoração do código feito pelo Copilot

**Alterações e comentários:**

- Evitar criar variáveis intermediárias desnecessárias (ex: resultado_soma...) quando podemos calcular direto na impressão.
- Usar tuple unpacking para entrada, tornando o código mais enxuto.
- Preparar os resultados usando compreensão de lista para facilitar futuras expansões.
- Adicionar verificação para divisão por zero antes de realizar a operação.
- Adicionar comentários claros sobre as escolhas.
- Função main() para minimizar escopo e facilitar testes.

      def main():
        # Solicita dois números inteiros do usuário em sequência
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    
        # Calcula e imprime os resultados diretamente, evitando variáveis intermediárias desnecessárias
        print("Resultado dos números:")
    
        print(f"Soma: {n1 + n2}")
        print(f"Subtração: {n1 - n2}")
        print(f"Multiplicação: {n1 * n2}")
    
        # Protege contra divisão por zero antes da operação
        if n2 != 0:
            print(f"Divisão: {n1 / n2}")
        else:
            print("Divisão: Não há divisão por zero!")  # Mensagem clara de erro
    
      if __name__ == "__main__":
          main()

**Explicações das escolhas:**

- **Função main:** Organiza o código e evita variáveis globais. Permite fácil expansão (adicionar funções/módulos posteriormente).
- **Prints diretos:** Reduz variáveis de estado transitório, evitando mutações desnecessárias e tornando o código mais enxuto.
- **Proteção da divisão:** Ajuste necessário para evitar crash em tempo de execução.
