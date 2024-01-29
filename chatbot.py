from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criar instância do chatbot
chatbot = ChatBot("Meu Chatbot")

# Treinar o chatbot usando dados de treinamento pré-existentes
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese")

# Interagir com o chatbot
while True:
    pergunta = input("Você: ")
    resposta = chatbot.get_response(pergunta)
    print("Chatbot: ", resposta)