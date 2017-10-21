@mfunction("out")
def drawRadixLine(_in=None, x=None, y=None, n=None):

    # Summary - draw radix line on input image

    # preparation
    fprintf(mstring('\\nDraw light line.\\n'))
    [M, N] = size(_in)
    lineData = zeros(4 * n, 3)
    count = 0

    # random line data (angle, dis, length)
    p1 = randperm(90)
    p2 = randperm(floor(50 * n))
    p3 = randperm(M)
    for i in mslice[1:4 * n]:
        lineData(i, 1).lvalue = (p1(i) + floor((i - 1) / 4) * 90) * pi / 180
        lineData(i, 2).lvalue = p2(i)
        lineData(i, 3).lvalue = p3(i) + N
        fprintf(mstring('%d: %d(%d) %d %d\\n'), i, lineData(i, 1), p1(i), lineData(i, 2), lineData(i, 3))
        end

        # draw line
        for i in mslice[1:M]:
            for j in mslice[1:N]:
                newx = i - x
                newy = j - y
                angle = atan(newy / newx)
                if (newx < 0):
                    angle = angle + pi; print angle

                elif (newy < 0):
                    angle = angle + 2 * pi; print angle

                    end
                    for k in mslice[1:4 * n]:
                        v = abs(angle - lineData(k, 1))
                        if (v < 0.01):
                            d = norm(mcat([newx, newy]) - mcat([0, 0]))
                            if (d > lineData(k, 2) and d < lineData(k, 2) + lineData(k, 3)):
                                _in(i, j).lvalue = 1
                                count = count + 1
                                end

                                end
                                end
                                end
                                end
                                out = _in
                                fprintf(mstring('%d %d count = %d\\n'), x, y, count)

                                end