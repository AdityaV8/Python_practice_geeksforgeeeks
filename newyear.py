import pyfiglet

def new_year_wish():
    text = "Happy New Year 2026"
    
    ascii_art = pyfiglet.figlet_format(
        text,
        font="slant"   
    )
    
    print(ascii_art)
    print("🎆 Wishing you a year full of happiness, success, and good health! 🎆")


new_year_wish()
