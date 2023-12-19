from gtts import gTTS
import os
mytext = "Hello Orif , How are you"
audio = gTTS(text=mytext, lang="en", slow=False)
audio.save("example1.mp3")
os.system("start example.mp3")