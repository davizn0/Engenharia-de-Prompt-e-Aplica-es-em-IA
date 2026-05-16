# Projeto Final Low Code/No Code — Automação de E-mails

## 📌 Desafio Escolhido

Automatizar o envio de e-mails de confirmação sempre que um usuário preencher um formulário de contato online, sem escrever nenhuma linha de código. O fluxo integra Google Forms → Google Sheets → Google Gemini (IA) → Gmail, disparando uma mensagem personalizada e inteligente automaticamente a cada nova resposta.

---

## 🖥️ Protótipo

- Print 1: Cenário no Make com os módulos Google Sheets, Google Gemini, Router e Gmail conectados.
- Print 2: Log de execução com sucesso (módulos em verde).
- Print 3: E-mail padrão recebido na caixa de entrada com resposta gerada pela IA.
- Print 4: E-mail urgente recebido ao enviar mensagem contendo a palavra "urgente".
- Print 5: Planilha de histórico de atendimentos preenchida automaticamente.

> Arquivos de imagem disponíveis na pasta `/docs`.

**Como o protótipo funciona:**

1. O usuário preenche o Google Forms com nome, e-mail e mensagem.
2. A resposta é registrada automaticamente em uma planilha Google Sheets.
3. O Make detecta a nova linha na planilha via módulo "Watch New Rows".
4. O Google Gemini lê a mensagem e gera uma resposta de e-mail personalizada em português.
5. Um Router analisa o conteúdo da mensagem:
   - Se contiver a palavra **"urgente"** → dispara e-mail prioritário com aviso de resposta em até 2 horas.
   - Caso contrário → dispara e-mail padrão com a resposta gerada pela IA.
6. Todo o atendimento é registrado automaticamente em uma planilha de histórico.

---

## ⚙️ Plataforma Utilizada

- **Make** (make.com) — orquestração do fluxo de automação
- **Google Forms** — coleta das respostas do usuário
- **Google Sheets** — gatilho da automação (Watch New Rows) e registro do histórico
- **Google Gemini (AI Studio)** — geração de respostas personalizadas por IA
- **Gmail** — envio dos e-mails de confirmação

**Justificativa da escolha:**

O Make foi escolhido por oferecer plano gratuito funcional, interface visual intuitiva e conectores nativos para todo o ecossistema Google (Forms, Sheets, Gemini e Gmail), sem necessidade de código. O Google Gemini foi adotado como motor de IA por ser gratuito via AI Studio, integrar-se nativamente ao Make e eliminar problemas de autenticação que surgiram com APIs externas (como OpenAI e Groq via HTTP). Para um desafio de automação com prazo curto e sem infraestrutura própria, essa combinação de ferramentas representa a escolha ideal para prototipagem rápida.

---

## ✅ Vantagens Identificadas

1. **Prototipagem rápida:** o cenário completo, incluindo IA e filtros condicionais, foi configurado em poucas horas sem escrever nenhuma linha de código.
2. **Integração nativa no ecossistema Google:** Forms, Sheets, Gemini e Gmail funcionam de forma plug-and-play dentro do Make, eliminando configurações complexas de autenticação.
3. **Respostas inteligentes e personalizadas:** o Google Gemini gera respostas únicas para cada mensagem recebida, tornando o atendimento automatizado mais humano e relevante.
4. **Triagem automática por urgência:** o Router com filtro condicional classifica as mensagens e direciona e-mails diferentes conforme a prioridade, sem intervenção manual.
5. **Histórico automático de atendimentos:** cada interação é registrada em uma planilha, criando um banco de dados de atendimentos sem esforço adicional.

---

## ⚠️ Limitações Encontradas

1. **Dependência de múltiplas plataformas:** o fluxo depende simultaneamente do Make, Google Forms, Sheets, Gemini e Gmail. Uma instabilidade em qualquer um desses serviços interrompe toda a automação.
2. **Filtro condicional frágil:** o Router detecta a palavra "urgente" apenas em letras minúsculas. Variações como "URGENTE" ou "Urgente" não seriam capturadas sem ajustes adicionais no filtro.
3. **Custo variável da IA em escala:** o Google Gemini é gratuito dentro dos limites do plano, mas em volumes altos de mensagens pode gerar custos ou limitações de requisições por minuto.
4. **Risco de lock-in tecnológico:** toda a lógica de automação está construída dentro do Make. Migrar para outra plataforma exigiria reconfigurar todos os módulos do zero.
5. **Controle de segurança reduzido:** os dados dos usuários (nome, e-mail, mensagem) trafegam por servidores de terceiros (Make, Google), o que levanta questões de privacidade e conformidade com a LGPD em contextos empresariais reais.

---

## 📚 Reflexão Crítica

O desenvolvimento do protótipo evidenciou de forma prática as limitações reais das plataformas no-code. A principal dificuldade enfrentada foi a integração com APIs de IA externas (OpenAI e Groq) via módulo HTTP do Make, que gerou erros consecutivos de autenticação (403 e 429) relacionados a permissões insuficientes, créditos esgotados e problemas no envio de headers. A solução criativa adotada foi migrar para o Google Gemini, que possui conector nativo no Make e eliminou todos os problemas de autenticação, demonstrando que a escolha da ferramenta certa é tão importante quanto a solução em si.

O filtro condicional por palavra-chave, embora funcional, revelou outra limitação: sistemas baseados em regras simples são frágeis diante da variabilidade da linguagem humana. Uma evolução natural seria substituir o filtro por uma classificação feita pela própria IA, tornando a triagem mais robusta e inteligente.

No geral, o projeto demonstrou que plataformas no-code permitem construir soluções funcionais e sofisticadas rapidamente, mas exigem pensamento crítico na escolha das ferramentas, no tratamento de erros e no planejamento de escalabilidade.

---

## 👥 Colaboração

O projeto foi desenvolvido em dupla, com divisão de responsabilidades da seguinte forma:

| Integrante | Responsabilidades |
|---|---|
| **FULANO** | Configuração do Google Forms e Google Sheets; testes de envio de formulário e validação dos e-mails recebidos. |
| *(seu nome aqui)* | Configuração do cenário no Make; integração com Google Gemini; configuração do Router e filtros condicionais; documentação no GitHub. |

A comunicação foi contínua durante toda a atividade, com decisões técnicas tomadas em conjunto, especialmente na escolha da plataforma de IA após os erros encontrados com OpenAI e Groq.

---

## 📝 Registro da Aula

Data: **11/05/2026**
Atividade: Discussão crítica + mini-projeto de aplicação
Local: Laboratório de informática / Quadro branco
Professor(a): Kadidja Valéria

---

## 🚀 Próximos Passos

- Substituir o filtro de palavras-chave por uma classificação feita pelo próprio Gemini, tornando a triagem de urgência mais inteligente e robusta.
- Adicionar um painel de controle em Google Sheets com gráficos automáticos de volume de atendimentos por dia, tipo e tempo de resposta.
- Integrar um módulo de validação de e-mail antes do envio para evitar falhas por endereços inválidos.
- Evoluir o protótipo para um sistema completo de atendimento ao cliente como proposta para o Projeto Final da Unidade 3, incluindo categorização automática de mensagens, respostas por tipo de solicitação e relatório semanal automatizado.
