import pyttsx3




# to work this code you need to install pyttsx3 : pip install pyttsx3


def text_to_speech():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Optional: Configure voice properties
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 25)  # Slightly slower for clarity
    
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume)  # 0.0 to 1.0
    
    print("=" * 50)
    print("Text to Speech Converter")
    print("=" * 50)
    
    # Get text input from user
    text = input("\nEnter text to convert to speech: ")
    
    # Check if input is empty
    if not text.strip():
        print("No text entered!")
    else:
        # Convert text to speech
        print(f"Speaking: {text}")
        engine.say(text)
        engine.runAndWait()
        print("Done!")
    
    # Stop the engine
    engine.stop()

if __name__ == "__main__":
    try:
        text_to_speech()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Make sure pyttsx3 is installed: pip install pyttsx3")