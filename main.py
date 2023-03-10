import pygame
import random
import cv2
import mediapipe as mp
import statistics
import time

pygame.init()

# Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input
cap = cv2.VideoCapture(0)  # Use 1 for external cam

# Window
screen = pygame.display.set_mode((800, 675))
pygame.display.set_caption('TicTacToe_UsingHandGestures')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')

# Font
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 128)

player = 1

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
xo = [['', '', ''], ['', '', ''], ['', '', '']]

player1score = 0  # Player1 is PLAYER
player2score = 0  # Player2 is BOT

# To get mouse position
x = 0
y = 0

sec = 0
stopwatchBoolean = True

win = 0
winner = '     Show 10 to start the game'

reset = False
running = True
start = False

ctime = time.time()
setCount = 0
countSet = []

finalCount = 0


# Functions
def show_player_turn_score():
    global player1score, player2score
    text_player1_score = font.render(str(player1score), True, (27, 140, 60))
    screen.blit(text_player1_score, (85, 311))
    text_player2_score = font.render(str(player2score), True, (3, 17, 138))
    screen.blit(text_player2_score, (751, 311))


def mouse_input_reset(x1, y1):
    global x, y, board, xo, win, reset, start, winner
    x2 = x1 + 50
    y2 = y1 + 50
    if x1 < x < x2 and y1 < y < y2:
        win = 0
        for i in range(3):
            for j in range(3):
                board[i][j] = 0
                xo[i][j] = ''
        win = 0
        reset = False
        start = False
        winner = '     Show 10 to start the game'


def check(a, b):
    global board, player
    if player == 1 and board[a - 1][b - 1] == 0:
        board[a - 1][b - 1] = player
        player = 2
        xo[a - 1][b - 1] = 'X'
        check_win()
    elif player == 2:
        if board[a - 1][b - 1] == 0:
            board[a - 1][b - 1] = player
            player = 1
            xo[a - 1][b - 1] = 'O'
            check_win()
        else:
            bot()


def check_win():
    global board, win, player1score, player2score, reset, player
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0:
            win = board[i][0]
            if win == 1:
                xo[i][0] = 'x'
                xo[i][1] = 'x'
                xo[i][2] = 'x'
            elif win == 2:
                xo[i][0] = 'o'
                xo[i][1] = 'o'
                xo[i][2] = 'o'
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:
            win = board[0][i]
            if win == 1:
                xo[0][i] = 'x'
                xo[1][i] = 'x'
                xo[2][i] = 'x'
            elif win == 2:
                xo[0][i] = 'o'
                xo[1][i] = 'o'
                xo[2][i] = 'o'
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 0:
        win = board[0][0]
        if win == 1:
            xo[0][0] = 'x'
            xo[1][1] = 'x'
            xo[2][2] = 'x'
        elif win == 2:
            xo[0][0] = 'o'
            xo[1][1] = 'o'
            xo[2][2] = 'o'
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != 0:
        win = board[2][0]
        if win == 1:
            xo[2][0] = 'x'
            xo[1][1] = 'x'
            xo[0][2] = 'x'
        elif win == 2:
            xo[2][0] = 'o'
            xo[1][1] = 'o'
            xo[0][2] = 'o'
    if win != 0:
        if win == 1:
            player1score += 1
        if win == 2:
            player2score += 1
        reset = True
        player = 1
    else:
        check_Draw()


def check_Draw():
    global winner, reset, player, win
    draw_cont = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                draw_cont += 1
    if draw_cont == 9:
        winner = '     DRAW'
        reset = True
        player = 1
        win = 3


def bot():
    global winner, start
    if win == 1:
        winner = 'Player Wins Show 10 to restart'
        start = False
    elif win == 2:
        winner = 'Player Lost Show 10 to restart'
        start = False
    elif win == 3:
        winner = '       DRAW Show 10 to restart'
        start = False
    else:
        while player == 2:
            check(random.choice([1, 2, 3]), random.choice([1, 2, 3]))


def gesture_input(a, b):
    global player, board, xo, winner, reset, win
    if reset:
        for i in range(3):
            for j in range(3):
                board[i][j] = 0
                xo[i][j] = ''
        win = 0
        reset = False
    elif player == 1:
        check(a, b)
    winner = ''


def showXO(cordx, cordy, a, b):
    global xo
    if xo[a - 1][b - 1] == 'X':
        textX = font2.render('X', True, (27, 140, 60))
        screen.blit(textX, (cordx + 44, cordy + 38))
    elif xo[a - 1][b - 1] == 'O':
        text_player_turn = font2.render('O', True, (3, 17, 138))
        screen.blit(text_player_turn, (cordx + 40, cordy + 38))
    elif xo[a - 1][b - 1] == '':
        text_ = font2.render('', True, (255, 255, 255))
        screen.blit(text_, (cordx + 44, cordy + 38))
    elif xo[a - 1][b - 1] == 'x':
        textX = font2.render('X', True, (255, 0, 0))
        screen.blit(textX, (cordx + 44, cordy + 38))
    elif xo[a - 1][b - 1] == 'o':
        text_player_turn = font2.render('O', True, (255, 0, 0))
        screen.blit(text_player_turn, (cordx + 40, cordy + 38))


def show_winner():
    global winner
    textX = font.render(winner, True, (0, 0, 0))
    screen.blit(textX, (160, 600))


def show_time():
    global sec
    sec = int(sec)
    mins = sec // 60
    sec = sec % 60
    mins = mins % 60
    time = '{0}:{1}'.format(int(mins), sec)
    texttime = font.render(time, True, (0, 0, 0))
    screen.blit(texttime, (705, 30))


# Main loop
with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.8,
        min_tracking_confidence=0.8) as hands:
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Initially set finger count to 0 for each cap
        fingerCount = 0

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:
                # Get hand index to check label (left or right)
                handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classification[0].label

                # Set variable to keep landmarks positions (x and y)
                handLandmarks = []

                # Fill list with x and y positions of each landmark
                for landmarks in hand_landmarks.landmark:
                    handLandmarks.append([landmarks.x, landmarks.y])

                # Test conditions for each finger: Count is increased if finger is considered raised.
                # Thumb: TIP x position must be greater or lower than IP x position, depending on hand label.
                if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                    fingerCount = fingerCount + 1
                elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                    fingerCount = fingerCount + 1

                # Other fingers: TIP y position must be lower than PIP y position, as image origin is in the
                # upper left corner.
                if handLandmarks[8][1] < handLandmarks[6][1]:  # Index finger
                    fingerCount = fingerCount + 1
                if handLandmarks[12][1] < handLandmarks[10][1]:  # Middle finger
                    fingerCount = fingerCount + 1
                if handLandmarks[16][1] < handLandmarks[14][1]:  # Ring finger
                    fingerCount = fingerCount + 1
                if handLandmarks[20][1] < handLandmarks[18][1]:  # Pinky
                    fingerCount = fingerCount + 1

                # Draw hand landmarks
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        if ctime + 0.1 <= (time.time()):
            countSet.append(fingerCount)
            setCount += 1
            ctime = time.time()

        # Taking mode of all the finger counts to get accurate finger count
        if setCount == 10:
            finalCount = statistics.mode(countSet)
            setCount = 0
            countSet = []
            ctime = time.time()
        # Display finger count
        cv2.putText(image, 'Input:' + str(finalCount), (35, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (27, 140, 60), 3)
        cv2.putText(image, str(fingerCount), (35, 75), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 0), 7)

        # Display camera video
        cv2.imshow('Camera', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

        # Pygame Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                mouse_input_reset(20, 630)
        # Check gesture inputs
        if not start and finalCount == 10:
            start = True
            winner = ''
            win = 0
            for i in range(3):
                for j in range(3):
                    board[i][j] = 0
                    xo[i][j] = ''
            win = 0
            reset = False
            sec = 0
            startTime = 0
            stopwatchBoolean = True
        if win == 0 and start:
            if stopwatchBoolean:
                startTime = time.time()
                stopwatchBoolean = False
            else:
                sec = time.time() - startTime
            match finalCount:
                case 1:
                    gesture_input(1, 1)
                    continue
                case 2:
                    gesture_input(1, 2)
                    continue
                case 3:
                    gesture_input(1, 3)
                    continue
                case 4:
                    gesture_input(2, 1)
                    continue
                case 5:
                    gesture_input(2, 2)
                    continue
                case 6:
                    gesture_input(2, 3)
                    continue
                case 7:
                    gesture_input(3, 1)
                    continue
                case 8:
                    gesture_input(3, 2)
                    continue
                case 9:
                    gesture_input(3, 3)
                    continue
        # Display X O on screen
        showXO(130, 50, 1, 1)
        showXO(310, 50, 1, 2)
        showXO(490, 50, 1, 3)
        showXO(130, 230, 2, 1)
        showXO(310, 230, 2, 2)
        showXO(490, 230, 2, 3)
        showXO(130, 410, 3, 1)
        showXO(310, 410, 3, 2)
        showXO(490, 410, 3, 3)
        bot()
        show_winner()
        show_time()
        show_player_turn_score()
        pygame.display.update()
cap.release()
