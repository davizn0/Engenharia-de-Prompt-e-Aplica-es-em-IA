# Desafio: Transformar uma instrução vaga em um Prompt Mestre estruturado.

## Código simples e resposta ruim da IA:

### Pergunta:

    def desconto(a, b):
      x = a * b
      y = x / 100
      z = a - y
      print("O valor e:")
      print(z)
      return z


    desconto(100, 10)
    desconto(250, 20)



Melhore isso.

### Resposta:

1. Nomes Semânticos e Clareza
Substituímos as letras por nomes que explicam o que o dado representa. Também simplificamos a conta matemática: subtrair uma porcentagem é o mesmo que multiplicar pelo fator restante (ex: tirar 10% é o mesmo que multiplicar por 0.90).

Python

    def calcular_desconto(preco, percentual):
      
      desconto = preco * (percentual / 100)
      
      preco_final = preco - desconto
    
      # Usando f-strings para uma saída mais elegante
      print(f"Preço original: R$ {preco:.2f} | Desconto: {percentual}% | Total: R$ {preco_final:.2f}")
    
      return preco_final

    # Testes
    calcular_desconto(100, 10)
    calcular_desconto(250, 20)

##  Equação do Prompt (Persona + Contexto + Restrições + Formato).

### Pergunta:


        def desconto(a, b):
        
          x = a * b
          
          y = x / 100
          
          z = a - y
          
          print("O valor e:")
          
          print(z)
          
          return z
    
    
        desconto(100, 10)
        
        desconto(250, 20)

Você é um Engenheiro de Software Sênior com 10 anos de experiência em Python.  Este código faz parte do motor de cálculo de um e-commerce em expansão. O código atual é difícil de ler, não possui validações e mistura lógica de cálculo com exibição (IO), o que impede testes automatizados eficazes. Refatore a função desconto(a, b) para torná-la profissional, robusta e documentada. Use Type Hints para definir que as entradas e a saída são números decimais (float), adicione uma Docstring detalhada explicando o que a função faz, seus parâmetros e o que ela retorna, remova os comandos print de dentro da função (ela deve apenas processar dados e retornar o valor) e adicione uma verificação simples para garantir que o desconto não seja negativo ou superior a 100%. Entregue a resposta final em Markdown estruturado: Um bloco com o código refatorado e uma seção chamada "Dívida Técnica" em formato YAML listando os 3 principais problemas do código original que foram corrigidos.

### Resposta:

Como Engenheiro de Software Sênior, recebo esse código como um "Code Smell" clássico de início de projeto que precisa de maturidade para escalar. Para um e-commerce em expansão, precisamos de previsibilidade, testabilidade e semântica.

Abaixo, apresento a refatoração seguindo as PEPs (Python Enhancement Proposals) e boas práticas de Clean Code.

**Código Refatorado**


Python


      def calcular_preco_com_desconto(preco_base: float, percentual_desconto: float) -> float:
          """
          Calcula o valor final de um produto aplicando um desconto percentual.
      
          A função valida se o percentual de desconto está dentro do intervalo aceitável 
          (0% a 100%) para evitar erros de lógica financeira no checkout.
      
          Args:
              preco_base (float): O valor original do produto antes do desconto.
              percentual_desconto (float): O valor da porcentagem de desconto (ex: 10 para 10%).
      
          Returns:
              float: O preço final após a dedução, arredondado para duas casas decimais.
      
          Raises:
              ValueError: Se o percentual de desconto for negativo ou superior a 100%.
          """
          if not (0 <= percentual_desconto <= 100):
              raise ValueError("O percentual de desconto deve estar entre 0 e 100.")
      
          if preco_base < 0:
              raise ValueError("O preço base não pode ser negativo.")
      
          fator_desconto = percentual_desconto / 100
          valor_final = preco_base * (1 - fator_desconto)
          
          return round(valor_final, 2)

**Exemplo de uso profissional com tratamento de exceções**

      if __name__ == "__main__":
          casos_teste = [(100, 10), (250, 20)]
          
          for preco, desc in casos_teste:
              try:
                  resultado = calcular_preco_com_desconto(preco, desc)
                  print(f"Sucesso: Preço final calculado: R$ {resultado}")
              except ValueError as e:
                  print(f"Erro de validação: {e}")


**YAML**


    divida_tecnica_corrigida:
      - problema_1:
          titulo: "Nomes de Variáveis Não Semânticos"
          descricao: "O uso de 'a, b, x, y, z' obscurece a intenção do código. Substituído por nomes que descrevem o domínio do negócio                 (preco_base, valor_final)."
      - problema_2:
          titulo: "Acoplamento de IO (Entrada/Saída)"
          descricao: "A função original possuía 'print()' interno. Isso impede testes unitários limpos e polui logs de produção. A lógica foi isolada apenas para retorno de dados."
      - problema_3:
          titulo: "Ausência de Contratos e Validações"
          descricao: "Não havia checagem de tipos (Type Hints) nem limites lógicos. Um desconto de 110% resultaria em preço negativo, o que foi mitigado com Raising de Exceptions."
    Dica de Sênior: Em um cenário de produção real, eu recomendaria o uso do tipo Decimal da biblioteca padrão do Python em vez de float para lidar com dinheiro, evitando erros de precisão de ponto flutuante.
