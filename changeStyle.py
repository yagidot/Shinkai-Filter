@mfunction("out")
def changeStyle(_in=None, pixel=None):

    # Summary - use median filtering change image style

    # decide filter size
    if (pixel < 2000000):
        s = 3; print s

    else:
        s = 5; print s

        end

        # median filtering
        out(mslice[:], mslice[:], 1).lvalue = ordfilt2(_in(mslice[:], mslice[:], 1), 5, ones(s, s))
        out(mslice[:], mslice[:], 2).lvalue = ordfilt2(_in(mslice[:], mslice[:], 2), 5, ones(s, s))
        out(mslice[:], mslice[:], 3).lvalue = ordfilt2(_in(mslice[:], mslice[:], 3), 5, ones(s, s))

        end