from pathlib import Path
import qrtools
import os
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode

class decoder:
    def __init__(self,shapekey,Folderpath):
        self.shapekey=shapekey
        self.Folderpath=Folderpath
        self.decode()

    def decode(self):
       
        one_d_array=[]
        paths = sorted(Path(self.Folderpath).iterdir(), key=os.path.getmtime)
        for i in range(len(paths)):
            filename=str(paths[i])
            if "code" in filename:
                file=filename
                result=decode(Image.open(file))
               
                for i in result:
                    c=i.data.decode("utf-8")
                    d=len(c)
                    cleaned_c=c[1:d-1]
                    list=cleaned_c.split(",")
                    for i in list:
                        one_d_array.append(int(i))
                    
        def extract_shapekey(c):
            d=c.split(",")
            e=d[0]
            f=d[1]
            g=e.split("(")
            h=f.split(")")
            part_1=g[1]
            part_2=h[0]
            shapekey=(int(part_1),int(part_2))
            return shapekey        

        shapekey=extract_shapekey(self.shapekey)    
        cleaned_one_d_array=np.array(one_d_array)
        #reforming the array back to the original shape
        extracted_array=np.asarray(cleaned_one_d_array).reshape(shapekey)
        #convert back array to image and showing the image
        #extracted_array.astype("float64)"
        extracted_image=Image.fromarray(np.uint8(extracted_array)).convert('RGB')
        extracted_image.show()
        extracted_image.save()



        
