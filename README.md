# Q10 blackberry keyboard

Micropython implementation of blackberry Q10 keyboard interface to esp32-wroom board.

I'm using the following breakout board for conneting the keyboard to the esp32:
https://github.com/arturo182/bbq10kbd_breakout

- **Sym** button swithes to symbols (and digits)
- Either of the **Shift** keys switches to capital letters
- **Alt** key switches to cyrillic keyboard.

## Todo

- Fix 'backspace' issue in terminal.
- Connect oled ssd1306 display for text on screen, instead in the terminal
- Implement button interrupts instead of regular looping through the key matrix.

