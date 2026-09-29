from chat_history import create_session, save_message, get_messages

session_id = "test123"

create_session(session_id)

save_message(
    session_id,
    "user",
    "My name is Siddique"
)

save_message(
    session_id,
    "assistant",
    "Nice to meet you!"
)

messages = get_messages(session_id)

print(messages)