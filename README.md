# Green Screen Replacer
## Description
This repository contains a program that performs background replacement for an input image captured using a green screen. 
The program allows the user to choose the output path for the resulting image.
It utilizes image processing techniques to replace the green background with a new background image of your choice.
  </br>**The project was created as part of an image processing course.**

## Environment
  - Operating System: Windows/macOS
  - Development Environment: PyCharm
  - Language: Python
  - Required Packages: cv2, numpy
  
  Please make sure you have the following packages installed before running the program.

## How to Run

To run the program, follow the steps below:

1. Format to run on the command line:
   ```shell
   python main.py <path of the input image> <path of the background image> <path of the output image>
   ```
   Example:
   ```shell
   python main.py input_image.jpg background_image.jpg output_image.jpg
   ```

2. The program will process the input image, replace the green background with the provided background image, and save the resulting image to the specified output path.

3. Check the output image at the specified output path to see the background-replaced image.

## Authors
- [Gil Ben Hamo](https://github.com/gilbenhamo)
- Yovel Aloni
---
Enjoy experimenting with the green screen replacer and create stunning images with new backgrounds!

