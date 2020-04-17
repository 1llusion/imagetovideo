# Image To Video

A simple image to video converter.

### Installation

```sh
$ pip install imagetovideo
```

### Preparation
- Ensure all images have numerical names
```sh
1.jpg, 2.jpg, 3.jpg...
```
- Prefixes and multiple prefixes are supported
```sh
foo1.jpg, foo2.jpg, bar3.jpg, bar4.jpg
```
### Basic Usage 
```sh
from imagetovideo import ImageToVideo

ImageToVideo.convert(INPUT_DIRECTORY, OUTPUT_FILE_NAME.avi)
```
### Supported Arguments
```sh
ImageToVideo.convert(dir_in, # Input directory containing sequence of images
                     out, # Output path + file. Has to include '.avi' extenion (example.avi)
                     prefix="", # File prefix, string or a list: "foo" or ["foo", "bar"]
                     first_image=0, # Number of first image: 0 if first image is named 0.jpg, 1 if 1.jpg
                     extension=".jpg", # Image extensions
                     fps=30, # FPS of output video
                     delete_files=False # Boolean. Delete all images in the input folder?
                     )
```