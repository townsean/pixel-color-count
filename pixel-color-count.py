# pixel-color-count.py - Gets a sum of pixels per unique color

import argparse
from ast import literal_eval

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit("This script requires the PIL module. Install with pip install Pillow")

try:
    import webcolors
except ImportError:
    # https://pypi.org/project/webcolors/
    exit("This script uses webcolors for displaying named colors. Install with pip install webcolors")

def count_pixels(filename):
    """
    Returns a count of pixels per a unique color

    Args:
        filename (str): the image to count the number of pixels of
    Returns:
        a key-value pairing of the rgb color value and the number of times the color was present in the image
    """
    color_count = {}
    with Image.open(filename) as image:
        width, height = image.size
        rgb_image = image.convert('RGB')

        # iterate through each pixel in the image and keep a count per unique color
        for x in range(width):
            for y in range(height):
                rgb = rgb_image.getpixel((x, y))

                if rgb in color_count:
                    color_count[rgb] += 1
                else:
                    color_count[rgb] = 1

    return color_count

def create_legend_image(filename, colors, title, ignore_color):
    """
    Create an image of color swatches paired with a color name and number

    Args:
        filename (str): the name of the legend image file
        colors (dict): a key-value pairing of the color name and count
        title (str): a title for the legend image
        ignore_color (tuple): do not add this color to the legend image
    Returns:
        None
    """
    margin = 10
    rect_width = 25
    rect_outline_width = 2
    font_size = 20
    img_width = 250
    img_height = len(colors) * (rect_width + rect_outline_width + margin) + (0 if title is None else font_size)
    legend_img = Image.new("RGBA", (img_width, img_height), "white")
    draw = ImageDraw.Draw(legend_img)    
    font = ImageFont.truetype("arialbd.ttf", font_size)
    
    # draw title for legend if applicable
    text_height = 0
    if title is not None:
        _, text_height = draw.textsize(title, font=font)
        draw.text((0, 0), title, font=font, fill="black")

    color_index = 1
    for color, count in colors.items():
        if color == ignore_color:
            continue

        try:
            # convert RGB color to a human readable color if applicable
            color_name = webcolors.rgb_to_name(color)
        except ValueError:                
            color_name = color

        # draw square for color legend
        y0 = rect_width * (color_index - 1) + margin * color_index + text_height
        y1 = rect_width * color_index + margin * color_index + text_height
        draw.rectangle([(0, y0), (rect_width, y1)], fill=color, outline="black", width=2)

        # draw color name next and pixel count for legend colors
        draw.text((rect_width + margin, y0), "{}: {}".format(color_name, count), font=font, fill="black")

        color_index += 1

    legend_img.save(filename, mode="w")

def main():
    parser = argparse.ArgumentParser(description='Calculates the sum of pixels per a color')
    parser.add_argument('image', nargs='?', default='.', help='The image to sum the pixels per a color of')
    parser.add_argument('-i', '--ignore-color', help='Skip counting pixels of this color')
    parser.add_argument('-t', '--title', help='Title for the image legend')
    parser.add_argument('-l', '--legend-image', help='Generate an image with color swatches paired with the pixel count')

    args = parser.parse_args()
    ignore_color = literal_eval(args.ignore_color) if args.ignore_color is not None else None
    color_count = count_pixels(args.image)                   

    if args.legend_image is not None:
        create_legend_image(args.legend_image, color_count, args.title, ignore_color)
 
    # outputs pixel color count to console
    print('Pixel Count per Unique Color:')
    print('-' * 30)
    color_index = 1

    for color, count in color_count.items(): 
        if color == ignore_color:
            continue

        try:
            # convert RGB color to a human readable color if applicable
            color_name = webcolors.rgb_to_name(color)
        except ValueError:                
            color_name = color

        print('{}.) {}: {}'.format(color_index, color_name, count))

        color_index += 1

    # Display the total number of pixels not ignored
    print('-' * 30)
    print('\t{} pixels'.format(sum(color_count[color] for color in color_count if color != ignore_color)))

if __name__ == '__main__':
    main()