#% preparation
close(mstring('all'))
clear(mstring('all'))
clc()

#% choose sky & guide
sky = im2double(imread(mstring('sky.jpg')))
guide = im2double(imread(mstring('guide/guide10.jpg')))
#% input
input1 = im2double(imread(mstring('input/input1.jpg')))
input2 = im2double(imread(mstring('input/input2.jpg')))
input3 = im2double(imread(mstring('input/input3.jpg')))
input4 = im2double(imread(mstring('input/input4.jpg')))
input5 = im2double(imread(mstring('input/input5.jpg')))
input6 = im2double(imread(mstring('input/input6.jpg')))
input7 = im2double(imread(mstring('input/input7.jpg')))
input8 = im2double(imread(mstring('input/input8.jpg')))
input9 = im2double(imread(mstring('input/input9.jpg')))
input10 = im2double(imread(mstring('input/input10.jpg')))

#% filtering
output1 = ShinkaiMakotoFilter(input1, guide, sky)
output2 = ShinkaiMakotoFilter(input2, guide, sky)
output3 = ShinkaiMakotoFilter(input3, guide, sky)
output4 = ShinkaiMakotoFilter(input4, guide, sky)
output5 = ShinkaiMakotoFilter(input5, guide, sky)
output6 = ShinkaiMakotoFilter(input6, guide, sky)
output7 = ShinkaiMakotoFilter(input7, guide, sky)
output8 = ShinkaiMakotoFilter(input8, guide, sky)
output9 = ShinkaiMakotoFilter(input9, guide, sky)
output10 = ShinkaiMakotoFilter(input10, guide, sky)