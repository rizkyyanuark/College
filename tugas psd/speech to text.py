import azure.cognitiveservices.speech as speechsdk
# Replace with your own subscription key and service region
speech_key = "5544cd8ec2fb442c8527470731b0daae"
service_region = "https://southeastasia.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

# Replace with the path to your audio file
audio_file = r"C:\Users\rizky\OneDrive\Dokumen\GitHub\test\testpython\project gui\Recording (5).mp3"

# Set up the speech configuration
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key, region=service_region)

# Set up the audio configuration
audio_config = speechsdk.audio.AudioConfig(filename=audio_file)

# Set up the speech recognizer
speech_recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config, audio_config=audio_config)

# Perform speech recognition
result = speech_recognizer.recognize_once()

# Print the transcribed text
print(result.text)

# code untuk menangkap gambar di gui
