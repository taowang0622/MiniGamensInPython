# implementation of card game - Memory

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random


# helper function to initialize globals
def new_game():
    global cards, exposed
    global state
    global turns
    
    cards = range(8) * 2
    random.shuffle(cards)
    exposed = [False] * 16
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
 
     
# define event handlers
def mouseclick(pos):
    global exposed
    global card_one_index, card_two_index
    global state
    global turns

    card_clicked = pos[0] // 50
    if exposed[card_clicked] == False:
        if state == 0:
            card_one_index = card_clicked
            exposed[card_clicked] = True
            state = 1
        elif state == 1:
            card_two_index = card_clicked
            exposed[card_clicked] = True
            state = 2
            turns += 1
            label.set_text("Turns = " + str(turns))
        else:
            if cards[card_one_index] != cards[card_two_index]:
                exposed[card_one_index] = False
                exposed[card_two_index] = False
            card_one_index = card_clicked
            exposed[card_clicked] = True
            state = 1


# cards are logically 50x100 pixels in size    
def draw(canvas):
    for card_index in range(len(cards)):
        card_pos = [50 * card_index, 78]
        canvas.draw_text(str(cards[card_index]), (card_pos[0]+5, card_pos[1]), 
                         80, 'White')
        if not exposed[card_index]:
            canvas.draw_line((card_pos[0] + 25, 0), (card_pos[0] + 25, 100), 
                              49, 'Green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
