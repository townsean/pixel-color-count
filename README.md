# pixel-color-count

Companion blog post: https://www.thecodingcouple.com/counting-pixels-by-color-in-python-with-pillow-a-pil-fork/

## Synopsis

Pixel Color Count is a Python script that sums the total number of pixels per a unique color.

![sample output for pixel-color-count.py](sample-output.png "Sample output for pixel-color-count.py")

## Motiviatation

I'm a [maker](https://www.ashleygrenon.com/project-gallery/) and love creating [8-bit art](https://www.ashleygrenon.com/tag/8-bit/), mostly with wood. I have a new project in the works where I need an exact count of each pixel per a color. I started to manually count them before I stopped myself and thought, *why don't I just write a script to automate this*!? Thus [pixel-color-count.py](https://github.com/townsean/pixel-color-count/blob/master/pixel-color-count.py) was born!

## Sample Usage
```
python pixel-color-count.py supermario3-8-bit-boo.png -i (0,255,255)
```

## Sample Output

In addtional to displaying the color with the number of pixels, pixel-color-count.py will generate an image feature a legend of the color, color name (if applicable) or color in (r, g, b) format, and the pixel count. 

![sample output for pixel-color-count.py](sample-legend.png "Sample output for pixel-color-count.py")

## Command Line Options

```
-i <RGB value as a tuple>
--ignore-color <RGB value as a tuple>
```
Skip counting pixels of this color. Currently only supports one tuple, should be a quick change to upgrade it support a list of tuples. 


```
-t <title>
--title <title>
```
Title for the image legend [**Not implemented**]

## Built With

Dependencies for the script are:
* [Pillow, the friendly fork of PIL](https://python-pillow.org/) for basic image manipulation
* [webcolors](https://pypi.org/project/webcolors/) for displaying human readable color names for RGB values when possible


## Maintainers

* [Ashley Grenon - @townsean](https://github.com/townsean)

## License (MIT)

MIT License

Copyright (c) 2019 Ashley Grenon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
