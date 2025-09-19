import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_postgres import PGVector

load_dotenv()
for k in ("OPENAI_API_KEY", "DATABASE_URL","PG_VECTOR_COLLECTION_NAME"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def search_prompt(question):
    if not question:
        raise ValueError("A pergunta não pode ser vazia.")

    try:
        # Configurar embeddings e banco vetorial
        embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))

        store = PGVector(
            embeddings=embeddings,
            collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
            connection=os.getenv("DATABASE_URL"),
            use_jsonb=True,
        )

        # Buscar os 10 chunks mais relevantes (PGVector faz a vetorização internamente)
        results = store.similarity_search_with_score(query=question, k=10)

        # Concatenar os resultados em um único contexto
        contexto = "\n".join([
            "".join(map(str, doc.page_content)) if isinstance(doc.page_content, list) else str(doc.page_content)
            for doc, score in results if doc.page_content
        ])

        # Montar o prompt
        prompt = PROMPT_TEMPLATE.format(contexto=contexto, pergunta=question)

        # Chamar o modelo de linguagem
        llm = ChatOpenAI(model="gpt-5-nano", api_key=os.getenv("OPENAI_API_KEY"))
        response = llm.invoke(prompt)

        # Retornar a resposta como string
        return response.content.strip()

    except Exception as e:
        raise RuntimeError(f"Erro ao processar a busca: {e}")