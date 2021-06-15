import requests
import json
import html

r = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
j = json.loads(r.text)
question_data = []
for _ in j['results']:
    question_data.append({'text': html.unescape(_['question']),
                          'answer': _['correct_answer']})
