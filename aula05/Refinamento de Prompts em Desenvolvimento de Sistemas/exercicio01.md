# 1. Abordagens de Prompt
### Prompt Inicial (Vago)

**"Crie um código em Python para calcular a soma de números."**

### Resultado

    # Definindo os números
    numero1 = 10
    numero2 = 5
    
    # Calculando a soma
    soma = numero1 + numero2
    
    # Exibindo o resultado
    print(f"A soma de {numero1} e {numero2} é: {soma}")

### Prompt Refinado (Detalhado)

**"Crie um código em Python que receba uma lista de números inteiros como entrada e retorne a soma.
Inclua comentários explicativos em cada etapa e valide se a lista está vazia antes de calcular."**

### Resultado

    def calcular_soma_lista(numeros):
        """
        Recebe uma lista de inteiros e retorna a soma total.
        """
        
        # 1. Validação: Verifica se a lista está vazia
        # Em Python, listas vazias são avaliadas como False
        if not numeros:
            return "Erro: A lista está vazia. Não é possível calcular a soma."
    
        # 2. Inicialização da variável acumuladora
        soma_total = 0
    
        # 3. Iteração: Percorre cada item da lista
        for numero in numeros:
            # Soma o valor atual ao acumulador
            soma_total += numero
    
        # 4. Retorno do resultado final
        return soma_total
    
    # --- Exemplos de Uso ---
    
    # Caso com lista preenchida
    minha_lista = [10, 25, 30, 5, 10]
    resultado = calcular_soma_lista(minha_lista)
    print(f"Resultado da soma: {resultado}")
    
    # Caso com lista vazia
    lista_vazia = []
    resultado_erro = calcular_soma_lista(lista_vazia)
    print(f"Teste lista vazia: {resultado_erro}")

### Conclusão

   O refinamento do prompt transforma um código comum em uma ferramenta profissional. Enquanto o pedido vago gera um cálculo fixo e sem utilidade real, o pedido detalhado cria uma função capaz de somar qualquer lista de números enviada pelo usuário. A principal melhoria está na segurança e na clareza. O código refinado não "trava" se a lista estiver vazia, pois ele aprende a verificar os dados antes de calcular. Além disso, com a inclusão de comentários, qualquer pessoa consegue entender a lógica sem esforço.
