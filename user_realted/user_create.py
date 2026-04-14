def user_create_account(message,bot,user_tg_id):
    text = message.text
    if ',' in text:
        text_soi = text.split(",",1)[0].strip()
        text_rest = text.split(",",1)[1].strip()
        if text_soi == 's' or 'i':


