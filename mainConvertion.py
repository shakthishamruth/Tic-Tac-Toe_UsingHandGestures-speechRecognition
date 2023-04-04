import recordMic
import speechRecognition

num = 0


def number():
    global num
    recordMic.record()
    txt = speechRecognition.audioToTxt("output.wav").split(' ', 1)
    first_word = str(txt[0]).upper()
    print(first_word.upper())
    if first_word == 'ONE.':
        num = 1
    elif first_word == 'TWO.':
        num = 2
    elif first_word == 'THREE.':
        num = 3
    elif first_word == 'FOUR.':
        num = 4
    elif first_word == 'FIVE.':
        num = 5
    elif first_word == 'SIX.':
        num = 6
    elif first_word == 'SEVEN.':
        num = 7
    elif first_word == 'EIGHT.':
        num = 8
    elif first_word == 'NINE.':
        num = 9
    elif first_word == 'TEN.':
        num = 10
    else:
        num = 0


while True:
    number()
    file = open("outNumber.txt", "w")
    file.write(str(num))
    file.close()
