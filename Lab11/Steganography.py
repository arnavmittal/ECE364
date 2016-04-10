import numpy as np
import sys
import scipy
import zlib
import base64

class Payload:
    def __init__(self, img=None, compressionLevel=-1, xml=None):
        self.img = img
        self.xml = str(xml)
        #print(img)
        #print(compressionLevel)
        #print(xml)

        if(img is None and xml is None):
            raise ValueError("Image and XML are not provided.")
        if compressionLevel > 9 or compressionLevel < -1:
            raise ValueError("Compression Level has invalid value")
        if(xml is not None and type(xml) is not str):
            raise TypeError("XML has incorrect type")
        if(type(img) is not np.ndarray):
            raise TypeError("Image has incorrect type")

        if (img is not None and xml is None):
            if(compressionLevel != -1):
                compressed = "True"
                value_1=zlib.compress(img, compressionLevel)
            else:
                value_1=self.img
                compressed = "False"
            cmp_value=base64.b64encode(value_1)
                                            # Compressed retreived
            row,col,num_byte = img.shape
            img_size=""
            img_size+=str(row)
            img_size+=","
            img_size+=str(col)
                                            # Image Size retreived
            if(num_byte == 1):
                payload_type = "Color"
            elif(num_byte == 3):
                payload_type = "Gray"
                                            # Payload Type retreived

            self.xml='<?xml version="1.0" encoding="UTF-8"?>\n'
            self.xml+='<payload type="'+payload_type+'" size="'+img_size+'" compressed="'+compressed+'">\n'
            self.xml+=str(cmp_value, encoding='UTF-8')+'\n'
            self.xml+='</payload>'

