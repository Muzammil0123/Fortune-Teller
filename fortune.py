
import random
import os

def main():
    print("🔮 Welcome to Muzammil Hussain's Fortune Teller (21JE0862) 🔮")
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        mood = "happy"  # Default mood for CI/CD run
        print("Running in CI environment: Defaulting mood to 'happy'")
    else:
    
        mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()

        fortunes = {
            "happy": [
                "✨ Your fortune: Great things await you, Muzammil! Keep smiling. ✨",
                "🌟 Muzammil you radiate positivity—this will attract amazing opportunities!"
            ],
            "sad": [
                "💫 Things may feel heavy now Muzammil, but brighter days are coming soon.",
                "🌈 Even the darkest clouds pass—hold on tight Muzammil!"
            ],
            "neutral": [
                "🌤️ A calm day brings peaceful surprises Muzammil.",
                "🌀 Muzammil,the universe is watching—prepare for something interesting today."
            ],
            "stressed": [
                "🧘 Take a deep breath, Muzammil. Peace is just around the corner.",
                "🫶 Stress fades, strength stays. You got this Muzammil!"
            ]
        }

        if mood in fortunes:
            print(random.choice(fortunes[mood]))
        else:
            print("😕 Sorry, I couldn't recognize that mood. Try happy, sad, neutral, or stressed.")

if __name__ == "__main__":
    main()

