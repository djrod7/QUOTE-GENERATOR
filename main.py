import random

quotes = [
    "In the middle of difficulty lies opportunity. -Albert Einstein",
    "In the end, it's not the years in your life that count. It's the life in your years. -Abraham Lincoln",
    "Whether you think you can, or you think you can't, you're right. -Henry Ford",
    "For we walk by faith, not by sight. -2 corinthians 5:7",
    "Keep your heart with diligence, For out of it spring the issues of life. -Proverbs 4:23"
]

def get_random_quote():
    return random.choice(quotes)

if __name__ == "__main__":
    print("\n--- Your Daily Inspiration ---")
    print(get_random_quote())
    print("=" *35)