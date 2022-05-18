from gtts import gTTS

text = "I am vishakh abhyan, am a python programmer"

language = "en-uk"

speech = gTTS(text=text, lang=language, slow=False)

speech.save("audio.mp3")

