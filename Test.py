import random
import tkinter as tk
from tkinter import filedialog
from PIL import Image as im, ImageTk, ImageOps


def get_original_images(NumberOfImages):
    Image_Array = []
    for i in range(1, NumberOfImages + 1):
        Image_path = "Image" + str(i) + ".jpg"
        Image = im.open(Image_path)
        Image_Array.append(Image)
    return Image_Array


def adjust_size(Image_Array):
    new_images = []
    new_size = (150, 150)
    for pic in Image_Array:
        resized_image = pic.resize(new_size)
        new_images.append(resized_image)
    return new_images


def generate_image_grid(images_list):
    image_size = 150
    grid_size = 3
    total_size = grid_size * image_size
    grid_image = im.new("RGB", (total_size, total_size))

    for index, pic in enumerate(images_list):
        x_offset = (index % grid_size) * image_size
        y_offset = (index // grid_size) * image_size
        grid_image.paste(pic, (x_offset, y_offset))

    return grid_image


def update_image():
    global current_grid
    random.shuffle(resized_images)
    current_grid = generate_image_grid(resized_images)
    tk_image = ImageTk.PhotoImage(current_grid)
    label.config(image=tk_image)
    label.image = tk_image


def save_image():
    global current_grid
    if current_grid:
        options = {
            'defaultextension': '.jpg',
            'filetypes': [('JPEG files', '.jpg'), ('All files', '.*')],
            'title': 'Save Current Permutation'
        }
        save_path = filedialog.asksaveasfilename(**options)

        if save_path:
            current_grid.save(save_path)
            print(f"Saved current permutation as {save_path}")


# Initialize Tkinter window
root = tk.Tk()
root.title("Image Permutator")
root.configure(bg='lightgray')  # Set background color of the window

# Preload and resize images
resized_images = adjust_size(get_original_images(9))

# Create initial image and label
initial_grid = generate_image_grid(resized_images)
initial_tk_image = ImageTk.PhotoImage(initial_grid)
current_grid = initial_grid

label = tk.Label(root, image=initial_tk_image, bg='lightgray')
label.grid(row=0, columnspan=2)  # Use grid instead of pack

# Create buttons and add them to the grid
button_new = tk.Button(root, text="Generate New Permutation", command=update_image, bg='lightblue', fg='white')
button_new.grid(row=1, column=0)  # Place button in the grid

button_save = tk.Button(root, text="Save Current Permutation", command=save_image, bg='lightgreen', fg='white')
button_save.grid(row=1, column=1)  # Place button in the grid

root.mainloop()
