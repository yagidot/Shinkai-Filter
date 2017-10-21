@mfunction("skyMask, I, dilate, erosion")
def findSky(input=None):

    # Summary - find sky part in image

    # threshold to blue space
    I = input(mslice[:], mslice[:], 3)
    I = imbinarize(I, 0.7)

    # do dilation -> erosion
    sq = ones(3, 3)
    dilate = imdilate(I, sq)
    erosion = imerode(dilate, sq)

    # choose the biggest part as sky
    J = bwlabel(erosion, 4)