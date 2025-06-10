import requests
import gradio as gr
import speech_recognition as sr
import pyttsx3
ollama_url = "http://localhost:11434/api/chat/generate"
#text to speech engine
engine = pyttsx3.init()
def ai_assistant(imput_text):
    prompt = f"Answer the following question:\n {imput_text}"
    payload = {
        "model":"deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False,
    }
    response = requests.post(ollama_url, json=payload)
    if response.status_code == 200:
        ai_response = response.json().get("response", "I don't know the answer to that.")
    # Convert the response to speech
        engine.say(ai_response)
        engine.runAndWait()
        return ai_response
    else:
        return "Error: Unable to get a response from the AI model."
# Function to handle speech input using voice command function
def voice_command():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command  
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            return "Sorry, Speech recognizattion is not available ."
        
# Test the assistant
