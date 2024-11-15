#the following code is for a ai assitant named jarvis that helps in open website
import webbrowser  # Website open karne ke liye webbrowser library import karte hain
import pyttsx3     # Text-to-speech functionality ke liye pyttsx3 library import karte hain

# Text-to-speech engine initialize karte hain
engine = pyttsx3.init()

# Function to speak a given message
def speak(message):
    engine.say(message)  # Message ko tts engine me daalte hain
    engine.runAndWait()  # TTS process start karte hain aur wait karte hain till it completes

# Website open karne ka function
def open_website():
    speak("Please enter the website you want to open")  # Bot message bolta hai
    url = input("Enter the website URL (e.g., https://www.example.com): ")
    
    # Agar URL mein 'https://' ya 'http://' nahi diya gaya, toh hum 'https://' prepend karte hain
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    
    webbrowser.open(url)  # URL ko browser mein open karte hain
    speak(f"Opening {url} in your default browser")  # Bot message bolta hai ki website open ho rahi hai
    print(f"Opening {url} in your default browser...")

# Main program ko run karte hain
if __name__ == "__main__":#important to write acche devloper banane ke liye
    speak("Hello Boss, this is Fauzan Present for the work")  # Initial greeting message
    print("Hello Boss, this is Jarvis!")
    open_website()  # Open website function ko call karte hain
