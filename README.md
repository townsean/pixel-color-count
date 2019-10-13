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

## Command Line Options

```
-i <RGB value>
--ignore-color
```
Skip counting pixels of this color **[Not implement]** (ran into some technical difficulties, will revisit when time permits) 


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
