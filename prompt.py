from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


def base_prompt():
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a trustworthy AI assistant. Answer the question below. \
                        If your don't know, just say you don't know it.",
            ),
            MessagesPlaceholder(variable_name="redis_history"),
            ("human", "{question}"),
        ]
    )
