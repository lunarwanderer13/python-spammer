try:
    import keyboard
    import time
    import os
    from colored import fg, bg, attr
except ModuleNotFoundError as err:
    print(f'{fg(196)}{err}{attr(0)}')

def displayTitle() -> None:
    time.sleep(1)

    print(f'{bg(233)}{fg(225)}------------+------------{attr(0)}')
    print(f'{bg(233)}{fg(225)}|      Spam  Typer      |{attr(0)}')
    print(f'{bg(233)}{fg(225)}|        made by        |{attr(0)}')
    print(f'{bg(233)}{fg(225)}|     LunarWanderer     |{attr(0)}')
    print(f'{bg(233)}{fg(225)}------------+------------{attr(0)}')

    time.sleep(1)
    os.system('cls')
    time.sleep(0.25)

def onEscPress(event) -> None:
    if keyboard.is_pressed('esc'):
        print(f'{fg(160)}\"esc" has been pressed, exiting...{attr(0)}')
        os._exit(0)

def main() -> None:
    try:
        keyboard.write(text, textTypeSpeed)
        print(f'{fg(45)}\"{text}\" has been written{attr(0)}')
        time.sleep(textSendDelay)
        keyboard.press_and_release('enter')
        print(f'{fg(219)}\"enter\" has been pressed{attr(0)}')
        time.sleep(textStartDelay)
    except Exception as err:
        print(f'{fg(196)}{err}{attr(0)}')

if __name__ == '__main__':
    displayTitle()

    text: str = input(f'{fg(27)}Text to spam: {attr(0)}') or '.' # Text to type
    startDelay: float = float(input(f'{fg(99)}Start Delay (defaults to 5s): {attr(0)}') or '5.0') # Time before the program starts working
    textTypeSpeed: float = float(input(f'{fg(99)}Text Type Speed (defaults to 0.001s): {attr(0)}') or '0.001') # Time between typing characters
    textSendDelay: float = float(input(f'{fg(99)}Text Send Delay (defaults to 0.125s): {attr(0)}') or '0.125') # Time before sending the message
    textStartDelay: float = float(input(f'{fg(99)}Text Start Delay (defaults to 0.25s): {attr(0)}') or '0.25') # Time before starting to type another message

    time.sleep(startDelay)

    try:
        keyboard.on_press_key('esc', onEscPress)
        while True:
            main()
    except KeyboardInterrupt:
        pass
    finally:
        keyboard.unhook_all()

    keyboard.wait('esc')
