import math 
from tqdm import tqdm
import time
import os

def information(answer_list, local_list):

    total_array = []
    key_array = ["g", "y", "w"]
    info_array = []
    word_list = []
    length = len(local_list)
    list_tuple = tuple(answer_list)
    print(len(list_tuple))

    for guess in tqdm(list_tuple, desc="Calculating..."):
        total_info = 0
        for first in key_array:
            for second in key_array:
                for third in key_array:
                    for fourth in key_array:
                        for fifth in key_array:
                            test_list = list(local_list)
                            key = first+second+third+fourth+fifth
                            indices = []

                            for i in range(len(guess)):
                                indices.append([j for j in range(len(guess)) if guess[j] == guess[i]])

                            bad_key = False

                            for i in (range(len(indices)-1)):
                                if(bad_key == False):
                                    for j in range(len(indices[i])-1):
                                        if(key[indices[i][j]] == "w" and key[indices[i][j+1]] == "y"):
                                            bad_key = True
                                            break
                                else:
                                    break                            
                            if(not bad_key):
                                new_list = find_matches(key, guess, test_list)
                                probability = len(new_list)/length
                            else:
                                probability = 0

                            if(probability == 0):
                                info = 0
                            else:
                                info = math.log(1/probability, 2)*probability
                            #print(str(info) + " " + str(probability))
                            total_info += info
        #print(guess)                    
        #print(total_info)
        guess_array = [guess, total_info]
        info_array.append(total_info)
        word_list.append(guess)
        total_array.append(guess_array)
    #total_array.append(word_list)
    return total_array


def find_matches(key, guess, alocal_list):
    word_list=tuple(alocal_list)
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    list_of_char = []
    letters = []
    keys = []
    bad_char = []

    for i in alphabet:
        if i in guess:
            letters.append(i)

    for i in range(len(letters)):
        keys = []
        for j in range(len(guess)):
            if(guess[j] == letters[i]):
                keys.append(key[j])
            else:
                keys.append("_")
        new_array = []
        new_array.append(letters[i])
        new_array.append(keys)
        list_of_char.append(new_array)

    for word in word_list:
        stop = False
        for i in range(len(list_of_char)):
            if stop:
                break
            elif "y" not in list_of_char[i][1] and "g" not in list_of_char[i][1] and list_of_char[i][0] in word:
                alocal_list.remove(word)
                break
            elif "g" in list_of_char[i][1] and list_of_char[i][0] not in word:
                alocal_list.remove(word)
                break
            elif "y" in list_of_char[i][1] and list_of_char[i][0] not in word:
                alocal_list.remove(word)
                break
            elif ((list_of_char[i][1].count("y") + list_of_char[i][1].count("g"))>word.count(list_of_char[i][0])):
                alocal_list.remove(word)
                break
            elif "w" in list_of_char[i][1] and ((list_of_char[i][1].count("y") + list_of_char[i][1].count("g"))<word.count(list_of_char[i][0])):
                alocal_list.remove(word)
                break
            else:
                for j in range(len(list_of_char[i][1])):
                    if list_of_char[i][1][j] == "g" and list_of_char[i][0] != word[j]:
                        alocal_list.remove(word)
                        stop = True
                        break
                    elif list_of_char[i][1][j] == "y" and list_of_char[i][0] == word[j]:
                        alocal_list.remove(word)
                        stop = True
                        break
                    elif list_of_char[i][1][j] == "w" and list_of_char[i][0] == word[j]:
                        alocal_list.remove(word)
                        stop = True
                        break

    return alocal_list

answers = []
guesses = []
total = []

with open('wordle_answers.txt') as file:
    for line in file:
        answers.append(line.rstrip())
        total.append(line.rstrip())

with open('wordle_guesses.txt') as file:
    for line in file:
        guesses.append(line.rstrip())
        total.append(line.rstrip())

new_list = answers
new_key = "wwwww"

whole_total = tuple(answers)
while(new_key!="ggggg"):

    word_guess = input("First guess: ")
    new_key = input("Key returned: ")

    os.system('cls||clear')

    base_length = len(new_list)

    new_list = find_matches(new_key, word_guess, new_list)
    #whole_total = tuple(new_list)

    print(new_list)
    
    found_length = len(new_list)

    #print(found_length)

    probability = found_length/base_length

    if(probability == 0):
        info = 0
    else:
        info = math.log(1/probability, 2)

    print(str(info)+" bits of information")
    #print(new_list)

    print("There are " + str(len(new_list)) + " possible words")
    answers = information(list(whole_total), new_list)
    answers.sort(key=lambda x:x[1], reverse=True)
    for i in range(min(10, len(answers))):
        print(answers[i])

