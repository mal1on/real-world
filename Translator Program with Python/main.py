'''
Program that lets users translate some text between languages through
the command line.
'''


import asyncio
from googletrans import Translator, LANGUAGES


LANGS = LANGUAGES.keys()


async def gtrans(text, lang):
    '''Translator function'''
    async with Translator() as translator:
        result = await translator.translate(text, dest=lang)
        print(f'\n{result.text}\n')


def main():
    '''Main function'''
    while True:
        text = input('Enter the text to translate: ')
        if not text:
            print('\nYou should enter text to translate.\n')
            continue
        else:
            lang = input('\nEnter the destination language (e.g., "fr" for French): ')
            if not lang or lang not in LANGS:
                print('\nPlease enter valid destination language.\n')
                continue
        if text and lang:
            break

    asyncio.run(gtrans(text, lang))


if __name__ == '__main__':
    main()
