import os
import datetime


def diary():
    '''Command line-based diary'''
    notes = ''
    today = datetime.date.today()
    os.makedirs('tmp', exist_ok=True)
    print('Enter your notes for today. Type "exit" to save and quit.')

    while True:
        note = input()
        if note.lower() == 'exit':
            if notes:
                file_path = os.path.join('tmp', f'{today}.txt')
                with open(file_path, 'a', encoding='utf-8') as f:
                    f.write(notes)
                print(f'\nYour notes were saved to {today}.txt\n')
            else:
                print("\nYou didn't enter any notes. Exiting.\n")
            break
        if note:
            notes += note + '\n'


if __name__ == '__main__':
    diary()
