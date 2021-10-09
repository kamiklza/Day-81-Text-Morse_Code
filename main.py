morse_code = {'a' : '.-',
              'b' : '-...',
              'c' : '-.-.',
              'd' : '-..',
              'e' : '.',
              'f' : '..-.',
              'g' : '--.',
              'h' : '....',
              'i' : '..',
              'j' : '.---',
              'k' : '-.-',
              'l' : '.-..',
              'm' : '--',
              'n' : '-.',
              'o' : '---',
              'p' : '.--.',
              'q' : '--.-',
              'r' : '.-.',
              's' : '...',
              't' : '-',
              'u' : '..-',
              'v' : '...-',
              'w' : '.--',
              'x' : '-..-',
              'y' : '-.--',
              'z' : '--..',
              '1' : '.----',
              '2' : '..---',
              '3' : '...--',
              '4' : '....-',
              '5' : '.....',
              '6' : '-....',
              '7' : '--...',
              '8' : '---..',
              '9' : '----.',
              '10' : '-----'}

message = input('Please enter the message: ').lower()
message_in_words = message.split(' ')

converted_message = []
for word in message_in_words:
    converted_message.append([morse_code[char] for char in word])
print(converted_message)

for index in range(len(converted_message)):
    for word in converted_message[index]:
        print(word)
    print('\n')

print(*converted_message)
# for word in message:
#
#     if word != ' ':
#         print(morse_code[word])
#     else:
#         print(' ')
# converted_message = [morse_code[word] for word in message if word != ' ']
# x = ' '.join(converted_message)
# print(x)


