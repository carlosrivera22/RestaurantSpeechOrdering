#import library
import speech_recognition as sr

class SR:
    def __init__(self):
    #create recognizer
        self.r = sr.Recognizer()

        #Define your microphone
        # print(sr.Microphone.list_microphone_names())

        self.mic = sr.Microphone(device_index=0)

    def get_speech_to_text(self):
        with self.mic as source:
            audio = self.r.listen(source)
        while True:
            try:
                result = self.r.recognize_google(audio)
                return result
            except:
                return ""