import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import webbrowser
import pyautogui
import datetime


def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("you said: "+ command)
        return command.lower()
    except sr.UnknownValueError:
        print("couldn't able to understand your audio")
        return None
    except sr.RequestError:
        print("unable to connect to the api")
        return None
    
def response(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    response_file = 'response.mp3'
    tts.save("response.mp3")
    playsound.playsound(response_file)
    os.remove(response_file)


task =[]
ListeningToTask = False

def main():
    global task
    global ListeningToTask
    response("hello, I am KD, How can I help you?")
    while True:
        commands = listen_for_command()

        

        if commands  in commands:
            if ListeningToTask:
                task.append(commands)
                ListeningToTask = False
                response("Adding " + commands +"to your list" + str(len(task))+ "currently in your list.")
                continue
            elif "add a task" in commands:
                ListeningToTask = True
                response("sure, what is the task ?")
                continue
            elif 'list task' in commands:
                response("sure, your tasks are: ")
                for tasks in task:
                    response(tasks)
                continue
            elif "git" in commands:
                response("opening git")
                webbrowser.open("https://github.com/HariharanRavisankar")
                continue
            elif "take a snap" in commands:
                response("taking a screenshot")
                pyautogui.screenshot("screenshot.png")
                continue
            elif "what time it is" in commands:
                time = str(datetime.datetime.now())
                response("the time is " +time)
                continue
            elif "close" in commands:
                response("Bye!, come again other time")
                break
            else:
                response("sorry, I am not sure what are you telling")

if __name__ == "__main__":
   main()
