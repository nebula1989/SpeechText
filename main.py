import speech_recognition as sr

filename = "audio.wav"

# init recognizer

r = sr.Recognizer()

# open file
with sr.AudioFile(filename) as source:
    # listen
    audio_data = r.record(source)
    # make into text
    text = r.recognize_google(audio_data)
    print(text)

    # create text file
    text_file = open("speech_text.txt", "w")
    text_file.write(text)
    text_file.close()
