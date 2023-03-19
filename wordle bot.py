import math

def information(local_list):

    total_array = []
    key_array = ["g", "y", "w"]
    info_array = []
    word_list = []
    length = len(local_list)
    list_tuple = tuple(local_list)
    print(len(list_tuple))
    for guess in list_tuple:
        #print(local_list)
        #print(guess)
        total_info = 0
        for first in key_array:
            for second in key_array:
                for third in key_array:
                    for fourth in key_array:
                        for fifth in key_array:
                            test_list = list(local_list)
                            key = first+second+third+fourth+fifth

                            new_list = find_matches(key, guess, test_list)
                            probability = len(new_list)/length
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
    for word in word_list:   
        for i in range(5):
            if(key[i] == "w"):
                if(guess.count(guess[i])==1 and guess[i] in word):
                    alocal_list.remove(word)
                    break
                elif(guess.count(guess[i])==2 and word.count(guess[i])>1):
                    alocal_list.remove(word)
                    break
                elif(guess.count(guess[i])==3 and word.count(guess[i])>2):
                    alocal_list.remove(word)
                    break
                elif(word[i] == guess[i]):
                    alocal_list.remove(word)
                    break          
            elif(key[i] == "g" and guess[i] != word[i]):
                alocal_list.remove(word)
                break
            elif(key[i] == "y" and guess[i] not in word):
                alocal_list.remove(word)
                break
            elif(key[i] == "y" and guess[i] == word[i]):
                alocal_list.remove(word)
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

    base_length = len(new_list)

    new_list = find_matches(new_key, word_guess, answers)

    print(new_list)
    
    found_length = len(new_list)

    probability = found_length/base_length
    info = math.log(1/probability, 2)

    print(str(info)+" bits of information")
    #print(new_list)

    print("There are " + str(len(new_list)) + " possible words")
    answers = information(new_list)
    answers.sort(key=lambda x:x[1], reverse=True)
    for i in range(min(10, len(answers))):
        print(answers[i])

#print(information(answers))


"""print(len(total))

#word_list = ["world", "coupe", "welsh", "loopy", "slate", "fiddl"]
info_results = information(answers)
array_size = len(info_results[0])

with open('results.txt', 'w') as f:
    i = 0
    while(i<array_size):
        f.write(info_results[0][i] + ",")
        f.write(str(info_results[1][i]))
        f.write("\n")
        i = i + 1"""

"""word_list = ["hello", "world", "coupe", "troop", "walsh", "loopy", "slate"]
guess = "coupe"
key = "ggggg"
find_matches(key, guess, word_list)"""


        





#def compare_word(guess, answer):
