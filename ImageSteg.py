from numpy.core.arrayprint import printoptions
from PIL import Image
import pandas as pd
import numpy as np
import random

class ImageSteg:

  global cipher
  cipher = {}
  alphabet = "abcdefghijklmnopqrstuvwxyz[@_!#$%^&*()<>?/\|}{~:]"
  l=[]  
  for letter in alphabet:
    k = random.choice(alphabet.replace(letter, ""))
    while k in l:
      k = random.choice(alphabet.replace(letter, ""))
    if k not in l:
      cipher[letter] = k
      l.append(k)

  def __fillMSB(self, inp):
    '''
    0b01100 -> [0,0,0,0,1,1,0,0]
    '''
    inp = inp.split("b")[-1]
    inp = '0'*(7-len(inp))+inp
    return [int(x) for x in inp]

  def __decrypt_pixels(self, pixels):
    '''
    Given list of 7 pixel values -> Determine 0/1 -> Join 7 0/1s to form binary -> integer -> character
    '''

    pixels = [str(x%2) for x in pixels]
    bin_repr = "".join(pixels)
    return chr(int(bin_repr,2))
  

  def hide(self, image_path, msg):
    
    img = np.array(Image.open(image_path))
    imgArr = img.flatten()
    msg += "<-END->"
    msgArr = [self.__fillMSB(bin(ord(ch))) for ch in msg]
    
    idx = 0
    for char in msgArr:
      for bit in char:
        if bit==1:
          if imgArr[idx]==0:
            imgArr[idx] = 1
          else:
            imgArr[idx] = imgArr[idx] if imgArr[idx]%2==1 else imgArr[idx]-1
        else: 
          if imgArr[idx]==255:
            imgArr[idx] = 254
          else:
            imgArr[idx] = imgArr[idx] if imgArr[idx]%2==0 else imgArr[idx]+1   
        idx += 1

    resImg = Image.fromarray(np.reshape(imgArr, img.shape))
    return resImg

  def reveal(self, image_path):

    img = np.array(Image.open(image_path))
    imgArr = np.array(img).flatten()
    
    decrypted_message = ""
    for i in range(7,len(imgArr),7):
      decrypted_char = self.__decrypt_pixels(imgArr[i-7:i])
      decrypted_message += decrypted_char

      if len(decrypted_message)>10 and decrypted_message[-7:] == "<-END->":
        break

    return decrypted_message[:-7]


  def encrypt(self,plaintext,watermark):
    global ciphertext
    ciphertext = ""
    for letter in plaintext.lower():
        if letter in cipher and letter.isalpha():
            ciphertext += cipher[letter]
        else:
            ciphertext += letter
    # conveting list of keys and values of dictionary to a list using map() function
    cipherlist = list(map(list, cipher.items()))
    cl=[]
    for l in cipherlist:
        cl= cl+ l
    cl1 = "".join(cl[:52])
    hashvalue= cl1 + watermark
    mark = len(ciphertext)//2
    ciphertext_final = ciphertext[0:mark] + hashvalue + ciphertext[mark:]
    return ciphertext_final


  def decrypt(self,ciphertext_final):
    ciphertext_length = len(ciphertext_final) - 52 -5
    mark = ciphertext_length//2
    coded_alphabets = list(ciphertext_final[mark:mark+52])
    coded_alphabets_dict= {coded_alphabets[i]: coded_alphabets[i + 1] for i in range(0, len(coded_alphabets), 2)}
    ciphertext1= ciphertext_final[:mark] + ciphertext_final[mark+52+5:]
    watermark= ciphertext_final[mark+52:mark+52+5]
    original_text= ""
    for c in ciphertext1:
      if c != " " and c != "." and c != "," and c.isdigit() == False:
        origin_letter = list(coded_alphabets_dict.keys())[list(coded_alphabets_dict.values()).index(c)]
        original_text += origin_letter
      else:
        original_text += c
    return original_text,watermark
    
