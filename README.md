# Region Growing Algorithm README

## Table of Contents

1. [Installation and Execution](#installation-and-execution)
    1.1 [Windows](#windows)
    1.2 [Linux](#linux)
2. [8-Neighborhood](#8-neighborhood)
3. [Region Growing](#region-growing)
    3.1 [Different Methods](#different-methods)
    3.2 [Operation of Region Growing Functions](#operation-of-region-growing-functions)
        3.2.1 [Processed](#processed)
        3.2.2 [Timer](#timer)
        3.2.3 [Colors](#colors)
    3.3 [Image Filling](#image-filling)
4. [Manual Seed Input](#manual-seed-input)
    4.1 [Mouse Handling](#mouse-handling)
    4.2 [Image Display](#image-display)
    4.3 [Main Program](#main-program)
5. [Conclusion](#conclusion)

## Installation and Execution

This program requires Python 3 and the OpenCV and NumPy libraries. Here are the instructions for installing and running the program on both Windows and Linux.

### Windows

1. First, check if Python is installed on your system:

    python --version

   
2. If Python is not present, you can download the executable from [Python's official website](https://www.python.org/downloads/windows/) (Python 3.11.1).

3. Next, install the necessary libraries, OpenCV, and NumPy using the following commands:
   
    pip install opencv-python
   
    pip install numpy


4. Now, you have everything you need to run the program with the command:

  py main.py

### Linux

(Note: This section has been tested under WSL2)

1. First, check if Python is installed on your system:

     python --version

   
2. If it's not present, you can install it with:
   
    sudo apt install python3


3. Install pip to be able to install the required libraries:

    sudo apt install python-pip

  
4. Next, install the necessary libraries, OpenCV, and NumPy using the following commands:

    pip install opencv-python

    pip install numpy


## 8-Neighborhood

In this project, the initial part involves traversing the image starting from a single seed point using the 8-neighborhood technique. The 8-neighborhood is a type of connectivity where a pixel is considered a neighbor to another pixel if they are horizontally, vertically, or diagonally adjacent. This means that there are 8 pixels considered as neighbors for a given pixel. Using the 8-neighborhood can improve the quality of segmentation by considering diagonal pixels as similar to horizontal and vertical pixels.

The corresponding function takes two parameters, x and y, representing the coordinates of a pixel in an image, and a variable "shape" from OpenCV, which contains the dimensions of the image. The function uses nested loops to traverse all the pixels within a 3x3 grid centered around the input pixel (x, y). It then checks if the current pixel is within the image boundaries and is not the same as the input pixel. If so, it adds the coordinates of the pixel to a list called "neighbors."

The function then returns this list of neighbors, which are the 8 pixels that are horizontally, vertically, or diagonally adjacent to the input pixel (x, y). The complexity of this function is O(1) since it performs a constant number of operations independent of the image size.

## Region Growing

### Different Methods

There are several methods to compare colors during region growing using 8 neighbors. The most common ones include:

- Euclidean Distance: The Euclidean distance between two colors is the square root of the sum of squared differences between the red, green, and blue values of the colors. This method is used in the provided code.

- Manhattan Distance: The Manhattan distance between two colors is the sum of the absolute differences between the red, green, and blue values of the colors.

- Minkowski Distance: The Minkowski distance between two colors is a generalization of the Manhattan and Euclidean distances, using a parameter 'p' to adjust the distance calculation.

- Color Histogram: This method compares the color histograms of the starting point and the neighboring pixel. Histograms are compared using a similarity metric such as the Chi-square distance or Bhattacharyya distance.

- Color Moments: This method compares the color moments of the starting point and the neighboring pixel. It is based on statistical properties of color values.

For this project, the Euclidean distance and color histogram methods have been implemented.

### Operation of Region Growing Functions

#### Processed

To prevent regions from overwriting each other, the pixels in the image are tracked using a variable called "processed." The "processed" variable is a 2D NumPy array that keeps track of the pixels that have been processed by the region growing algorithm. The algorithm starts with a set of seed points and iteratively examines the 8 neighboring pixels of each seed point to determine if they should be included in the growing region.

When a pixel is processed for the first time, its corresponding value in the "processed" array is set to True. This way, when the algorithm checks a neighboring pixel, it can see if that pixel has already been processed and, if so, skip it. This prevents the algorithm from getting stuck in an infinite loop and ensures that each pixel is processed only once.

The "processed" variable is used as follows:

- At the beginning of the loop, all pixels that are part of the seed points are processed, and their corresponding values in the "processed" array are set to True.

- In the while loop, for each pixel in the seed_points, its 8 neighbors are processed, and if they haven't been processed before and meet the threshold criteria, they are added to seed_points, and their corresponding values in the "processed" array are set to True.

- The while loop continues until there are no more pixels in seed_points.

- The "processed" variable is returned as output along with the "outimg" variable, so you can use it later if needed.

## Timer
The timer is an optional variable that controls the speed at which the region-growing algorithm executes. If the timer is set to True, the algorithm displays an image window every time a certain number of iterations is reached. This number of iterations is defined by the variable "speed". When "timer" is set to True, the iteration variable is initialized to 1. With each iteration of the while loop, the iteration is incremented by 1. If the iteration equals the speed, the cv2.imshow() function is used to display the output image. This allows you to see the evolution of the output image as the algorithm progresses. The iteration is then reset to 1 to continue counting the number of iterations. Using this timing feature can significantly slow down the region-growing algorithm, especially for large images, as it has to display the output image at each iteration. Therefore, it is generally used for small images or debugging purposes.

## Colors
Color generation is added to give a random color to the starting pixels. Then, the pixels added to the region are assigned the same color as the starting pixel.

## Image Filling
The fill_image function is responsible for image filling. There are two different methods - Euclidean distance and color histogram. First, an infinite loop is created with the condition "while (True)" that will continue to run until there are no more unprocessed pixels in the image. The np.where function is used to find the x and y positions of unprocessed pixels in the "processed" image. If the size of x is zero, it means there are no more unprocessed pixels, so the loop is broken. Then, the function creates an empty "pixels" array that stores the coordinates of 20 randomly chosen unprocessed pixels. These pixels are then used as starting points for the region-growing algorithm.

## Manual Seed Selection
### Mouse Handling
First, the "on_mouse" function is defined. It is used to record the coordinates of points clicked with the mouse and stores them in the "clicks" variable. This function is called when the "EVENT_LBUTTONDOWN" (left-click) event occurs on the image window.

### Image Display
The "show_img" function is also defined. It takes text and an image as input and displays them in a window using cv2.imshow(). It also uses cv2.waitKey() to wait for keyboard input and cv2.destroyAllWindows() to close the window when input is received.

### Main Program
In the "if __name__ == '__main__':" section, a "clicks" variable is initialized as empty. The "img.jpg" image is then loaded using cv2.imread(), and an image window named "Input" is created. The "on_mouse" function is then set as the mouse event handler for the "Input" window using cv2.setMouseCallback(). The "Input" window is then displayed using cv2.imshow(), and cv2.waitKey() is used to wait for keyboard input. When the user clicks on the window, the coordinates of that point are saved in the "clicks" variable. Once the user has finished selecting the starting points, the "region_growing_euclidean" function is used to select regions of the image using the starting points stored in the "clicks" variable. The "region_growing_euclidean" function takes the input image "img," starting points "seed," output image "out," processed pixel image "processed," and an optional "timer" parameter, which, when set to True, displays intermediate images at each iteration of the algorithm to show how the image is filled. After the "region_growing_euclidean" function has been executed, the "show_img" function is used to display the output image "out" with the title "Region Growing". Finally, the "fill_image_euclidean" function is used to completely fill the image using the region-growing algorithm with random starting points. The function takes the input image "img," processed pixel image "processed," and output image "out." Once the function has been executed, the "out" image is displayed again using the "show_img" function to show the final result.

## Conclusion
The region-growing algorithm is a useful tool for selecting specific regions in an image using chosen starting points. It works by using color comparison to identify pixels similar to the starting points and adding them to the selected region. Several methods can be used to compare colors, such as Euclidean distance, Manhattan distance, color histogram, and color moments. 

The provided code demonstrates how to use the region-growing algorithm to select regions in an image using mouse-clicked starting points. It uses either Euclidean distance or histogram comparison for color comparison, a mouse callback function to record starting points, and a function to fully fill the image using the region-growing algorithm with random starting points. 

In summary, the region-growing algorithm is a powerful tool for selecting specific regions in an image using chosen starting points. It can be used with different methods for color comparison and can also be used to completely fill the image using random starting points. It is also possible to visualize the algorithm's iterations to understand how it fills the image.

