import speech_recognition


r = speech_recognition.Recognizer()

with speech_recognition.AudioFile('englishhh.wav') as src:
    
    owo = r.listen(src)

    try:
        text = r.recognize_google(owo)
        print(text)
    except:
        print('error')