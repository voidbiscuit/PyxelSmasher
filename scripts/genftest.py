xscale = 1.4
yscale = 3

max = 100

file = open("fourier.sc", "w")
filebuffer = ""
for i in range(0, 100):
    filebuffer += "\nf " + str(100-i)
file.writelines(filebuffer)
file.close()
