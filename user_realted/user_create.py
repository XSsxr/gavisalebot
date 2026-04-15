from db.db import add_waiting


def user_create_account(message, bot, user_tg_id, ios):
    text = (message.text or "").strip().lower()

    if text == "end":
        add_waiting(user_tg_id, ios)

    else:
        add_waiting(user_tg_id, ios, text)

    bot.send_message(message.chat.id, "Now just wait to be allowed to use this bot. Youll be notified")
    return


