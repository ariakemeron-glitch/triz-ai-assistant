import os
import asyncio
from dotenv import load_dotenv
from gigachat import GigaChat

load_dotenv()


def get_credentials():
    credentials = os.getenv("GIGACHAT_CREDENTIALS")

    if not credentials:
        try:
            import streamlit as st
            credentials = st.secrets.get("GIGACHAT_CREDENTIALS")
        except Exception:
            credentials = None

    if not credentials:
        raise ValueError("Не найден ключ GigaChat. Проверь настройки Secrets.")

    return credentials


def ask_gigachat(prompt):
    try:
        asyncio.get_event_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    credentials = get_credentials()

    with GigaChat(
        credentials=credentials,
        model="GigaChat-2",
        ca_bundle_file="russian_trusted_root_ca_pem.crt"
    ) as client:

        response = client.chat.create(prompt)
        message = response.messages[0].content

        if isinstance(message, list):
            return "".join(
                part.text or "" for part in message
                if hasattr(part, "text")
            )

        return str(message)
