from PIL import Image
import numpy as np
import sys
import decoder
import encoder
import os



def encoding(path):
    root_path=os.getcwd()
    results_path=root_path+"\\results"
    #loading the digital Image
    image=Image.open(path)
    #converting image to array
    Matrix=np.asarray(image)
    #recording the shape of the array
    shape=Matrix.shape 
    #313
    data_size=350
    #flattening the array to about 1d
    np.set_printoptions(threshold=sys.maxsize)
    flat_array=list(Matrix.flatten())
    encoder.Processor(flat_array,data_size,results_path)
    return shape

def decoding(shape,path_to_dest):
    decoder.decoder(shape,path_to_dest)
    





'''
if __name__ == "__main__":
    
    encoder.Processor(flat_array,data_size,'F:/results')
    pathtodest="F:/results/"
    decoder.decoder(shape,pathtodest)
'''







