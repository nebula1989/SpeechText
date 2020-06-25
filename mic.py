import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio from default mic

    audio_data = r.record(source, duration=5)

    print("Recognizing...")

    text = r.recognize_google(audio_data)
    print(text)
