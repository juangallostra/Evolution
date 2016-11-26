
This program evolves a given number of circles in order to ressemble as much as possible a target image.

Requirements:
- Python 2.7
- PIL
- Target image has to be in the same folder as the program file.

Supported image formats: .GIF, .BMP, .PNG , .JPEG, .EXIF, .TIFF, .PPM, .PAM, .JPG

Notes:
- The programs scales the target image to 264x162 and converts it to grayscale.
- The fitness function that evaluates how good a certain DNA sequence is the sum of the squared errors computed for every pixel. This is done between evolved image and target image.
- Crossovers are not impelemented yet. By now, mutations of the mother and selection of strongest candidate between mother and daughter are the only ways of evolution.

Every 1000 iterations an image is saved in the working directory with the progress of the algorithm so far. Furthermore, a 'data.txt' file is generated with the DNA of the strongest candidate so far. This data can replace the function call mother=create_mother(n=128) in order to make the algorithm run from that saved evolution instead of starting from scratch again.

Actual algorithm flow:

1. Initialize mother DNA

2. For the specified number of iterations:
    - Mutate to obtain 1 offspring
    - Compare mother and daughter strength
    - Keep the one with highest strength as mother

TO DO (improvements):
- Increase the offspring the mother has to more than 1 so that there are more possibilities of getting stronger candidates.
- Implement crossover between different DNA sequences.
- Optimize code so it runs faster. Some changes can be done regarding the way the strength is computed and the objective function. 
