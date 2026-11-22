import os
from dotenv import load_dotenv
from gigachat import GigaChat


load_dotenv()


def ask_gigachat(prompt):
    credentials = os.getenv("GIGACHAT_CREDENTIALS")

    if not credentials:
        raise ValueError(
            "Не найден ключ GigaChat. Проверь файл .env"
        )

    with GigaChat(
        credentials=credentials,
        model="GigaChat"
    ) as client:

        response = client.chat.create(prompt)

        return response.messages[0].content[0].text