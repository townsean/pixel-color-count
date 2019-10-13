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

def main():
    parser = argparse.ArgumentParser(description='Calculates the sum of pixels per a color')
    parser.add_argument('image', nargs='?', default='.', help='The image to sum the pixels per a color of')
    parser.add_argument('-i', '--ignore-color', help='Skip counting pixels of this color')
    parser.add_argument('-t', '--title', help='Title for the image legend')

    args = parser.parse_args()
    ignore_color = literal_eval(args.ignore_color) if args.ignore_color is not None else None
    color_count = {}

    with Image.open(args.image) as image:
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
                    
    # outputs pixel color count to console
    print('Pixel Count per Unique Color:')
    print('-' * 30)
    color_index = 1
    
    margin = 10
    rect_width = 25
    rect_outline_width = 2
    font_size = 20
    img_width = 250
    img_height = len(color_count) * (rect_width + rect_outline_width + margin) + (0 if args.title is None else font_size)
    legend_img = Image.new("RGBA", (img_width, img_height))
    draw = ImageDraw.Draw(legend_img)    
    font = ImageFont.truetype("arialbd.ttf", font_size)

    # draw title for legend if applicable
    text_width = text_height = 0
    if args.title is not None:
        text_width, text_height = draw.textsize(args.title, font=font)
        draw.text((0, 0), args.title, font=font, fill="black")

    for color, count in color_count.items():
        if color == ignore_color:
            continue

        try:
            # convert RGB color to a human readable color if applicable
            color_name = webcolors.rgb_to_name(color)
        except ValueError:                
            color_name = color
        
        print('{}.) {}: {}'.format(color_index, color_name, count))        

        # draw square for color legend
        y0 = rect_width * (color_index - 1) + margin * color_index + text_height
        y1 = rect_width * color_index + margin * color_index + text_height
        draw.rectangle([(0, y0), (rect_width, y1)], fill=color, outline="black", width=2)

        # draw color name next and pixel count for legend colors
        draw.text((rect_width + margin, y0), "{}: {}".format(color_name, count), font=font, fill="black")

        color_index += 1    

    legend_img.save('legend.png', mode="w")

if __name__ == '__main__':
    main()