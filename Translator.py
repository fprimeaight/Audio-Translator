import speech_recognition as sr
import googletrans

def main():
    translator = googletrans.Translator()
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print('Listening...')
        audio = r.listen(source)
        print('Processing audio...')

        try:
            s = f'{r.recognize_google(audio)}'
            translator = googletrans.Translator()
            s = translator.translate(s,dest='zh-cn').text

            with open('Translated_Text.txt','w',encoding='utf-8') as f:
                f.write(s)
                print('Audio processed!')

        except Exception as e:
            print(f'Error: {e}')
    
if __name__ == '__main__':
    main()
