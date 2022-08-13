import pyttsx3
import os

from typing import Tuple, List


QUOTES_FILE = "Your path to file"


def get_quote(path: str) -> Tuple[str, str]:
    
    with open(path, "r") as f:

        lines = f.read().split("\n")
        n = int(lines[0])

        if lines[-1] == "":
            lines.pop()


    # --- Update ordinal number of current quote
    with open(path, "w") as f:

        if n >= len(lines):
            n = 1

        f.write(str(n + 1))
        f.write("\n")

        for line in lines[1:]:

            if line == "":
                continue

            f.write(line + "\n")

    
    author, quote = lines[n].split(";")
    return author, quote



if __name__ == "__main__":

    author, quote = get_quote(QUOTES_FILE)

    speaker = pyttsx3.init()
    speaker.setProperty("rate", 110)
    voices = speaker.getProperty("voices")
    speaker.setProperty('voice', voices[1].id)


    speaker.say("Hello Adam!")
    speaker.say(f"{author} once said ... {quote}")
    speaker.say("I hope this thought will be helpful today")

    speaker.runAndWait()
