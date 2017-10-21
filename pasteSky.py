@mfunction("output")
def pasteSky(input=None, sky=None, skyMask=None):

    # Summary - paste shinkai makoto style sky

    # preparation
    size(input)
    size(sky)
    size(skyMask)
    output = input
    LALPH = 0.5

    # paste
    for i in mslice[1:m2]:
        if (max(skyMask(i, mslice[:]) == 1)):
            a1 = i
            break
            end
            end
            for i in mslice[m2:-1:1]:
                if (max(skyMask(i, mslice[:]) == 1)):
                    a2 = i
                    break
                    end
                    end
                    for j in mslice[1:n2]:
                        if (max(skyMask(mslice[:], j) == 1)):
                            b1 = j
                            break
                            end
                            end
                            for j in mslice[n2:-1:1]:
                                if (max(skyMask(mslice[:], j) == 1)):
                                    b2 = j
                                    break
                                    end
                                    end
                                    theta = 0
                                    scale = max((a2 - a1) / m1, (b2 - b1) / n1); print scale

                                    tform = affine2d(mcat([scale * cosd(theta) - scale * sind(theta), 0, OMPCSEMI, scale * sind(theta), scale * cosd(theta), 0, OMPCSEMI, 0, 0, 1]))
                                    sky = imwarp(sky, tform)
                                    size(sky)
                                    for i in mslice[1:m]:
                                        for j in mslice[1:n]:
                                            if skyMask(i, j) == 1:
                                                output(i, j, mslice[:]).lvalue = sky(mod(i, m1) + 1, mod(j, n1) + 1, mslice[:]) * LALPH + input(i, j, mslice[:]) * (1 - LALPH)
                                                end
                                                end
                                                end

                                                end