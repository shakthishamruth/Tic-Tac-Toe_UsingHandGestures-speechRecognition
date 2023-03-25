import recordMic
import speechRecognition

num = 0


def number():
    global num
    recordMic.record()
    txt = speechRecognition.audioToTxt("output.wav")
    print(txt.upper())
    if txt.upper() == 'ONE.':
        num = 1
    elif txt.upper() == 'TWO.':
        num = 2
    elif txt.upper() == 'THREE.':
        num = 3
    elif txt.upper() == 'FOUR.':
        num = 4
    elif txt.upper() == 'FIVE.':
        num = 5
    elif txt.upper() == 'SIX.':
        num = 6
    elif txt.upper() == 'SEVEN.':
        num = 7
    elif txt.upper() == 'EIGHT.':
        num = 8
    elif txt.upper() == 'NINE.':
        num = 9
    elif txt.upper() == 'TEN.':
        num = 10
    else:
        num = 0


while True:
    number()
    file = open("outNumber.txt", "w")
    file.write(str(num))
    file.close()
