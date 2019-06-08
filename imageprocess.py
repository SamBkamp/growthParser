from PIL import Image
import re


def analyse(imgPath, ctrl):
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
    if(ctrl != "ctrl"):
        x = re.search(r"[0-9]\w+", open('contro.txt').read())
        if (x.group() == None):
            print("either contro.txt is currupt or you havn't loaded a control file")
            exit()
        
        actualarea = amountBac - int(x.group())
    else:
        actualarea = amountBac
    
    print("done")
    print("amount of bacteria: " + str(actualarea) + "px (" + str((actualarea/(pix.size[0] * pix.size[1]))*100) + "%)")
    if (ctrl == "ctrl"):
        with open("contro.txt", "w", encoding='utf-8') as text_file:
            text_file.write(str(amountBac))
    
        
 
def black_and_white(input_image_path,
    output_image_path, ctrl):
    color_image = Image.open(input_image_path) #E.coli as bacteria
    bw = color_image.convert('L')
    trueB = bw.point(lambda x: 255 if x<128 else 0, "1")
    #trueB = bw.point(lambda x: 0 if x<128 else 255, '1')
    trueB.save("tests/" + output_image_path)
    analyse("tests/" + output_image_path, ctrl)

infile = input("infile: ") #I havnt figured out how to use argv's in python yet ;~;
isctrl = input("is it control? [y/n]")

if isctrl == "y":
    try:
        black_and_white(infile, "bacteria-processed.png", "ctrl") #if output is .jpeg, it will return an incorrect value.
    except FileNotFoundError:
        print("file '" + infile + "' not found")

elif isctrl == "n":
    try:
        black_and_white(infile, "bacteria-processed.png", "standard") #if output is .jpeg, it will return an incorrect value.
    except FileNotFoundError:
        print("file '" + infile + "' not found")
else:
    print("enter 'y' or 'n' in the second prompt. exiting now.")
    
