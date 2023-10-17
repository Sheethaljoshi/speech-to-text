import speech_recognition as sr


def convert_audio_to_text():
    
    r = sr.Recognizer()

    
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)  

    try:
        text = r.recognize_google(audio)
        return text