# Projeto Final Low Code/No Code — Automação de E-mails


## Participantes
- Davi Lucas de Oliveira Sousa (45845531)
- Lorruan Pereira Soares (45886466)


## Desafio Escolhido

Automatizar o envio de e-mails de confirmação sempre que um usuário preencher um formulário de contato online, sem escrever nenhuma linha de código. O fluxo integra Google Forms, Google Sheets, Google Gemini e Gmail, disparando uma mensagem personalizada e inteligente automaticamente a cada nova resposta.


## Plataformas Utilizadas
- **Make**
- **Google Forms**
- **Google Sheets** (Banco de Dados)
- **Gemini**
- **Gmail**


## Protótipo

**Forms:** https://forms.gle/w6sriwgHkjqUK9Ui9

**Make:** https://us2.make.com/public/shared-scenario/9Fhp3hOTRc6/integration-google-sheets-gmail

Prints do funcionamento:
- Print 1: Cenário no Make com módulos conectados, com a IA integrada.
- Print 2: Formulário para envio dos dados.
- Print 3: Planilha com os dados para o e-mail.
- Print 4: E-mail recebido na caixa de entrada, com a resposta gerada por IA.


**Como o protótipo funciona:**

1. O usuário preenche o Google Forms com nome, e-mail e mensagem.
2. A resposta é registrada automaticamente em uma planilha Google Sheets.
3. O Make é processado no cenário, lê todas as últimas respostas realizadas e gravadas no Google Sheets.
4. O Google Gemini lê a mensagem e gera uma resposta de e-mail personalizada.
5. Uma condição gera o conteúdo da mensagem:
   - Se contiver a palavra **"urgente"**: dispara e-mail prioritário com aviso de resposta que demonstra aviso e urgência na resposta.
   - Caso contrário: dispara e-mail padrão com a resposta gerada pela IA.
6. Todo o atendimento é registrado automaticamente em uma planilha de histórico.


## Justificativa da Plataforma Make

O Make foi escolhido por ser gratuito, visual, intuitivo e especializado em automações de fluxo entre sistemas de forma simples. 
Para o desafio proposto (integrar uma IA + Forms + Excel + Gmail), ele oferece conectores dos aplicativos prontos, o que permite criar
e testar o protótipo em pouco tempo de produção. Seria a escolha ideal para um projeto de curto prazo.


## Vantagens

1. **Prototipagem rápida:** o cenário completo, incluindo IA e filtros condicionais, foi configurado em poucas horas sem escrever nenhuma linha de código.
2. **Integração de várias plataformas do Google:** Forms, Sheets, Gemini e Gmail funcionam de forma plug-and-play dentro do Make, eliminando configurações complexas de autenticação.
3. **Respostas inteligentes e personalizadas:** o Google Gemini gera respostas únicas para cada mensagem recebida, tornando o atendimento automatizado mais humano e relevante.
4. **Triagem automática por urgência:** O filtro condicional classifica as mensagens e direciona e-mails diferentes conforme a prioridade, sem intervenção manual.


## Limitações

1. **Dependência de múltiplas plataformas:** o fluxo depende simultaneamente do Make, Google Forms, Sheets, Gemini e Gmail. Uma instabilidade em qualquer um desses serviços interrompe toda a automação.
2. **Filtro condicional:** O filtro condicional detecta a palavra "urgente" apenas em letras minúsculas. Variações como "URGENTE" ou "Urgente" não seriam capturadas sem ajustes adicionais no filtro.
3. **Custo da IA:** o Google Gemini é gratuito dentro dos limites do plano, mas em volumes altos de mensagens pode gerar custos ou limitações de requisições por minuto.
4. **Controle de segurança:** os dados dos usuários (nome, e-mail, mensagem) trafegam por servidores de terceiros (Make, Google), o que levanta questões de privacidade e conformidade com a LGPD em contextos empresariais reais.


## Reflexão Crítica

O desenvolvimento do protótipo evidenciou de forma prática as limitações reais das plataformas no-code. A principal dificuldade enfrentada foi a integração com APIs de IA externas (OpenAI e Groq) via módulo HTTP do Make, que gerou erros consecutivos relacionados a permissões insuficientes, créditos esgotados e problemas no envio de informações. A solução adotada após pesquisas foi migrar para o Google Gemini, que possui conector nativo no Make e eliminou todos os problemas de autenticação, demonstrando que a escolha da ferramenta certa é tão importante quanto a solução em si. No geral, o projeto demonstrou que plataformas no-code permitem construir soluções funcionais e sofisticadas rapidamente, mas exigem pensamento crítico na escolha das ferramentas, no tratamento de erros e no planejamento de escalabilidade.


## Colaboração

O projeto foi desenvolvido em dupla, com divisão de responsabilidades da seguinte forma:

- **Lorruan:** Configuração do Google Forms e Google Sheets e testes de envio de formulário.
- **Davi:** Configuração do cenário no Make, integração com Google Gemini, configuração dos filtros condicionais e documentação no GitHub.

A comunicação foi contínua durante toda a atividade, com decisões técnicas tomadas em conjunto, especialmente na escolha da plataforma de IA após os erros encontrados com OpenAI e Groq.
