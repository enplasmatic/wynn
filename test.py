import pygame
import sys
import keyboard
pygame.init()

# --- Display and Colors ---
WIDTH, HEIGHT = 1000, 250
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MacBook Pro Keyboard Visualizer")

BG_COLOR = (30, 30, 30)
KEY_COLOR = (200, 200, 200)
KEY_PRESSED_COLOR = (0, 150, 250)
BORDER_COLOR = (50, 50, 50)


TEXT_COLOR = (0, 0, 0)

font = pygame.font.SysFont("menlo", 12)

# --- Layout parameters ---
KEY_HEIGHT = 40*0.5
KEY_GAP = 5
start_y = 20

# Define rows as lists of (label, width) tuples.
rows = [
    # Row 0: Top row – Esc, backtick, numbers, minus, equals, Delete
    [("Esc", 50), ("`", 40), ("1", 40), ("2", 40), ("3", 40), ("4", 40),
     ("5", 40), ("6", 40), ("7", 40), ("8", 40), ("9", 40), ("0", 40),
     ("-", 40), ("=", 40), ("Delete", 70)],
    # Row 1: Tab row with Q - \
    [("Tab", 60), ("Q", 40), ("W", 40), ("E", 40), ("R", 40), ("T", 40),
     ("Y", 40), ("U", 40), ("I", 40), ("O", 40), ("P", 40), ("[", 40),
     ("]", 40), ("\\", 40)],
    # Row 2: Caps row with A - Return
    [("Caps", 70), ("A", 40), ("S", 40), ("D", 40), ("F", 40), ("G", 40),
     ("H", 40), ("J", 40), ("K", 40), ("L", 40), (";", 40), ("'", 40),
     ("Return", 90)],
    # Row 3: Shift row with Z - Shift
    [("lShift", 90), ("Z", 40), ("X", 40), ("C", 40), ("V", 40), ("B", 40),
     ("N", 40), ("M", 40), (",", 40), (".", 40), ("/", 40), ("rShift", 90)],
    # Row 4: Bottom row with Ctrl, lOpt, lCmd, Space, rCmd, rOpt, Ctrl
    [("Ctrl", 60), ("lOpt", 60), ("lCmd", 70), ("Space", 300),
     ("rCmd", 70), ("rOpt", 60), ("Ctrl", 60)]
]

# --- Mapping labels to pygame key codes ---
def get_key_codes(label):
    mapping = {
         "Esc": [pygame.K_ESCAPE],
         "`": [pygame.K_BACKQUOTE],
         "1": [pygame.K_1],
         "2": [pygame.K_2],
         "3": [pygame.K_3],
         "4": [pygame.K_4],
         "5": [pygame.K_5],
         "6": [pygame.K_6],
         "7": [pygame.K_7],
         "8": [pygame.K_8],
         "9": [pygame.K_9],
         "0": [pygame.K_0],
         "-": [pygame.K_MINUS],
         "=": [pygame.K_EQUALS],
         "Delete": [pygame.K_BACKSPACE],
         "Tab": [pygame.K_TAB],
         "Q": [pygame.K_q],
         "W": [pygame.K_w],
         "E": [pygame.K_e],
         "R": [pygame.K_r],
         "T": [pygame.K_t],
         "Y": [pygame.K_y],
         "U": [pygame.K_u],
         "I": [pygame.K_i],
         "O": [pygame.K_o],
         "P": [pygame.K_p],
         "[": [pygame.K_LEFTBRACKET],
         "]": [pygame.K_RIGHTBRACKET],
         "\\": [pygame.K_BACKSLASH],
         "Caps": [pygame.K_CAPSLOCK],
         "A": [pygame.K_a],
         "S": [pygame.K_s],
         "D": [pygame.K_d],
         "F": [pygame.K_f],
         "G": [pygame.K_g],
         "H": [pygame.K_h],
         "J": [pygame.K_j],
         "K": [pygame.K_k],
         "L": [pygame.K_l],
         ";": [pygame.K_SEMICOLON],
         "'": [pygame.K_QUOTE],
         "Return": [pygame.K_RETURN],
         "lShift": [pygame.K_LSHIFT],
         "rShift": [pygame.K_RSHIFT],
         "Z": [pygame.K_z],
         "X": [pygame.K_x],
         "C": [pygame.K_c],
         "V": [pygame.K_v],
         "B": [pygame.K_b],
         "N": [pygame.K_n],
         "M": [pygame.K_m],
         ",": [pygame.K_COMMA],
         ".": [pygame.K_PERIOD], 
         "/": [pygame.K_SLASH],
         "Ctrl": [pygame.K_LCTRL, pygame.K_RCTRL],
         "lOpt": [pygame.K_LALT],
         "rOpt": [pygame.K_RALT],
         "lCmd": [pygame.K_LMETA],
         "rCmd": [pygame.K_RMETA],
         "Space": [pygame.K_SPACE]
    }
    return mapping.get(label, [])

# --- Build key objects with positions ---
keys = []
current_y = start_y
for row in rows:
    current_x = 20  # left margin
    for (label, key_width) in row:
        key_width *= 0.6
        rect = pygame.Rect(current_x, current_y, key_width, KEY_HEIGHT)
        key_obj = {
            "label": label,
            "rect": rect,
            "codes": get_key_codes(label),
            "is_pressed": False
        }
        keys.append(key_obj)
        current_x += key_width + KEY_GAP
    current_y += KEY_HEIGHT + KEY_GAP

# --- Add Arrow Keys Cluster ---
# We'll create a 2-row cluster: Up arrow on top, then Left, Down, Right.
arrow_key_width = 20
arrow_key_height = 20
arrow_gap = 5

# Position the arrow cluster in the bottom-right area of the window.
cluster_left = 200  # adjust this to move cluster horizontally
bottom_y = 180              # base y for the bottom row of arrow keys

# Calculate positions:
up_x = cluster_left + arrow_key_width+5  # center the up arrow above the 3 keys below
up_y = bottom_y - arrow_key_height - arrow_gap

left_x = cluster_left
left_y = bottom_y
down_x = cluster_left + arrow_key_width + arrow_gap
down_y = bottom_y
right_x = cluster_left + 2*(arrow_key_width + arrow_gap)
right_y = bottom_y

NOframe = True

SHIFTS = {
    "`": "~",
    "1": "!",
    "2": "@",
    "3": "#",
    "4": "$",
    "5": "%",
    "6": "^",
    "7": "&",
    "8": "*",
    "9": "(",
    "0": ")",
    "-": "_",
    "=": "+",
    "[": "{",
    "]": "}",
    "\\": "|",
    ";": ":",
    "'": "\"",
    ",": "<",
    ".": ">",
    "/": "?"
}

# Append arrow keys to the keys list.
keys.append({
    "label": "↑",
    "rect": pygame.Rect(up_x, up_y, arrow_key_width, arrow_key_height),
    "codes": [pygame.K_UP],
    "is_pressed": False
})
keys.append({
    "label": "←",
    "rect": pygame.Rect(left_x, left_y, arrow_key_width, arrow_key_height),
    "codes": [pygame.K_LEFT],
    "is_pressed": False
})
keys.append({
    "label": "↓",
    "rect": pygame.Rect(down_x, down_y, arrow_key_width, arrow_key_height),
    "codes": [pygame.K_DOWN],
    "is_pressed": False
})
keys.append({
    "label": "→",
    "rect": pygame.Rect(right_x, right_y, arrow_key_width, arrow_key_height),
    "codes": [pygame.K_RIGHT],
    "is_pressed": False
})

clock = pygame.time.Clock()
Shift = False

# --- Main Loop ---
while True:
    toggle = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if keyboard.is_pressed('shift'):
        Shift = True
        if keyboard.is_pressed('enter'):
            toggle = True
    else:
        Shift = False
        
    # Check each key and update pressed state
    for key_obj in keys:
        key_pressed = False
        for code in key_obj["codes"]:
            # Convert pygame key code to keyboard library name
            key_name = pygame.key.name(code, False)
            try:
                val = ord(get_key_codes(code)[0])
                if keyboard.is_pressed(val):
                    key_pressed = True
                    key_obj["fade_progress"] = 1.0
                    break
            except IndexError:
                pass
                
        key_obj["is_pressed"] = key_pressed
    if toggle:
        NOframe = not NOframe
        if NOframe:
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
        else:
            screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # --- Drawing ---
    screen.fill(BG_COLOR)
    for key_obj in keys:
        if key_obj["is_pressed"]:
            color = KEY_PRESSED_COLOR
        else:
            # If key was previously pressed, gradually fade back to KEY_COLOR
            if "fade_progress" not in key_obj:
                key_obj["fade_progress"] = 1.0
            
            if key_obj["fade_progress"] > 0:
                # Interpolate between pressed and normal color
                r = KEY_PRESSED_COLOR[0] + (KEY_COLOR[0] - KEY_PRESSED_COLOR[0]) * (1 - key_obj["fade_progress"])
                g = KEY_PRESSED_COLOR[1] + (KEY_COLOR[1] - KEY_PRESSED_COLOR[1]) * (1 - key_obj["fade_progress"]) 
                b = KEY_PRESSED_COLOR[2] + (KEY_COLOR[2] - KEY_PRESSED_COLOR[2]) * (1 - key_obj["fade_progress"])
                color = (int(r), int(g), int(b))
                key_obj["fade_progress"] -= 0.1  # Adjust fade speed
            else:
                color = KEY_COLOR
                key_obj["fade_progress"] = 0
        pygame.draw.rect(screen, color, key_obj["rect"])
        pygame.draw.rect(screen, BORDER_COLOR, key_obj["rect"], 2)
        # Center the label text in the key.
        h = key_obj["label"]
        if (Shift) and (key_obj["label"] in SHIFTS):
            h = SHIFTS[key_obj["label"]]
        text_surface = font.render(h, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=key_obj["rect"].center)
        screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(60)
