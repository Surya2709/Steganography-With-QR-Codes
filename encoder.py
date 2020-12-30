import pyqrcode
from PIL import Image
import math
import qrcode


class Processor(object):
    def __init__(self,array,data_size,destination_folder):
        self.array=array
        self.data_size=data_size
        self.counter=1
        self.beg=0
        self.end=self.data_size
        self.destination_folder=destination_folder
        #print('Shapekey:',main.shape)
        self.process()
    
    def qr_generator(self,text):
        #qr_code=pyqrcode.create(text)
        
        file_name='Qrcode'+str(self.counter)
        name=f"/{file_name}.png"
        qr = qrcode.QRCode(version=12,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=2,border=8)
        qr.add_data(text)
        qr.make()
        qr_image=qr.make_image()
        qr_image.save(self.destination_folder+"\\temp\\tempimg.png")
        image=Image.open(self.destination_folder+"\\temp\\tempimg.png")
        #qr_code.png(name,scale=10)
        #image=Image.open(name)
        image=image.resize((400,400),Image.ANTIALIAS)
        destination=self.destination_folder+name
        image.save(destination,'PNG')
        self.counter+=1

    def process(self):
        print(self.array)
        divisor=math.ceil(len(self.array)/self.data_size)
        print("THe divisor value is : ", divisor)
        while(int(divisor))!=0 and int(divisor)>0:
            data=str(self.array[self.beg:self.end])   
            print(data)
            self.qr_generator(data)
            self.beg=self.end
            self.end=self.end+self.data_size
            divisor-=1
