"""
Python program that asks the user to enter the ID of a question in the
command line. Then, the program returns the correct answer for that
question.
"""

import requests

url = 'https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json'

def data_getter():
    """json data load function"""

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')
        return {}

    return data


def answer_getter(data):
    """function to get all the correct answers"""

    correct_answers = {}
    for quiz in data['quizzes']:
        for question in quiz['questions']:
            for choice, answer in question['choices'].items():
                if answer == True:
                    correct_answers[str(question['id'])] = choice

    return correct_answers


if __name__ == '__main__':

    correct_answers = {}
    
    while True:
        question_id = input('Enter the question id: ')
        if question_id:
            break

    data = data_getter()
    if data:
        correct_answers = answer_getter(data)
        
    if question_id in correct_answers:
        print(f'The correct answer is: {correct_answers[question_id]}')
    else:
        print(f'Question id "{question_id}" not found in the available questions.')
