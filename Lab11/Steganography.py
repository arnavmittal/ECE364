import numpy as np
import sys
import scipy
import zlib
import base64
import re

class Payload:
    def __init__(self, img=None, compressionLevel=-1, xml=None):
        self.img = img
        self.cmplvl = compressionLevel
        self.xml = str(xml)

        if(img is None and xml is None):
            raise ValueError("Image and XML are not provided.")

        if compressionLevel > 9 or compressionLevel < -1:
            raise ValueError("Compression Level has invalid value")

        if(xml is not None and type(xml) is not str):
            raise TypeError("XML has incorrect type")

        if(type(img) is not np.ndarray):
            raise TypeError("Image has incorrect type")

        # Image is given but XML is not.
        if (img is not None and xml is None):
            raster_array = raster_scan(self)
            extractXML(self, raster_array)

        if (img is None and xml is not None):


def raster_scan(self):
    if(len(self.img.shape) == 3):
        comb_list = self.img.transpose(2, 0, 1)
    else:
        comb_list = self.img
    comb_list = comb_list.flatten()
    return(np.asarray(comb_list))

def extractXML(self, raster_array):

    # Compressed retreived

    if(self.cmplvl != -1):
        compressed = "True"
        value_1=zlib.compress(raster_array, self.cmplvl)
    else:
        value_1=self.img
        compressed = "False"
    cmp_value=base64.b64encode(value_1)


    # Image Size retreived

    size_chk= self.img.shape
    img_size=""
    img_size+=str(size_chk[0])
    img_size+=","
    img_size+=str(size_chk[1])


    # Payload Type retreived

    if(len(size_chk) == 3):
        payload_type = "Color"
    else:
        payload_type = "Gray"

    self.xml='<?xml version="1.0" encoding="UTF-8"?>\n'
    self.xml+='<payload type="'+payload_type+'" size="'+img_size+'" compressed="'+compressed+'">\n'
    self.xml+=str(cmp_value, encoding='UTF-8')+'\n'
    self.xml+='</payload>'