import os,sys
import keyboard
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


pygame.mixer.init()

def resource(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

enter_sound = pygame.mixer.Sound(resource(os.path.join("assets", "ducky.mp3")))
allkeys_sound = pygame.mixer.Sound(resource(os.path.join("assets", "duck.mp3")))

def play_key(key):
    if key.name == "enter":
        enter_sound.play()
    else:
        allkeys_sound.play()

def main():
    print("You have unleashed the superpower of duck typing")
    keyboard.on_press(play_key)  
    keyboard.wait() 
    keyboard.unhook_all()

if __name__ == "__main__":
    main()
