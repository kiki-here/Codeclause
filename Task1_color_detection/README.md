# COLOR DETECTION 

### Description :
How many times has it occurred to you that even after seeing, you
don't remember the name of the color? There can be 16 million colors based on the different RGB color values but we only remember a few.
So in this project, we are going to build an interactive app that will detect the selected color from any image. To implement this we will
need a labeled data of all the known colors then we will calculate which color resembles the most with the selected color value.

### About The Project :
Talking about this Color Detection in Python, we are going to build an application through which you can automatically 
get the name of the color by clicking on them. So for this, we will have a data file that contains the color name and its values. 
Then we will calculate the distance from each color and find the shortest one.

### About files :
- "Color_detection.py" – main source code of our project.
- "sample.jpg" – sample image for experimenting.
- "Colors.csv" – a file that contains our dataset.

### Programming Languages- Python

### Python version (Recommended) - 2.x or 3.x

### Dependencies - pandas , numpy , opencv , argparse
CAN INSTALL PYTHON PACKAGES BY : 
- `pip install pandas`
- `pip install numpy`
- `pip install opencv-python`

### About DataSet :
Colors are made up of 3 primary colors; red, green, and blue. In computers, we define each color value within a range of 0 to 255.
So in how many ways we can define a color? The answer is 256*256*256 = 16,581,375. There are approximately 16.5 million different ways to represent a color.
In our dataset, we need to map each color’s values with their corresponding names. But don’t worry, we don’t need to map all the values.
We will be using a dataset that contains RGB values with their corresponding names.
