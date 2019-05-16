from PIL import Image

def analyse(imgPath):
    area = 0
    pix = Image.open(imgPath)
    loaded = pix.load()

    for i in range(pix.size[0]):
        for j in range (pix.size[1]):

            if j == (pix.size[1] - 1):
                print("line " + str(i + 1))

            if int(loaded[i,j]) != 255:
                area = area + 1
                
    amountBac = (pix.size[0] * pix.size[1]) - area
    print("done")
    print("amount of bacteria: " + str(amountBac) + "px (" + str((amountBac/(pix.size[0] * pix.size[1]))*100) + "%)")
    
        
 
def black_and_white(input_image_path,
    output_image_path):
    color_image = Image.open(input_image_path) #E.coli as bacteria
    bw = color_image.convert('L')
    trueB = bw.point(lambda x: 0 if x<128 else 255, '1')
    trueB.save(output_image_path)
    analyse(output_image_path)

infile = input("infile: ") #I havnt figured out how to argv's in python yet ;~;
try:
    black_and_white(infile, "bacteria-processed.png") #if output is .jpeg, it will return an incorrect value.
except FileNotFoundError:
    print("file '" + infile + "' not found")