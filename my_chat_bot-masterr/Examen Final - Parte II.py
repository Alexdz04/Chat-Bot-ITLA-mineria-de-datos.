import re
import random
from preguntas_itla import get_responses

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    recognized_words_count = sum(word in user_message for word in recognized_words)

    percentage = float(recognized_words_count) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    for resp in get_responses():
        response(*resp)

    best_match = max(highest_prob, key=highest_prob.get)
    #print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['me podrias especificar mejor tu pregunta?', 'no entiendo lo que me quieres decir', 'intenta buscarlo en google a ver que te dice',][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))