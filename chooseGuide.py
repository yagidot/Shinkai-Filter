@mfunction("out")
def chooseGuide(_in=None, M=None, N=None):

    # Summary - auto choose guide

    # standard
    _in = rgb2hsv(_in)


    # choose guide

    out = zeros(M, N)
    if index == 1:
        out = im2double(imread(mstring('guide/guide1.jpg')))
    elif index == 2:
        out = im2double(imread(mstring('guide/guide2.jpg')))
    elif index == 3:
        out = im2double(imread(mstring('guide/guide3.jpg')))
    elif index == 4:
        out = im2double(imread(mstring('guide/guide4.jpg')))
    elif index == 5:
        out = im2double(imread(mstring('guide/guide5.jpg')))
    elif index == 6:
        out = im2double(imread(mstring('guide/guide6.jpg')))
    elif index == 7:
        out = im2double(imread(mstring('guide/guide7.jpg')))
    elif index == 8:
        out = im2double(imread(mstring('guide/guide8.jpg')))
    elif index == 9:
        out = im2double(imread(mstring('guide/guide9.jpg')))
    elif index == 10:
        out = im2double(imread(mstring('guide/guide10.jpg')))
    elif index == 11:
        out = im2double(imread(mstring('guide/guide11.jpg')))
    elif index == 12:
        out = im2double(imread(mstring('guide/guide12.jpg')))
        end

        end