import requests
import pprint

question_data = []
params = {
    'amount': '20',
    'type': 'boolean',
    'category': '9',
    'difficulty': 'medium'
}
fetch = requests.get('https://opentdb.com/api.php', params=params)

question_data = fetch.json()['results']


# pprint.pprint(question_data)


