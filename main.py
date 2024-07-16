import os
from langchain.chat_models import ChatOpenAI
from langchain.memory.chat_message_histories import RedisChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from fastapi import FastAPI
from prompt import base_prompt


app = FastAPI()


@app.get("/chat/completions/user_id/{user_id}")
def chat_completions(user_id: str, question: str):
    model = ChatOpenAI(model_name="gpt-4o")
    template = base_prompt()

    chain = template | model
    chain_with_redis_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: RedisChatMessageHistory(
            session_id, url=os.getenv("REDIS_URL")
        ),
        input_messages_key="question",
        history_messages_key="redis_history",
    )
    return chain_with_redis_history.invoke(
        {"question": question},
        config={"configurable": {"session_id": user_id}},
    )
