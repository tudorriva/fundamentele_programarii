def replace_word (file_name, word, replacing_word):
    file = open(file_name, 'r')
    text = file.read()
    count = text.count(word)
    if count > 0:
        file = open(file_name, 'w')
        new_text = text.replace(word, replacing_word)
        file.write(new_text)
        print(f"Ersetzt '{word}' durch '{replacing_word}' an {count} Stellen.")
    else:
        print(f"Das Wort '{word}' wurde in der Datei nicht gefunden.")


def main():
    file_name = input("Pfad zur Datei: ")
    word = input("Wort zu ersetzen: ")
    replacing_word = input("Ersatzwort: ")
    replace_word(file_name, word, replacing_word)

main()