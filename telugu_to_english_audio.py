from googletrans import Translator
import pyttsx3

# Initialize Google Translator
translator = Translator()

# Initialize the pyttsx3 engine for Text-to-Speech
engine = pyttsx3.init()

# Function to translate Telugu text to English
def translate_telugu_to_english(telugu_text):
    try:
        # Translate the Telugu text to English
        translated = translator.translate(telugu_text, src='te', dest='en')
        print(f"Original Telugu Text: {telugu_text}")
        print(f"Translated English Text: {translated.text}")
        return translated.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return None

# Function to convert text to speech (English)
def text_to_speech(text, output_file):
    try:
        # Set up the speech engine rate and volume
        engine.setProperty('rate', 150)  # Speed of the speech
        engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

        # Save the speech to an audio file
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        print(f"English audio has been saved to {output_file}")
    except Exception as e:
        print(f"Error in converting text to speech: {e}")

# List of example Telugu texts to translate
telugu_texts = [
    "మీరు ఎలా ఉన్నారు?",  # How are you?
    "మీ పేరు ఏమిటి?",  # What is your name?
    "నాకు సాయం కావాలి."  # I need help.
]

# Iterate over the list of Telugu texts
for i, telugu_text in enumerate(telugu_texts, start=1):
    # Step 1: Translate Telugu text to English
    english_text = translate_telugu_to_english(telugu_text)

    # Step 2: Convert translated English text to speech (audio)
    if english_text:
        output_file = f"english_audio_{i}.mp3"  # Output audio file (differentiating names)
        text_to_speech(english_text, output_file)
