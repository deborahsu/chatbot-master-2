"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import random

swear_words = ["asshole", "fuck", "fucking" "jerkoff", "shit", "silly", "dyke", "fag", "damn", "prick", "Whore", "twat",
               "goddamn"]
help_request = ["help", "need", "problem", "assistance", "support"]
bot_questions = [
    "what's your plans for the week-end?",
    "Where can I find a Zumba course?",
    "Where can I find a kick-boxing course?",
    "How can you increase your salary?",
    "I want to laugh, tell me a joke?",
    "ask me the weather?",
    "Which bus for Netanya?",
    "Ask me a joke?",
    "how much is the euro change today?"
]


@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    animation, msg = get_Bot_Answer(user_message)
    return json.dumps({"animation": animation, "msg": msg})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)


def is_swear_word(user_msg):
    user_msg_array = user_msg.split()
    if any(word in user_msg_array for word in swear_words):
        return True
    else:
        return False


def is_help_request(user_msg):
    user_msg_array = user_msg.split()
    if any(word in user_msg_array for word in help_request):
        return True
    else:
        return False


def get_Bot_Answer(user_msg):
    user_msg_array = user_msg.split()
    user_name = user_msg_array[-1]
    if "name" in user_msg_array and "is" in user_msg_array:
        return "inlove", "Hello {0}, nice to meet you. How can I help you ?".format(user_name)
    elif user_msg == "how are you?" or user_msg == "what's up?":
        return "giggling", "I am fine and you? How can I help you?"
    elif is_swear_word(user_msg):
        return "heartbroke", "please, be polite. I'm trying to help you"
    elif is_help_request(user_msg):
        return "waiting", "ok.How I can help you?"
    elif "weather" in user_msg_array:
        return "excited", "Tel aviv is always sunny my dear"
    elif "change" in user_msg_array:
        return "money", "less than 4.0, bassa"
    elif "salary" in user_msg_array:
        return "money", "work more, ahahahaa!"
    elif "week-end" in user_msg_array:
        return "takeoff", "beach and tequila. I guess you'll spend yours on Python lecture, ahahah!"
    elif "boxing" in user_msg_array:
        return "afraid", "Next course is in Yaffo Tel-Aviv in 2 hours. Everybody is already in panic there to know that " \
                         "to know that you are on your way "
    elif "bus" in user_msg_array or "where" in user_msg_array:
        return "takeoff", "download Moovit and Google Maps and you'll have all your answers"
    elif "zumba" in user_msg_array:
        return "dancing", "Next course is in Namal Tel-Aviv in 1 hour"
    elif "thank you" in user_msg_array:
        return "ok", "you're welcome!"
    elif "joke" in user_msg_array:
        return "laughing", "What is the difference between a Friend and a Best Friend? A friend: Wow, you are so pretty." \
                           " Best Friend: Shrek called, he wants his face back."
    elif len(user_msg_array)== 1:
        return "confused", "please be more specific, write a sentence or a question to help me to understand"
    elif user_msg.startswith("Do you"):
        return "confused", "I cannot answer your question, i am so sorry..."
    else:
        return "confused", "I am afraid that I am not so advanced to provide you with some assistance. " \
                           "But ask me anything else, for example: " + random.choice(bot_questions)


if __name__ == '__main__':
    main()
