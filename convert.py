import os
import sys
from pdf2image import convert_from_path

for i in list(os.walk(sys.argv[1]))[1:]:
    for j in i[2]:
        if j[-3:] == "pdf":
            images = convert_from_path(i[0]+"/"+j)
            if len(images) == 1:
                images[0].save(i[0]+"/"+j[:-3]+"jpg")
