import pyttsx3 as pyt
import pyautogui as pyg
import pywhatkit as pyw
import webbrowser as wb
import os
import requests
import pyjokes
import smtplib
from datetime import datetime
import time


# Function to speak text
def speack(text):
    engine = pyt.init()
    engine.say(text)
    engine.runAndWait()


# Personalized Greetings
from datetime import datetime

def greet_user():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        speack("Good morning!")
    elif 12 <= hour < 18:
        speack("Good afternoon!")
    elif 18 <= hour < 22:
        speack("Good evening!")
    else:
        speack("Hello! It's late, but I'm here to help.")



# Weather Information
def get_weather(city):
    api_key = "your_api_key"  # Replace with OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            speack(f"The current temperature in {city} is {temp} degrees Celsius with {description}.")
        else:
            speack("Unable to fetch weather information. Please check the city name or API key.")
    except Exception as e:
        speack("Error fetching weather information.")
        print(f"Error: {e}")


# Time and Date
def get_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    speack(f"The current time is {current_time}.")


def get_date():
    today = datetime.now()
    current_date = today.strftime("%A, %B %d, %Y")
    speack(f"Today's date is {current_date}.")


# Reminders
def set_reminder(message, delay):
    speack(f"Reminder set. I will remind you to {message} in {delay} seconds.")
    time.sleep(delay)
    speack(f"Reminder: {message}")


# Telling Jokes
def tell_joke():
    joke = pyjokes.get_joke()
    speack(joke)


# News Headlines
def fetch_news():
    api_key = "your_api_key"  # Replace with NewsAPI key
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json()["articles"]
            speack("Here are the top news headlines:")
            for article in articles[:5]:
                speack(article["title"])
        else:
            speack("Unable to fetch news at the moment.")
    except Exception as e:
        speack("Error fetching news.")
        print(f"Error: {e}")


# Email Functionality
def send_email(to_email, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_password")  # Replace with your email credentials
        email_message = f"Subject: {subject}\n\n{body}"
        server.sendmail("your_email@gmail.com", to_email, email_message)
        speack("Email sent successfully.")
        server.quit()
    except Exception as e:
        speack("Failed to send the email.")
        print(f"Error: {e}")


# Take Screenshot
def take_screenshot():
    try:
        img = pyg.screenshot()
        save_path = r"C:\Users\jhakr\Downloads\project\screenshot.png"  # Update the path
        img.save(save_path)
        speack("Screenshot taken and saved successfully.")
    except Exception as e:
        speack("Failed to take a screenshot.")
        print(f"Error: {e}")



# Open Application
def open_app(app_name):
    try:
        speack(f"Opening {app_name}.")
        pyg.press("win")
        time.sleep(1)
        pyg.typewrite(app_name)
        pyg.press("enter")
        time.sleep(3)  # Give time for the app to open
    except Exception as e:
        speack(f"Failed to open {app_name}.")
        print(f"Error: {e}")


# Play Video
def play_video(video_name):
    try:
        speack(f"Playing {video_name} on YouTube.")
        pyw.playonyt(video_name)
    except Exception as e:
        speack("Failed to play the video.")
        print(f"Error: {e}")


# Main Task Handler
def perform_task(query):
    query = query.strip().lower()

    if "quit" in query:
        speack("Goodbye!")
        return False

    elif "time" in query:
        get_time()

    elif "date" in query:
        get_date()

    elif "joke" in query:
        tell_joke()

    elif "reminder" in query:
        speack("What should I remind you about?")
        message = input("Reminder: ").strip()
        speack("In how many seconds?")
        delay = int(input("Seconds: "))
        set_reminder(message, delay)

    elif "news" in query:
        fetch_news()

    elif "weather" in query:
        speack("Please tell me the city name.")
        city = input("City: ").strip()
        get_weather(city)

    elif "send email" in query:
        speack("Please provide the recipient's email address.")
        to_email = input("Recipient Email: ").strip()
        speack("What is the subject?")
        subject = input("Subject: ").strip()
        speack("What is the message?")
        body = input("Message: ").strip()
        send_email(to_email, subject, body)

    elif "screenshot" in query:
        take_screenshot()

    elif "open" in query:
        app_name = query.replace("open", "").strip()
        open_app(app_name)

    elif "play" in query:
        video_name = query.replace("play", "").strip()
        play_video(video_name)

    else:
        speack("Sorry, I don't understand that command.")

    return True


# Main Program
if __name__ == "__main__":
    greet_user()
    running = True
    while running:
        query = input("Task: ")
        running = perform_task(query)
