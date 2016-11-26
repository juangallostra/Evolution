from PIL import Image, ImageDraw
from os import listdir,getcwd
import pygame
from pygame.locals import *
from random import *
import copy
from math import sqrt
import ast



# FUNCTIONS

# Original image openning and info
def get_image():
    dir=getcwd()
    files=listdir(dir)
    # Find images
    s=None
    for f in files:
        string=''
        for i in range(1,5):
            string+=f[-i]
        q=string[::-1]
        t=q.upper()
        if t in ('.GIF','.BMP','.PNG','JPEG','EXIF','TIFF','.PPM','.PAM','.JPG'):
            ima=f
            return ima
    return 'Image not found'

# Get reference image info
def info_image(ima):
    l1=[]
    im=Image.open(ima).convert('LA')
    im2=im.resize((242,162))
    # im2.save('greyscale.png')
    # rgb_im=im2.convert('RGB')
    im2.show()
    w,h=im2.size
    for p in range(h):
        for q in range(w):
            l1.append(im2.getpixel((q,p)))
    l_def=[]
    for p in l1:
        l_def.append(p[0])
    return l_def


# ----- Genetic Algorithm ------

# Create initial DNA
def create_mother(n=128):
    mother=[]
    for i in range(n):
        circle=[]
        circle.append(randint(0,242))
        circle.append(randint(0,162))
        circle.append(randint(0,70))
        circle.append([randint(0,255),255])
        circle.append(randint(30,60))
        mother.append(circle)
    return mother

# Mutate mother DNA
def create_daughter_from_mother(mother,n_mutations):
    # We pass the mother and the number of mutations as function parametres
    daughter=copy.deepcopy(mother)
    for i in range(n_mutations):
        mutation_type=randint(0,5)
        mutated_dna=randint(0,127)
        if mutation_type==0:
            daughter[mutated_dna][0]=randint(0,242)
        if mutation_type==1:
            daughter[mutated_dna][1]=randint(0,162)
        if mutation_type==2:
            daughter[mutated_dna][2]=randint(0,70)
        if mutation_type==3:
            daughter[mutated_dna][3][0]=randint(0,255)
        if mutation_type==4:
            daughter[mutated_dna][4]=randint(30,60)
        if mutation_type==5:
            p=randint(0,99)
            q=randint(0,99)
            daughter_q=daughter[q]
            daughter_p=daughter[p]
            daughter[p]=daughter_q
            daughter[q]=daughter_p
    return daughter

# Get strength  
def strength(mother_or_daughter,original):
    if mother_or_daughter == None:
        return 0
    m_or_d=circles_to_image(mother_or_daughter)
    w,h=m_or_d.size
    m_or_d_color=[]
    for p in range(h):
        for q in range(w):
            pixel=m_or_d.getpixel((q,p))
            m_or_d_color.append(pixel)
    strength=0.0
    i=0
    for color in original:
        strength+=(color-m_or_d_color[i])**2
        i+=1
    strength=sqrt(float(strength)/(242*162))
    return strength


# Get strongest candidate 
def get_strongest(mother,daughter,original):
    mother_strength=strength(mother,original)
    daughter_strength=strength(daughter,original)
    print min(mother_strength,daughter_strength)
    if mother_strength>daughter_strength:
        return daughter
    else:
        return mother

#DRAWING RESULTS

# Draw actual state
def circles_to_image(m_or_d):
    w=242;h=162
    im = Image.new('L', (w,h), 255)
    for individual in m_or_d:
        mask = Image.new('L', (w, h))
        draw = ImageDraw.Draw(mask)
        draw.ellipse((individual[0]-individual[2],individual[1]-individual[2],individual[0]+individual[2], individual[1]+individual[2]), fill=individual[3][0])
        im.paste(mask, mask)
        del mask, draw
    return im


# EVOLUTION

# main function
def main(n_iters = 10000):
    original=info_image(get_image())
    mother = create_mother(n=128)
    n_mutations=1 # 16
    for i in range(n_iters): # number of iterations
        print i
        if i>4000:
            n_mutations=1
        daughter=create_daughter_from_mother(mother,n_mutations)
        mother=get_strongest(mother,daughter,original)
        if i%1000==0 and i>=1000:
            circles_to_image(mother).show()
            circles_to_image(mother).save(str(i)+'it.bmp')
            mother_data=open('data.txt','w')
            mother_data.write(str(mother))
            mother_data.close()


    circles_to_image(mother).show()

# Run evolution

if __name__ == '__main__':
    main()



