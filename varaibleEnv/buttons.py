from components.Buttons import Button
import pygame


def resize_image(image, max_width, max_height):
    """Resize the image while maintaining the aspect ratio."""
    width, height = image.get_size()
    aspect_ratio = width / height

    if width / max_width > height / max_height:
        new_width = max_width
        new_height = int(max_width / aspect_ratio)
    else:
        new_height = max_height
        new_width = int(max_height * aspect_ratio)

        return pygame.transform.scale(image, (new_width, new_height))
    return image


def CreateButtonList(image_list, star_point, scale, number_per_line, space_left, space_bottom):
    button_list = []
    x = star_point[0]
    y = star_point[1]
    number = 0

    for img, filename in image_list:
        resized_image = resize_image(img, 30, 30)  # Resize the image
        element = Button(x, y, resized_image, scale)
        x += 10 + space_left
        number += 1
        if number == number_per_line:
            number = 0
            y += 10 + space_bottom
            x = star_point[0]
        button_list.append(element)

    return button_list


def Draws(button_list, sur):
    for button in button_list:
        button.draw(sur)

def DrawBOXS(button_list, sur, image, star, number, space_lef, space_bottom, scale):
    x = star[0]
    y = star[1]
    n = 0
    for _ in button_list:
        sur.blit(image, (x, y))
        x += image.get_width()+space_lef
        n += 1
        if n == number:
            n = 0
            x = star[0]
            y += image.get_height() + space_bottom

