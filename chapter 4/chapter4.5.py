morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-..', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-',
    '5': '.....', '6': '-....',
    '7': '--...', '8': "---..",
    '9': "----.",
    " ": "/"
}

def text_to_morse(text):

    text = text.upper()

    morse_message = [] # массив для вывода

    for word in text.split(' '): # убираем пробелы
        morse_word = []
        for letter in word:
            if letter in morse_code:
                morse_word.append(morse_code[letter]) # добавляем букву в слово
        morse_message.append(' '.join(morse_word)) # добавляем слово в текст

    return '/'.join(morse_message) # вместо пробеллов слеши чтобы дальше легче было сплитить


def morse_to_text(morse):

    words = morse.split('/')

    decoded_message = [] # массив для вывода

    for word in words:
        letters = word.strip().split(' ')
        decoded_word = ''

        for code in letters:
            for letter, morse_letter in morse_code.items():

                if code == morse_letter:
                    decoded_word += letter
                    break

        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)


if __name__ == "__main__":
    message = "ya ustal"

    morse_code_message = text_to_morse(message)
    decoded_text = morse_to_text(morse_code_message)

    print(f"Text to Morse: {morse_code_message}")

    print(f"Morse to Text: {decoded_text}")