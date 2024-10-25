import os
import csv
from pygame import QUIT
import pickle
from varaibleEnv import *
from varaibleEnv.buttons import *
from varaibleEnv.load_tiles import Load_Tiles, load_images
from components.Buttons import Layer

# initialize the needed module
pygame.init()

logo_button = Button(16, 16, LOGO, 1)

# # draw grid
# def draw_grid(screen, scroll, scroll_v):
#     # Calculate the center of the screen
#     center_x = WIDTH // 2
#     center_y = HEIGTH // 2
#
#     # Calculate how many tiles can fit on either side of the center
#     half_cols = MAX_COLS // 2
#     half_rows = MAX_ROWS // 2
#
#     # Draw vertical lines (left and right of the center)
#     for c in range(-half_cols, half_cols + 1):
#         x_pos = center_x + (c * TILE_SIZE) - scroll
#         pygame.draw.line(screen, E_ORANGE, (x_pos, 0), (x_pos, HEIGTH), 2)
#
#     # Draw horizontal lines (up and down of the center)
#     for r in range(-half_rows, half_rows + 1):
#         y_pos = center_y + (r * TILE_SIZE) - scroll_v
#         pygame.draw.line(screen, E_ORANGE, (0, y_pos), (WIDTH, y_pos), 2)

# draw grid
def draw_grid(screen, scroll, scroll_v):
    # Start drawing from position (0, 0)

    # Draw vertical lines (from left to right of the screen)
    for c in range(0, MAX_COLS//2 + 1):
        x_pos = (c * TILE_SIZE) - scroll
        pygame.draw.line(screen, E_ORANGE, (x_pos, 0), (x_pos, HEIGTH), 2)

    for c in range(-MAX_COLS//2, 0):
        x_pos = (c * TILE_SIZE) - scroll
        pygame.draw.line(screen, E_ORANGE, (x_pos, 0), (x_pos, HEIGTH), 2)

    # Draw horizontal lines (from top to bottom of the screen)
    for r in range(0, MAX_ROWS //2 + 1):
        y_pos = (r * TILE_SIZE) - scroll_v
        pygame.draw.line(screen, E_ORANGE, (0, y_pos), (WIDTH, y_pos), 2)

    for r in range(-MAX_ROWS//2, 0):
        y_pos = (r * TILE_SIZE) - scroll_v
        pygame.draw.line(screen, E_ORANGE, (0, y_pos), (WIDTH, y_pos), 2)


def enviroment(sur):
    run = True
    scroll_left = False
    scroll_right = False
    scroll_up = False
    scroll_down = False
    scroll_side_y_up = False
    scroll_side_y_down = False
    scroll = 0
    scroll_v = 0
    scroll_speed = 1
    scroll_side_y = 0
    image_list = load_images(IMAGE_LOCATION)
    button_list = CreateButtonList(image_list, (962, 17), 1, 3, 28, 67)
    save_button = Button(26, 556, SAVE2, 1)
    load_button = Button(26, 636, LOAD2, 1)
    menu_display = False
    menu_button = Button(26, 38, MENU, 1)
    menu_option1 = Button(43, 49, MENU1, 1)
    menu_option2 = Button(43, 89, MENU2, 1)
    menu_option3 = Button(43, 129, MENU3, 1)
    menu_option4 = Button(43, 169, MENU4, 1)

    # Initialize layers
    world_data = [[[None for _ in range(MAX_COLS)] for _ in range(MAX_ROWS)] for _ in range(10)]
    active_layer = 1

    def draw_world():
        for layer in world_data:  # Iterate over all layers
            for y in range(MAX_ROWS):
                for x in range(MAX_COLS):
                    tile = layer[y][x]
                    if tile is not None:
                        sur.blit(image_list[tile][0], (x * TILE_SIZE - scroll, y * TILE_SIZE - scroll_v))

    layer_list = []
    lay_x = 456
    lay_y = 576
    x = lay_x
    y = lay_y
    for i in range(1, 11):
        layer = Layer(x, y, [LAYERS[f'LAYER{i}'], LAYERS[f'LAYER{i}S']], 1, i)
        if i == 5:
            x = lay_x
            y += (9 + layer.height)
        else:
            x += (24 + layer.width)
        if i == 1:
            layer.active = True
        layer_list.append(layer)

    current_tile = 0

    while run:

        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type == QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    run = False
                if e.key == pygame.K_LEFT:
                    scroll_left = True
                if e.key == pygame.K_RIGHT:
                    scroll_right = True
                if e.key == pygame.K_UP:
                    scroll_up = True
                if e.key == pygame.K_DOWN:
                    scroll_down = True
                if e.key == pygame.K_w:
                    scroll_side_y_up = True
                if e.key == pygame.K_s:
                    scroll_side_y_down = True
                if e.key == pygame.K_TAB and not menu_display:
                    menu_display = True
                elif e.key == pygame.K_TAB and menu_display:
                    menu_display = False
                # Check if the Shift key is held down
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    scroll_speed = 10  # Increase scroll speed when Shift is pressed

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT:
                    scroll_left = False
                if e.key == pygame.K_RIGHT:
                    scroll_right = False
                if e.key == pygame.K_UP:
                    scroll_up = False
                if e.key == pygame.K_DOWN:
                    scroll_down = False
                if e.key == pygame.K_w:
                    scroll_side_y_up = False
                if e.key == pygame.K_s:
                    scroll_side_y_down = False

            # Mouse click event
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for layer in layer_list:
                    if layer.check_click(mouse_pos):  # Check if the layer was clicked
                        # Deactivate all layers
                        for l in layer_list:
                            l.active = False
                        # Activate the clicked layer
                        layer.active = True
                        active_layer = layer.number
                        break  # No need to check further once clicked

            # Add new tiles to the screen
            pos = pygame.mouse.get_pos()
            # Calculate tile position
            x = (pos[0] + scroll) // TILE_SIZE
            y = (pos[1] + scroll_v) // TILE_SIZE

            # Check that the coordinates are within the tile area
            if pos[0] < 940 and pos[1] < 546:
                # Ensure active_layer is within bounds
                if 1 <= active_layer <= 10:
                    current_layer = world_data[active_layer - 1]  # Get the active layer
                    # Allow negative x and y to be valid indices
                    if -MAX_COLS < x < MAX_COLS and -MAX_ROWS < y < MAX_ROWS:
                        # Adjust x and y to fit the layer's indices if negative
                        adjusted_x = x + MAX_COLS if x < 0 else x
                        adjusted_y = y + MAX_ROWS if y < 0 else y

                        # Check bounds again after adjustment
                        if 0 <= adjusted_x < MAX_COLS and 0 <= adjusted_y < MAX_ROWS:
                            if pygame.mouse.get_pressed()[0] == 1:  # Left click
                                if current_layer[adjusted_y][adjusted_x] != current_tile:
                                    current_layer[adjusted_y][adjusted_x] = current_tile
                                    print(current_tile)
                            if pygame.mouse.get_pressed()[2] == 1:  # Right click
                                current_layer[adjusted_y][adjusted_x] = None

        # Scrolling logic

        # Left scrolling (don't go past the leftmost side)
        if scroll_left and scroll > -(MAX_COLS//2) * TILE_SIZE:
            scroll -= 5 * scroll_speed

        # Right scrolling (don't go past the rightmost side)
        if scroll_right and scroll < (MAX_COLS//2) * TILE_SIZE:
            scroll += 5 * scroll_speed

        # Up scrolling (don't go past the topmost side)
        if scroll_up and scroll_v > -(MAX_ROWS//2) * TILE_SIZE:
            scroll_v -= 5 * scroll_speed

        # Down scrolling (don't go past the bottommost side)
        if scroll_down and scroll_v < (MAX_ROWS//2) * TILE_SIZE:
            scroll_v += 5 * scroll_speed

        if scroll_side_y_up:
            scroll_side_y -= 1 * scroll_speed
        if scroll_side_y_down:
            scroll_side_y += 1 * scroll_speed

        sur.fill((180, 180, 180))

        # Choose a tile
        button_count = 0
        for button_count, i in enumerate(button_list):
            if i.draw(sur):
                current_tile = button_count

        draw_world()  # Draw the world after placing tiles
        draw_grid(sur, scroll, scroll_v)
        sur.blit(BOTTOM, (0, 546))
        sur.blit(SIDE, (940, 0))

        # Update buttons with scroll_side_y applied
        for button in button_list:
            button.update(scroll_side_y)

        DrawBOXS(button_list, sur, BOX, (952, 14+scroll_side_y), 3, 9, 61, 1)
        Draws(button_list, sur)
        # highlight the selected tile
        pygame.draw.rect(sur, (255, 0, 0), button_list[current_tile].rect, 5)
        if menu_display:
            menu_button.draw(sur)
            menu_option1.draw(sur)
            menu_option2.draw(sur)
            menu_option3.draw(sur)
            menu_option4.draw(sur)
        logo_button.draw(sur)

        save_button.draw(sur)
        load_button.draw(sur)

        # Save logic
        if save_button.clicked:
            save_button.clicked = False
            for layer_index, layer in enumerate(world_data):
                # Check if the layer is not empty
                if any(tile is not None for row in layer for tile in
                       row):  # Check if there's at least one non-None tile
                    # Save as .EE file
                    file_name_ee = f'output/layer_{layer_index + 1}_data.EE'  # Ensure file extension is .pkl
                    with open(file_name_ee, 'wb') as pickle_out:  # Use with statement to handle file
                        pickle.dump(layer, pickle_out)  # Save the current layer data

                    # Save as CSV file
                    file_name_csv = f'output/layer_{layer_index + 1}_data.csv'
                    with open(file_name_csv, 'w', newline='') as csv_out:  # Use 'w' for writing
                        csv_writer = csv.writer(csv_out)
                        # Write each row of tiles
                        for row in layer:
                            csv_writer.writerow(row)

        # Load logic
        if load_button.clicked:
            load_button.clicked = False
            scroll = 0
            for layer_index in range(10):  # Assuming you have 10 layers
                # Load from .EE file if exists
                file_name_ee = f'output/layer_{layer_index + 1}_data.EE'
                if os.path.exists(file_name_ee):  # Check if the file exists
                    with open(file_name_ee, 'rb') as pickle_in:  # Open file for reading
                        current_layer = pickle.load(pickle_in)  # Load layer data
                        world_data[layer_index] = current_layer  # Update the world_data
                else:
                    print(f"Layer {layer_index + 1} EE file does not exist. Checking CSV.")

                # Load from CSV file if EE file does not exist
                # file_name_csv = f'output/layer_{layer_index + 1}_data.csv'
                # if not os.path.exists(file_name_ee) and os.path.exists(file_name_csv):
                #     with open(file_name_csv, 'r') as csv_in:  # Open file for reading
                #         csv_reader = csv.reader(csv_in)
                #         current_layer = []
                #         for row in csv_reader:
                #             # Convert row from string to the appropriate type (if needed)
                #             current_layer.append([int(tile) if tile else None for tile in row])
                #         world_data[layer_index] = current_layer  # Update the world_data
                # else:
                #     if not os.path.exists(file_name_csv):
                #         print(f"Layer {layer_index + 1} CSV file does not exist. Skipping.")

        sur.blit(LAYER, (436, 560))
        for _ in layer_list:
            if _.active:
                active_layer = _.number
            _.update()
            _.draw(sur)

        pygame.display.update()
