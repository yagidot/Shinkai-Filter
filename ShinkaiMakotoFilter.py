@mfunction("light")
def ShinkaiMakotoFilter(src=None, target=None, sky=None):

    # Summary - function version

    # preparation
    [M, N, C] = size(src)

    # Step1: median filtering
    fprintf(mstring('\\nStep1: median filtering\\n'))
    blur = changeStyle(src, M * N)

    # Step2: color transfer (guide)
    fprintf(mstring('\\nStep2: color transfer\\n'))
    color = cf_reinhard(blur, target)

    # Step3: adjust (saturation, brightness)
    fprintf(mstring('\\nStep3: adjust\\n'))
    adjust = adjustHSV(color)

    # Step4: paste sky (sky)
    fprintf(mstring('\\nStep4: paste sky\\n'))
    [skyMask, mask_threshold, mask_dilate, mask_erode] = findSky(src)
    changeSky = pasteSky(adjust, sky, skyMask)

    # Step5: add light (light source)
    fprintf(mstring('\\nStep5: add light\\n'))
    [light, light_filter] = addLight(src, changeSky, M, N)

    # show
    figure()
    imshow(src)
    title(mstring('src'))
    figure()
    imshow(blur)
    title(mstring('Step1: median filtering'))
    figure()
    imshow(target)
    title(mstring('guide'))
    figure()
    imshow(color)
    title(mstring('Step2: color transform'))
    figure()
    imshow(adjust)
    title(mstring('Step3: adjust'))
    figure()
    imshow(mask_threshold)
    title(mstring('Step4-1: threshold'))
    figure()
    imshow(mask_dilate)
    title(mstring('Step4-2: dilation'))
    figure()
    imshow(mask_erode)
    title(mstring('Step4-3: erosion'))
    figure()
    imshow(skyMask)
    title(mstring('Step4-3: sky mask'))
    figure()
    imshow(changeSky)
    title(mstring('Step4: paste sky'))
    figure()
    imshow(light_filter)
    title(mstring('light filter'))
    figure()
    imshow(light)
    title(mstring('Step5: add light'))

    end