import openai

openai.api_key = "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"

# Função para gerar texto a partir do modelo de linguagem
def gerar_texto(texto):

    response = openai.Completion.create(
    # Modelo usado
    engine = "text-ada-001",

    # Texto inicial da conversa
    prompt = texto,

    # Comprimento das respostas
    max_tokens = 150,

    # QUantas conclusões gerar para cada prompt
    n = 5,

    # O texto retornado não conterá a sequência de parada
    stop = None,

    # Medida da aletoriedade de um texto gerado pelo modelo. (Valor entre 0 e 1)
    temperature = 0.8,
    )

    return response.choices[0].text.strip()

# Função principal
def main():
    print('\n Bem vindo ao projeto Chatbot')
    print('Digite sair para encerrar o chat')

    while True:
        # Coleta a pergunta
        user_message = input('\nVocê: ')

        if user_message.lower() == 'sair':
            break
    
        # Coloca a mensagem digitada pelo usuário na variável Python chamada gpt4_prompt
        gpt4_prompt = f"\nUsuário: {user_message}\nChatbot: "

        # Obtem a resposta do modelo execultando a função gera_texto
        chatbot_response = gerar_texto(gpt4_prompt)

        # Imprime a resposta do chatbot
        print(f"Chatbot: {chatbot_response}")


if __name__ == '__main__':
    main()