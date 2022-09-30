#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    pair = len(string)%2 == 0
    return pair

def remove_third_char(string: str) -> str:
    new_string = string[:2]+string[3:]
    return new_string


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_string = string.replace(old_char,new_char)
    return new_string

def replace_char_2(string: str, old_char: str, new_char: str) -> str:
    for i in range(len(string)):
        if string[i] == old_char:
            new_string = string[:i] + new_char + string[i+1:]
    return new_string


def get_number_of_char(string: str, char: str) -> int:
    n=0
    for i in string:
        if char == i:
            n+=1
    return n

def get_number_of_words(sentence: str, word: str) -> int:
    number= sentence.count(word)
    return number

def get_number_of_words_2(sentence: str, word: str) -> int:
    n=0
    a=sentence.split(" ")
    for i in a:
        if word in i:
            n+=1
    return n

def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char_2(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans {chaine} est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo, doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")

    chaine = "Baby shark doo, doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words_2(chaine, 'doo')}")

if __name__ == '__main__':
    main()
