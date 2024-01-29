# def guesser():
#     primarchs = ['magnus', 'sanguinius', 'horus', 'leeman', 'fulgrim', 'rogal', 'peterturbo',
#                  'ferus', 'mortarion', 'lorgar', 'angron', 'corvus', 'conrad', 'vulkan', 'girllyman',
#                  'lionel', 'jhagatai', 'alpharius']
#     target = random.choice(primarchs)
#     letters_used = []
#     max_attempts=6
#
#     while max_attempts > 0 :
#         revealed_word = ""
#         guess = input("guess a character: ")
#         if len(guess) != 1:
#             print('invalid guess enter only one letter')
#             continue
#         letters_used.append(guess)
#         if guess in target:
#             print('correct guess')
#         else:
#             print("Wrong try again")
#             print("_")
#             max_attempts -= 1
#         for letter in target:
#             if letter in letters_used:
#                 revealed_word += letter + ' '
#             else:
#                 revealed_word += ' _ '
#         print("the word is: ",revealed_word)
#         print("attempts left: ", max_attempts)
#
#         if all(letter in letters_used for letter in target):
#             print("Congratulations! You guessed",revealed_word," word correctly!")
#             break
#         if max_attempts == 0:
#             print("out of guesses")
#             break
#
# x = guesser()
# print(x)