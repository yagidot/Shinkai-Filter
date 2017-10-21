@mfunction("out")
def drawCircle(_in=None, x=None, y=None, r=None):

    # Summary - draw circle in input image

    # preparation
    fprintf(mstring('\\nDraw light source.\\n'))
    [M, N] = size(_in)
    count = 0
    min = 5000

    # draw
    for i in mslice[1:M]:
        for j in mslice[1:N]:
            dis = norm(mcat([i, j]) - mcat([x, y]))
            if (dis < min):
                min = dis; print min

                end
                if (dis < r):
                    _in(i, j).lvalue = 1
                    count = count + 1
                    end
                    end
                    end
                    out = _in
                    fprintf(mstring('%d %d %d count = %d / %d\\n'), x, y, r, count, min)

                    end