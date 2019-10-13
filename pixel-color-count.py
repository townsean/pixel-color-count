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

    args = parser.parse_args()
    ignore_color = literal_eval(args.ignore_color)
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
    legend_img = Image.new("RGBA", (200, len(color_count) * (rect_width + rect_outline_width + margin)))
    draw = ImageDraw.Draw(legend_img)
    font = ImageFont.truetype("arialbd.ttf", 20)
    for color, count in color_count.items():
        if color == ignore_color:
            continue

        try:
            color_name = webcolors.rgb_to_name(color)
        except ValueError:                
            color_name = color
        
        print('{}.) {}: {}'.format(color_index, color_name, count))        

        # draw square for color legend
        y0 = rect_width * (color_index - 1) + margin * color_index
        y1 = rect_width * color_index + margin * color_index
        draw.rectangle([(0, y0), (rect_width, y1)], fill=color, outline="black", width=2)

        # draw text for legend
        draw.text((rect_width + margin, y0), "{}: {}".format(color_name, count), font=font, fill="black")

        color_index += 1

    legend_img.save('legend.png', mode="w")

if __name__ == '__main__':
    main()