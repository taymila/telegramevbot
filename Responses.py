from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi"):
        return "Hi, how may I help today \n here are some options:"

    if user_message in ("what are you", "who are you?"):
        return "I am ChargeEV Bot, a Bot created to provide you with dedicated support"

    if user_message in ("time", "time now"):
        now = datetime.now()
        date_time = now.strftime("%d/$m, %H:%M")

        return str(date_time)

    return "Could you rephrase that?"