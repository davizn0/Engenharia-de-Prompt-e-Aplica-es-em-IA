# Código de média de alunos
### Feito por mim

    nota1 = float(input("Qual é a primeira nota do aluno? "))
    nota2 = float(input("Qual é a segunda nota do aluno? "))
    
    media = (nota1 + nota2) / 2
    
    print(f"A média do aluno é {media}")
    
    if media >= 6:
      print("O aluno está aprovado!")
    else:
      print("O aluno está reprovado!")

### Versão Neutra (IA)

Com certeza! Esse é um clássico para quem está começando. A lógica é simples: somamos todas as notas e dividimos pela quantidade de notas inseridas.

Vou te apresentar um exemplo funcional em Python, que é uma das linguagens mais legíveis para esse tipo de tarefa.

    # Definindo as notas em uma lista
    notas = [7.5, 8.0, 6.5, 9.0]
    
    # Calculando a média
    # A função sum() soma os valores e len() conta quantos itens existem
    media = sum(notas) / len(notas)
    
    # Exibindo o resultado
    print(f"A média do aluno é: {media:.2f}")
    
    # Verificando a situação
    if media >= 7.0:
        print("Situação: Aprovado!")
    else:
        print("Situação: Reprovado.")

### Versão Persona (IA)

"Olha, eu normalmente não saio do meu terminal para explicar o "Hello World" da aritmética,
mas já que você pediu (e parece que o Stack Overflow não foi suficiente para você hoje), vamos lá.

Calcular uma média é algo que até um estagiário no primeiro dia deveria fazer de olhos fechados.
Se você quer algo que realmente funcione e não apenas um script "sujo", você usa Python pela legibilidade
ou JavaScript se estiver preso no navegador.

Aqui está a solução em Python, escrita de uma forma que você não passe vergonha:"


    def calcular_media(notas):
        # Validar se a lista não está vazia para não causar um ZeroDivisionError. 
        # Coisas que iniciantes sempre esquecem.
        if not notas:
            return 0.0
        
        return sum(notas) / len(notas)
    
    # Exemplo de uso com notas reais
    notas_aluno = [8.5, 7.0, 9.2, 6.0]
    media = calcular_media(notas_aluno)
    
    # Formatação limpa. Ninguém quer ver 15 casas decimais.
    print(f"Média final: {media:.1f}")
    
    # Uma lógica de corte básica, porque o mundo é cruel.
    status = "Aprovado" if media >= 7 else "Reprovado"
    print(f"Status: {status}")

### Versão Restritiva (IA)

    def calcular_media(notas):
        if not notas:
            return 0.0
        return sum(notas) / len(notas)
    
    notas_aluno = [8.5, 7.0, 9.2, 6.0]
    media = calcular_media(notas_aluno)
    
    print(f"Média: {media:.2f}")
    print("Status: Aprovado" if media >= 7 else "Status: Reprovado")

# Resultados

### Versão Neutra (IA)

O cálculo matemático está correto e todos funcionam normalmente. O código tem poucos textos/comentários, apenas os necessários para
explicar cada linha. Inclui explicações e comentários no código, o que não foi solicitado, mas mesmo assim aparece para melhor
compreensão do usuário. Não comenteu erros para manter um personagem, pois não foi solicitado nenhum personagem.

### Versão Persona (IA)

O cálculo matemático está correto e todos funcionam normalmente. O código tem textos/comentários que não foram solicitados, sendo
desnecessário para o usuário e gastando a "energia" da IA desenecessariamente. Inclui textos não solicitados e não cometeu erros
por manter o personagem. Mas por ser tratar de código, tem baixa probabilidade de ter erros.

### Versão Restritiva (IA)

O cálculo matemático está correto e todos funcionam normalmente. O código nao possui textos/comentários sendo limpo, pois foi 
solicitado para não ter ter nenhum dos mesmos. Não foi comentidos erros, podendo ter apenas o código limpo e rodando perfeitamente.
