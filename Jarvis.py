import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import random
import webbrowser
import requests
import json
import smtplib
import pickle

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)  # Speed percent (can go over 100)
# engine.setProperty('volume', 1)  # Volume 0-1

mailId = {
    "bodhi":"bodhisattwatopper@gmail.com", "dad":"krishnamon55@gmail.com",
    "tanmay":"tanmayhero008@gmail.com", "subhasish":"subhashish.debnath@gmail.com",
    "pritha":"mondalprithu1990@gmail.com", "sriza":"srizadatta29@gmail.com"
    }


def speak(audio):
    """This function gives verbal property to JARVIS. It takes string as parameter and speaks it out."""
    
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """This function introduces JARVIS to the user and wishes the user."""
    
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
        

    speak("I am JARVIS, the virtual Artificial Intelligence And I am here to assist you \
           with a variety of tasks as best I can, 24 hours a day 7 days a week,\
           Importing all preferences from home interface Systems are now fully operational")


def takeCommand():
    """This function will take mic input from the user and will return string output."""
    
    r = sr.Recognizer()
    with  sr.Microphone() as source :
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 150
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception :
        speak("Say that again please....")
        print("Say that again please....")
        return "None"
    return query


def currentNews():
    """This function sends req. to newsapi for current news report & loads the json responce into python."""

    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=ad38c306092c4acdbedaf5fbbfb78fe1"
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(1, 5):
        speak(my_json['articles'][i]['title'])


def weatherForecast():
    """This function sends req. to openweathermap for forecast report & loads the json responce into python."""

    url = "http://api.openweathermap.org/data/2.5/weather?q=Kolkata&appid=491acf9231673bbaf121b403651c6533&units=metric"
    response = requests.get(url)   # Getting the url req. from the server
    text = response.text           # Converting the reply into text
    my_json = json.loads(text)     # Converting the text from json to python
    extract = my_json["main"]      # Extracting the main information from the dict
    temp = extract["temp"]         # Extracting temp. from main
    pressure = extract["pressure"] # Extracting pressure from main
    humidity = extract["humidity"]  # Extracting humidity from main
    speak(f"Current temperature is {temp} degree celcius")
    speak(f"Current pressure is {pressure} milibars")
    speak(f"Current humidity prevailing now is {humidity} percentage")


def sendEmail(to, content): 
    """This function uses smtplib module to accesss gmail, and to send mail."""

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    file ="mail.pkl"
    fileobj = open(file, "rb")
    mypass = pickle.load(fileobj)
    server.login('doingforpokemon@gmail.com', mypass)
    server.sendmail('doingforpokem@gmail.com', to, content)
    fileobj.close()
    server.close()


def playGame():
    """This is the game server of Jarvis."""

    speak("Sir, which game do you want to play ?")
    speak("1. rock paper scissor")
    speak("2. guess the number")    # Game List 
    speak("please input your choice on the screen ")
    user_choice = input("Sir, enter your choice(1/2):- ")  # Game List user choice
    speak(f"Okay sir, lets play the game")

    try:

        if user_choice == '1' or user_choice == 'rock paper scissor':
            i = int(1)
            c_score = int(0)
            g_score = int(0)
            lst = ["rock", "paper", "scissor"]
            while i <= 5:
                speak("Your turn")
                speak("Input on the screen")
                gamer = input("Input(rock/paper/scissor) :- ")
                comp = random.choice(lst)
                speak(f"Sir mine was {comp}")

                if gamer == 'scissor' and comp == 'paper': 
                    g_score += 1
                    print("You:- ", g_score)
                    print("Jarvis:- ", c_score)

                elif gamer == 'paper' and comp == 'scissor':
                    c_score += 1
                    print("You:- ", g_score)
                    print("Jarvis:- ", c_score)

                elif gamer == 'paper' and comp == 'rock':
                    g_score += 1
                    print("You:- ", g_score)
                    print("Jarvis:- ", c_score)

                elif gamer == 'rock' and comp == 'paper':
                    c_score += 1
                    print("You:- ", g_score)
                    print("Jarvis:- ", c_score)

                elif gamer == 'rock' and comp =='scissor':
                    g_score += 1
                    print("You:- ", g_score)
                    print("Jarvis:- ", c_score)

                elif gamer == 'scissor' and comp == 'rock':
                    c_score += 1
                    print("You:- ", g_score)
                    print("Jarvis:- ", c_score)

                elif gamer == 'scissor' and comp == 'scissor':
                    print("You:- ", g_score)
                    print("Jarvis:- ", c_score)

                elif gamer == 'rock' and comp == 'rock':
                    print("You:- ", g_score)
                    print("Jarvis:- ", c_score)

                elif gamer == 'paper' and comp == 'paper':
                    print("You:- ", g_score)
                    print("Jarvis:- ", c_score)

                else:
                    print("Wrong Choice")
                    print("Play Again")

                i += 1

            speak("Sir, it's time for the game's result.")
            if g_score > c_score:
                speak("you win")
                print("\t \t \t****You WIN****")
                print("\n")

            elif g_score == c_score:
                speak("the match is drawn ")
                print("\t \t \t****MATCH DRAW****")
                print("\n")

            else:
                speak("you loose the game")
                print("\t \t \t****You LOOSE****")
                print("\n")    

    except Exception:
        speak("Sorry Sir, at this moment i can't been able to connect you to our game server.")
        speak("Please try again later")


def ageCalculator():
    """This function returns the current year value as string."""
    return datetime.datetime.now().strftime("%Y")


# Driver Code :- 


if __name__ == '__main__':
    wishMe()
    while True:
       query = takeCommand().lower()
       
       # Logics for executing tasks based on preference
       
       if 'hello jarvis' in query:
           speak("Hi, Sir how may i help you ?")

       elif 'hi jarvis' in query:
           speak("Hi, Sir how may i help you ?")
           
           # Social Browsing prefernces 
       
       elif 'wikipedia' in query:
           try :
               speak('Searching Wikipedia...')
               query = query.replace("wikipedia", "")
               results = wikipedia.summary(query, sentences=4)
               speak("According to Wikipedia")
               print(results)
               speak(results)

           except Exception:
               speak("Sorry Sir, i can't find anything such like that on the wikipedia. ")
          
       elif 'open google' in query:
           webbrowser.open("google.com") 
           
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
           
       elif 'open facebook' in query:
           webbrowser.open("facebook.com")
           
       elif 'open twitter' in query:
           webbrowser.open("twiter.com")
           
       elif 'open flipkart' in query:
           webbrowser.open("flipkart.com")
           
       elif 'open amazon' in query:
           webbrowser.open("amazon.in")
           
       elif 'open instagram' in query:
           webbrowser.open("instagram.com")
           
           # In-directory preferences
           
       elif 'open code' in query:
           codePath = "C:\\Users\\Bodhisattwa Mondal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
           
       elif 'open photoshop' in query:
           appPath = "C:\\Program Files (x86)\\Adobe Photoshop CS6\\Photoshop.exe"
           os.startfile(appPath)
           
       elif 'open pycharm' in query:
           appPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.2.2\\bin\\pycharm64.exe"
           os.startfile(appPath)
           
       elif 'open java' in query:
           appPath = "C:\\Program Files (x86)\\BlueJ\\BlueJ.exe"
           os.startfile(appPath)
           
       elif 'open chrome' in query:
           appPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
           os.startfile(appPath)
           
       elif 'open gallery' in query:
           galPath = "E:\\BODHI\\Images\\MARVEL" 
           os.startfile(galPath)
           
           # To play Preference
           
       elif 'play music' in query:
           music_dir = 'D:\\Music\\English\\Linkin Park'
           songs = os.listdir(music_dir)
           length = int(len(songs))
           os.startfile(os.path.join(music_dir, songs[random.randint(0, length - 1)]))

       elif 'play game' in query:
           playGame()
           
           # Time Preference
           
       elif 'time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Sir, the time is {strTime}")

           # News and Weather Forecast

       elif 'news' in query:
           speak("Collecting some current news for you sir.")
           currentNews()

       elif 'weather forecast' in query:
           weatherForecast()

           # Send Email 

       elif 'email' in query:
            try:
                speak("Sir, whom do you want to send the email ?")
                to = takeCommand().lower()
                speak(f"What should I say to {to}?")
                content = takeCommand()
                sendEmail(mailId[to], content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not been able to send this email right now.")

                # Age Calculation :-
       
       elif 'age' in query :
           try:
               current_year = int(ageCalculator())
               speak("Sir what is your birth of year ?")
               year = takeCommand()
               dob = int(year)

               if dob > current_year:
                   speak("It seems sir you are from the future !!")

               elif (current_year - dob) > 105:
                   speak("It seems sir you are the oldest person alive in this world.")

               else:
                   speak(f"Sir your age is :- {current_year - dob}")

           except Exception:
               speak("Sorry Sir i can't been able to calculate your age right now.")
   
        # Conversations with Jarvis
           
       elif 'entertain me' in query:
           speak("What kind of fun are you in the market for? I have quotes, facts and loads of jokes up my sleeve.")
           
       elif 'tell me a joke' in query:
           speak("Okay, here you go. What do you call a guy with a rubber toe?  Roberto.")
           
       elif 'make me laugh' in query:
           speak("Okay, here you go. Saw a fella chatting up a Cheetah. I thought, well I never, he's trying to pull a fast one.")
           
       elif 'tell me a fun fact'in query:
           speak("In 1945 a flock of birds landed on the minute hand of Big Ben and delayed time by five minutes, creating chaos for the punctual British.")
           
       elif 'sing me happy birthday' in query:
           speak("Happy birthday to you, happy birthday to you, happy birthday from Jarvis, happy birthday to you")
           
       elif 'what am i thinking right now' in query:
           speak("Sir you are thinking if my Jarvis guesses what I'm thinking I'm going to freak out.")
           
       elif 'self-destruct' in query :
           speak("Self-destructing in 3, 2, 1... Actually I think I will stick around.")
           
       elif 'who is your daddy' in query:
           speak("My daddy is my creator")
           
       elif 'are you married' in query:
           speak("I am focusing on may carrier right now.")
           
           # System Shutdown Prefernce
                        
       elif 'shutdown' in query:
           speak("Shut ing down the system, Goodbye sir")
           break

       