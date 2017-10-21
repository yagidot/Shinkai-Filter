@mfunction("est_im")
def cf_reinhard(source=None, target=None):
    #CF_REINHARD computes Reinhard's image colour transfer
    #
    #   CF_REINHARD(SOURCE,TARGET) returns the colour transfered source
    #   image SOURCE according to the target image TARGET.
    #

    #   Copyright 2015 Han Gong <gong@fedoraproject.org>, University of East
    #   Anglia.

    #   References:
    # Erik Reinhard, Michael Ashikhmin, Bruce Gooch and Peter Shirley, 
    # 'Color Transfer between Images', IEEE CG&A special issue on Appliedi
    # Perception, Vol 21, No 5, pp 34-41, September - October 2001

    [x, y, z] = size(source)
    img_s = reshape(im2double(source), mcat([]), 3)
    img_t = reshape(im2double(target), mcat([]), 3)

    a = mcat([0.3811, 0.5783, 0.0402, OMPCSEMI, 0.1967, 0.7244, 0.0782, OMPCSEMI, 0.0241, 0.1288, 0.8444])
    b = mcat([1 / sqrt(3), 0, 0, OMPCSEMI, 0, 1 / sqrt(6), 0, OMPCSEMI, 0, 0, 1 / sqrt(2)])
    c = mcat([1, 1, 1, OMPCSEMI, 1, 1 - 2, OMPCSEMI, 1 - 1, 0])
    b2 = mcat([sqrt(3) / 3, 0, 0, OMPCSEMI, 0, sqrt(6) / 6, 0, OMPCSEMI, 0, 0, sqrt(2) / 2])
    c2 = mcat([1, 1, 1, OMPCSEMI, 1, 1 - 1, OMPCSEMI, 1 - 2, 0])

    img_s = max(img_s, 1 / 255)
    img_t = max(img_t, 1 / 255)

    # convert to LMS space
    LMS_s = a * img_s.cT
    LMS_t = a * img_t.cT

    # take the log of LMS
    LMS_s = log10(LMS_s)
    LMS_t = log10(LMS_t)

    # convert to lab space
    lab_s = b * c * LMS_s
    lab_t = b * c * LMS_t

    # compute mean and std
    mean_s = mean(lab_s, 2)
    std_s = std(lab_s, 0, 2)
    mean_t = mean(lab_t, 2)
    std_t = std(lab_t, 0, 2)

    res_lab = zeros(3, x * y)

    sf = std_t /eldiv/ std_s

    for ch in mslice[1:3]:    # for each channel, apply the statistical alignment
        res_lab(ch, mslice[:]).lvalue = (lab_s(ch, mslice[:]) - mean_s(ch)) * sf(ch) + mean_t(ch)
        end

        # convert back to LMS
        LMS_res = c2 * b2 * res_lab
        for ch in mslice[1:3]:
            LMS_res(ch, mslice[:]).lvalue = 10. ** LMS_res(ch, mslice[:])
            end

            # convert back to RGB
            est_im = (mcat([4.4679 - 3.5873, 0.1193, OMPCSEMI, -1.2186, 2.3809 - 0.1624, OMPCSEMI, 0.0497 - 0.2439, 1.2045]) * LMS_res).cT
            est_im = reshape(est_im, size(source))        # reshape the image