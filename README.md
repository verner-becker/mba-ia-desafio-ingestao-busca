# Desafio MBA IA - Ingestão e Busca Semântica

Sistema de ingestão e busca semântica desenvolvido com LangChain e PostgreSQL + pgVector para o MBA em Engenharia de Software com IA da Full Cycle.

## 📋 Objetivo

Este software é capaz de:

- **Ingestão**: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão pgVector
- **Busca**: Permitir que o usuário faça perguntas via linha de comando (CLI) e receba respostas baseadas apenas no conteúdo do PDF

## 🛠 Tecnologias Utilizadas

- **Linguagem**: Python 3.12+
- **Framework**: LangChain
- **Banco de Dados**: PostgreSQL + pgVector
- **Containerização**: Docker & Docker Compose
- **LLM**: OpenAI GPT-5-nano
- **Embeddings**: OpenAI text-embedding-3-small

## 📋 Pré-requisitos

- Python 3.12 ou superior
- Docker e Docker Compose
- Conta OpenAI com API Key

## ⚙️ Configuração do Ambiente

### 1. Clone o repositório e navegue até a pasta
```bash
git clone <seu-repositorio>
cd mba-ia-desafio-ingestao-busca
```

### 2. Crie e ative o ambiente virtual Python
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Copie o arquivo `.env.example` para `.env` e configure suas variáveis:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:
```env
OPENAI_API_KEY=sua_api_key_aqui
DATABASE_URL=postgresql://user:password@localhost:5432/vectordb
PG_VECTOR_COLLECTION_NAME=document_chunks
OPENAI_EMBEDDING_MODEL=text-embedding-3-small
PDF_PATH=./document.pdf
```

## 🚀 Execução do Projeto

Execute os comandos na ordem exata abaixo:

### 1. Iniciar o banco de dados
```bash
docker compose up -d
```

### 2. Executar a ingestão do PDF
```bash
python src/ingest.py
```

### 3. Iniciar o chat interativo
```bash
python src/chat.py
```

## 📁 Estrutura do Projeto

```
├── docker-compose.yml          # Configuração do PostgreSQL + pgVector
├── requirements.txt            # Dependências Python
├── .env.example               # Template das variáveis de ambiente
├── src/
│   ├── ingest.py              # Script de ingestão do PDF
│   ├── search.py              # Lógica de busca semântica
│   ├── chat.py                # Interface CLI para chat
├── document.pdf               # PDF para ingestão
└── README.md                  # Este arquivo
```

## 💬 Exemplos de Uso

Após executar `python src/chat.py`, você pode fazer perguntas:

```
Faça sua pergunta:

PERGUNTA: Qual o faturamento da Empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhões de reais.

---

PERGUNTA: Quantos clientes temos em 2024?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.

Digite 'sair' para encerrar.
```

## 🔧 Como Obter a API Key da OpenAI

1. Acesse [platform.openai.com](https://platform.openai.com)
2. Faça login ou crie uma conta
3. Vá em "API Keys" no menu lateral
4. Clique em "Create new secret key"
5. Copie a chave e adicione no arquivo `.env`

## ❓ Solução de Problemas

### Erro de conexão com o banco
```bash
# Verifique se o container está rodando
docker ps

# Se não estiver, inicie novamente
docker compose up -d
```

### Erro de API Key
- Verifique se a API Key está correta no arquivo `.env`
- Confirme se você tem créditos na conta OpenAI

### Erro de dependências
```bash
# Reinstale as dependências
pip install -r requirements.txt --force-reinstall
```

### PDF não encontrado
- Certifique-se de que o arquivo `document.pdf` está na raiz do projeto
- Verifique se o caminho no `.env` está correto

## 🔄 Para Reiniciar o Sistema

```bash
# Parar containers
docker compose down

# Limpar dados (se necessário)
docker compose down -v

# Reiniciar
docker compose up -d
python src/ingest.py
python src/chat.py
```