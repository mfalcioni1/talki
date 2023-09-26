import pyttsx3

def text_to_speech_pyttsx3(text, rate: int = 150, volume: float = 0.9):
    engine = pyttsx3.init()
    
    # Optionally set properties like volume and speaking rate.
    engine.setProperty('rate', rate)  # Speed of speech. Higher means faster.
    engine.setProperty('volume', volume)  # Volume level. Range: 0.0 to 1.0.
    
    engine.say(text)
    engine.runAndWait()

# load text from script.txt
def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--script', '-s', type=str, default="script.txt")
    parser.add_argument('--rate', '-r', type=int, default=150)
    parser.add_argument('--volume', '-v', type=float, default=0.9)

    args = parser.parse_args()

    script = load_text_from_file(args.script)
    text_to_speech_pyttsx3(script, args.rate, args.volume)

if __name__ == "__main__":
    main()