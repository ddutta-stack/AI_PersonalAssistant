import requests
import gradio as gr
import speech_recognition as sr
import pyttsx3
ollama_url = "http://localhost:11434/api/chat/generate"
#text to speech engine
engine = pyttsx3.init()
def ai_assistant(imput_text):
    prompt = f"Answer the following question:\n {imput_text}"