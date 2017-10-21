@mfunction("out")
def drawParallelLine(_in=None, angle=None, n=None):

    # Summary - draw parallel line one the image

    # random line data
    [M, N] = size(_in)
    lineData = zeros(n, 3)
    p1 = randperm(M)
    p2 = randperm(N)
    p3 = randperm(floor(M / 2))
    for i in mslice[1:n]:
        lineData(i, 1).lvalue = p1(i)
        lineData(i, 2).lvalue = p2(i)
        lineData(i, 3).lvalue = p3(i)
        fprintf(mstring('%d: %d %d %d\\n'), i, lineData(i, 1), lineData(i, 2), lineData(i, 3))
        end

        # draw line
        c = floor(N / 150)
        b = 1
        if angle < 0:
            b = -1; print b
            end
            for i in mslice[1:M]:
                for j in mslice[1:N]:
                    for k in mslice[1:n]:
                        for l in mslice[1:c]:
                            deltax = i - (lineData(k, 1) - l)
                            deltay = j - (lineData(k, 2) + l * b)
                            thita = atan(deltay / deltax)
                            if norm(thita - angle) < 0.01 and norm(mcat([i, j]) - mcat([(lineData(k, 1) - l), (lineData(k, 2) + l)])) < lineData(k, 3):
                                _in(i, j).lvalue = 1
                                end
                                end
                                end
                                end
                                end
                                out = _in

                                end