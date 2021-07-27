import requests
import html


def get_quiz_data():
    r = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
    json_data = r.json()
    question_data = []
    for record in json_data['results']:
        question_data.append({'text': html.unescape(record['question']),
                              'answer': record['correct_answer']})
    return question_data


data = get_quiz_data()
