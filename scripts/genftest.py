xscale = 1.4
yscale = 3

max = 150

file = open("fourier.sc", "w")
filebuffer = ""
for i in range(1, 50):
    xval = round(i * xscale)
    yval = round(i * yscale)
    if xval < max and yval < max:
        filebuffer += "\nf " + str(yval) + " " + str(xval)
file.writelines(filebuffer)
file.close()
