import speech_recognition as sr




def voice2text(target_file_path,lang_is="tr-TR"):
    target_file_path = str(target_file_path)

    try:
        recognizator = sr.Recognizer()
        with sr.AudioFile(target_file_path) as sound_file:
            audio_is = recognizator.record(sound_file)
            finaly_text_is = recognizator.recognize_google(audio_data=audio_is,language=lang_is)
            return [ "true" , finaly_text_is ]
    
    except Exception as err_msg:
        return ["false", f"Error: {str(err_msg)}"]
    




