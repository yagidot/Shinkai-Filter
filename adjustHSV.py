@mfunction("out")
def adjustHSV(_in=None, guide=None, M=None, N=None):

    # Summary - adjust image light and saturation in HSV color space

    # convert
    out = rgb2hsv(_in)
    # g = rgb2hsv(guide);
    # [m, n, c] = size(guide);

    # choose parameter
    # sumH = 0;
    #sumS = 0;
    #sumV = 0;
    #for i=1:M
    #    for j=1:N
    #        sumH = sumH + out(i, j, 2);
    #        sumS = sumS + out(i, j, 2);
    #        sumV = sumV + out(i, j, 3);
    #    end
    #end
    #aveH1 = sumH/M/N;
    #aveS1 = sumS/M/N;
    #aveV1 = sumV/M/N;
    #sumH = 0;
    #sumS = 0;
    #sumV = 0;
    #for i=1:m
    #    for j=1:n
    #        sumH = sumH + g(i, j, 2);
    #        sumS = sumS + g(i, j, 2);
    #        sumV = sumV + g(i, j, 3);
    #    end
    #end
    #aveH2 = sumH/M/N;
    #aveS2 = sumS/m/n;
    #aveV2 = sumV/m/n;
    #H = aveH2 - aveH1;
    #S = aveS2 - aveS1;
    #V = aveV2 - aveV1;

    # adjust
    # out(:,:,1) = out(:,:,1) + H;
    out(mslice[:], mslice[:], 2).lvalue = out(mslice[:], mslice[:], 2) + 0.2
    out(mslice[:], mslice[:], 3).lvalue = out(mslice[:], mslice[:], 3) + 0.35
    out = hsv2rgb(out)

    end
