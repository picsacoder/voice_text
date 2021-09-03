import speech_recognition

r = speech_recognition.Recognizer()

with speech_recognition.AudioFile('audio.wav') as src:
    
    owo = r.listen(src)

    try:
        text = r.recognize_google(owo)
        print(text)

        f = open("text.txt", "w")
        f.write(text)
        f.close()

        print("Check text.txt nwn")
    except:
        print('error')