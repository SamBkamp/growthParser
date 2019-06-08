# growthParser
## A python script measure growth of bacteria in agar jelly

- This program uses python and PIL to parse and analyse images
- The run time for most images should be < 1 second but not enough testing has been done


### How it works

- The idea was based off of Dr. Michael Pound's [auto root program](https://plantmethods.biomedcentral.com/articles/10.1186/s13007-017-0161-y)
- It works by taking the subject image, and turning it to true black and white. After this, the program iterates through the pixels and if the pixel is 
  white, it gets added to the value 'area'. This is then subtracted from the size of the total image to get the amount and percentage of pixels in the image




### TODO

- Add command line argument support
- add ability to add 'focus zone' where everything outside of said zone is omitted for scanning
- add support for storage of data, to allow for easier graphing and complete, long-term automation
 
