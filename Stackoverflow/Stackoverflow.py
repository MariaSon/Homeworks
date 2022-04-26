import requests

url = 'https://api.stackexchange.com/2.3/questions?fromdate=1650758400&todate=1650931200&order=desc&sort=activity&tagged=python&site=stackoverflow'
python_questions = requests.get(url).json()['items']
for questions in python_questions:
    for k, v in questions.items():
        if k == 'title':
            print(f'Вопрос с тегом "python" - {v}')
