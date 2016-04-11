import numpy as np
from copy import deepcopy
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

        if(img is not None and type(img) is not np.ndarray):
            raise TypeError("Image has incorrect type")

        if (xml):
            extractIMG(self)
        else:
            raster_array = raster_scan(self)
            generateXML(self, raster_array)


def raster_scan(self):
    if(len(self.img.shape) == 3):
        comb_list = self.img.transpose(2, 0, 1)
    else:
        comb_list = self.img
    comb_list = comb_list.flatten()
    return(np.asarray(comb_list))

def generateXML(self, raster_array):
    #--------------------------------------------------------#
    # Compressing
    #--------------------------------------------------------#
    if(self.cmplvl != -1):
        compressed = "True"
        value_1=zlib.compress(raster_array, self.cmplvl)
    else:
        value_1=self.img
        compressed = "False"

    #--------------------------------------------------------#
    # Base 64 encoding
    #--------------------------------------------------------#
    cmp_value=base64.b64encode(value_1)

    #--------------------------------------------------------#
    # Image Size retreived
    #--------------------------------------------------------#
    size_chk= self.img.shape
    img_size=""
    img_size+=str(size_chk[0])
    img_size+=","
    img_size+=str(size_chk[1])

    #--------------------------------------------------------#
    # Payload Type retreived
    #--------------------------------------------------------#
    if(len(size_chk) == 3):
        payload_type = "Color"
    else:
        payload_type = "Gray"

    #--------------------------------------------------------#
    # Generating XML
    #--------------------------------------------------------#
    self.xml='<?xml version="1.0" encoding="UTF-8"?>\n'
    self.xml+='<payload type="'+payload_type+'" size="'+img_size+'" compressed="'+compressed+'">\n'
    self.xml+=str(cmp_value, encoding='UTF-8')+'\n'
    self.xml+='</payload>'

def extractIMG(self):
    #--------------------------------------------------------#
    # Extracting everything from XML String
    #--------------------------------------------------------#
    img_str=self.xml.split('\n')[1]
    xml_str=self.xml.split('\n')[2]
    expr=r'<payload type="(.*)" size="(.*),(.*)" compressed="(.*)">'
    matched = re.search(expr, img_str)
    if matched:
        payload_type=matched.group(1)
        row=matched.group(2)
        col=matched.group(3)
        compressed=matched.group(4)

    #--------------------------------------------------------#
    # Base 64 decoding
    #--------------------------------------------------------#
    cmp_value=base64.b64decode(xml_str)

    #--------------------------------------------------------#
    # Decompress
    #--------------------------------------------------------#
    if(compressed == "True"):
        dcmp_val=list(zlib.decompress(cmp_value))
    else:
        dcmp_val=list(cmp_value)

    #--------------------------------------------------------#
    # Creating IMG based on Color or Gray Scale
    #--------------------------------------------------------#
    if(payload_type == "Gray"):
        self.img = np.resize(dcmp_val, (int(row),int(col)))
    elif(payload_type == "Color"):
        new_list=[0 for i in range(len(dcmp_val))]
        for i in range(int(len(dcmp_val)/3)):
            new_list[3*i]=dcmp_val[i]
            new_list[3*i+1]=dcmp_val[int(len(dcmp_val)/3)+i]
            new_list[3*i+2]=dcmp_val[int(len(dcmp_val)/3)*2+i]
        self.img = np.resize(new_list, (int(row),int(col),3))


class Carrier:
    def __init__(self, img):
        self.img = img
        if(type(img) is not np.ndarray):
            raise TypeError("Image has incorrect type")

    def payloadExists(self):
    #--------------------------------------------------------#
    # payload_type=1 if color, 0 if gray
    #--------------------------------------------------------#
        new_str=''
        for i in range(8):
            if(len(self.img.shape) == 3):
                if(self.img[0][i][0] % 2):
                    new_str+='1'
                else:
                    new_str+='0'
            else:
                if(self.img[0][i] % 2):
                    new_str+='1'
                else:
                    new_str+='0'
        if(int(new_str, 2)==60):
            return True
        else:
            return False


    def clean(self):
        temp=deepcopy(self.img)
        for i in range(len(self.img)):
            for j in range(len(self.img[0])):
                if(len(self.img.shape) == 3):
                    for k in range(3):
                        if(temp[i][j][k] % 2):
                            temp[i][j][k] = temp[i][j][k] - 1
                else:
                    if(temp[i][j] % 2):
                            temp[i][j] = temp[i][j] - 1
        return temp

    def embedPayload(self, payload, override=False):
        if(type(payload) is not Payload):
            raise TypeError("self or payload has an invalid type")
        if(len(self.img.shape)==3):
            if(len(payload.xml)*8 > int(self.img.shape[0])*int(self.img.shape[1])*3):
                raise ValueError("payload can not be bigger than carrier")
        else:
            if(len(payload.xml)*8 > int(self.img.shape[0])*int(self.img.shape[1])):
                raise ValueError("payload can not be bigger than carrier")
        if(self.payloadExists() and override is False):
            raise Exception("Carrier already contains a payload, try again")
        return func1(self, payload)


    def extractPayload(self):
        if(self.payloadExists()):
            new_list=[]
            raster_array = raster_scan(self)
            for i in range(len(raster_array)):
                if(raster_array[i]%2):
                    new_list.append(1)
                else:
                    new_list.append(0)
            bin_str=''
            new_str=''

            for i in range(len(new_list)):

                if i % 8 == 0 and i!= 0:


                    int_val=int(bin_str, 2)
                    char_val=chr(int_val)
                    new_str+=char_val
                    bin_str=''
                    if "</payload>" in new_str:
                        break

                bin_str += str(new_list[i])

            temp=Payload(xml=new_str)
            return temp
        else:
            raise Exception("No payload contained")

def func1(self, payload):
    #--------------------------------------------------------#
    # Type of image: Color or Gray
    #--------------------------------------------------------#
    if(len(self.img.shape)==3):
        # Color Image
        image = 1
    else:
        # Gray Image
        image = 0
    #--------------------------------------------------------#
    # Convert xml into binary
    #--------------------------------------------------------#
    bin_list=[]
    fin_list=[]
    for i in payload.xml:
        bin_list.append('{0:08b}'.format(ord(i)))
    for i in bin_list:
        for j in i:
            fin_list.append(int(j))

    k=0
    raster_array = list(raster_scan(self))
    for i in range(len(fin_list)):
        if fin_list[k]==0:
            k+=1
            if raster_array[i] % 2 == 1:
                raster_array[i] -= 1
                #if(raster_array[i] < 0):
                #    raster_array[i] = 0
        elif fin_list[k]==1:
            k+=1
            if raster_array[i] % 2 == 0:
                raster_array[i] += 1
                #if(raster_array[i] > 255):
                #    raster_array[i] = 255

    #--------------------------------------------------------#
    # Creating IMG based on Color or Gray Scale
    #--------------------------------------------------------#
    row=int(self.img.shape[0])
    col=int(self.img.shape[1])
    if(image == 0):
        temp = np.resize(raster_array, (int(self.img.shape[0]),int(self.img.shape[1])))
    elif(image == 1):
        new_list=[0 for i in range(len(raster_array))]
        for i in range(int(len(raster_array)/3)):
            new_list[3*i]=raster_array[i]
            new_list[3*i+1]=raster_array[int(len(raster_array)/3)+i]
            new_list[3*i+2]=raster_array[int(len(raster_array)/3)*2+i]
        temp = np.resize(new_list, (int(self.img.shape[0]),int(self.img.shape[1]),3))
    return temp
