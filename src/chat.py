from search import search_prompt

def main():
    chain = search_prompt  # Mantendo a referência à função `search_prompt`

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    print("Bem-vindo ao Chat de Busca Semântica!")
    print("Faça perguntas baseadas no conteúdo do PDF ingerido.")
    print("Digite 'sair' para encerrar o chat.\n")

    while True:
        # Solicitar pergunta do usuário
        question = input("PERGUNTA: ").strip()

        # Verificar se o usuário deseja sair
        if question.lower() == "sair":
            print("Encerrando o chat. Até mais!")
            break

        # Processar a pergunta usando a função search_prompt
        try:
            response = chain(question)
            print(f"RESPOSTA: {response}\n")
        except Exception as e:
            print(f"Erro ao processar a pergunta: {e}\n")

if __name__ == "__main__":
    main()