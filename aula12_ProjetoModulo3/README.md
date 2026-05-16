# Protótipo Low Code / No Code — Automação de E-mails

## Descrição do Desafio
Automatizar o envio de e-mails de confirmação sempre que um usuário preencher um formulário de contato.

## Plataformas Utilizadas
- **Make** (make.com)
- **Google Forms**
- **Google Sheets** (Banco de Dados)
- **Gmail** (para envio do e-mail)

## Protótipo

**Forms:** https://forms.gle/mpgSrA2XcvA8j3LT7

**Make:** https://us2.make.com/public/shared-scenario/9Fhp3hOTRc6/integration-google-sheets-gmail


Prints do funcionamento:
- Print 1: Cenário no Make com módulos conectados.
- Print 2: Formulário para envio dos dados.
- Print 3: Planilha com os dados para o e-mail.
- Print 4: E-mail recebido na caixa de entrada.

## Justificativa Técnica da Plataforma
O Make foi escolhido por ser gratuito, visual, intuitivo e especializado em automações de fluxo entre sistemas de forma simples. 
Para o desafio proposto (integrar Forms + Gmail), ele oferece conectores dos aplicativos prontos, o que permite criar e testar o protótipo em
pouco tempo de produção. Seria a escolha ideal para um projeto de curto prazo.


## Vantagens X Limitações do No-Code/Low-Code

**3 Vantagens:**

- Prototipagem rápida sem precisar programar.
- Redução de custo para validar ideias.
- Acessível para não-desenvolvedores criarem soluções reais, de forma fácil e simples.

**3 Limitações:**

- Dependência total da plataforma (se ela sair do ar, sua solução para).
- Difícil escalar ou customizar além do que a ferramenta permite com o plano gratuito.
- Migrar para outra solução ou até plataforma depois é trabalhoso.

## Reflexão Crítica

A principal limitação enfrentada foi o erro de autenticação [403] no módulo Gmail, causado por permissões insuficientes concedidas ao Make
durante a conexão inicial com o Google. A solução foi reconectar a conta concedendo todas as permissões solicitadas, incluindo a de envio de
e-mails. Isso evidencia uma limitação real das plataformas no-code: o usuário depende de fluxos de autorização de terceiros (OAuth) que podem
falhar silenciosamente, exigindo diagnóstico mesmo sem programar.

## Colaboração

O projeto foi realizado individualmente. Todas as etapas, como: discussão crítica, configuração do protótipo e documentação foram
desenvolvidas por mim mesmo, único integrante, o que exigiu maior autonomia na tomada de decisões técnicas e se tornando mais
trabalhoso. Mas serviu de grande aprendizado.
