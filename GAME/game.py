import random #for choose random choices
import time #for time sleep to program execution
import speech_recognition as sr    # speech recognition used for listening the user input through microphone
import pygame
import pyttsx3  # pyttsx3 used to speak the output of the game through speakers


def play_game():
    while True:
        engine = pyttsx3.init()
        
        r = sr.Recognizer()
        print("==========Welcome to the my game!==============")
        engine.say("Welcome to the my game!. I am Tony Stark here to play rock paper scissors with you. Let's start the game!")
        engine.runAndWait()
        choices = ["rock", "paper", "scissors"]

        with sr.Microphone() as source:
            engine.say("Please say your choice (rock, paper, scissors):")
            engine.runAndWait()
            audio = r.listen(source)

        try:
            user = r.recognize_google(audio).lower()
        except sr.UnknownValueError:
            engine.say("Sorry, I did not understand that.")
            engine.runAndWait()
            exit()
        except sr.RequestError as e:
            engine.say(f"Could not request results from Google Speech Recognition service; {e}")
            engine.runAndWait()
            exit()

        computer = random.choice(choices)

        engine.say(f"You chose : {user}, and computer chose : {computer}")
        engine.runAndWait()

        print("Computer chose:", computer)    
        if user not in choices:
            engine.say("Invalid choice! Please choose rock, paper, or scissors.")
            engine.runAndWait()
        elif user == computer:
            time.sleep(1)
            engine.say("It's a tie!")
            engine.runAndWait()
        else:
            if (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
                time.sleep(1)
                engine.say("You win!")
                engine.runAndWait()
                print("You win!")
            else:
                time.sleep(1)
                engine.say("Computer wins!")
                engine.runAndWait() 
                
                print("Computer wins!")
                
                print("Thank you for playing the game!")

if __name__ == "__main__":  #for function call
    play_game()
    