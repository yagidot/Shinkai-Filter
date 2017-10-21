#% preparation
close("all")
clear("all")
clc

#% read image
fprintf(mstring('Shinkai Makoto Filter START!\\nRead image.\\n'))
src = im2double(imread(mstring('input/input5.jpg')))
target = im2double(imread(mstring('guide/guide10.jpg')))
sky = im2double(imread(mstring('sky.jpg')))
[M, N, C] = size(src)

#% Step1: median filtering
fprintf(mstring('\\nStep1: median filtering\\n'))
blur = changeStyle(src, M * N)

#% Step2: color transfer (guide)
fprintf(mstring('\\nStep2: color transfer\\n'))
#target = chooseGuide(src, M, N);
color = cf_reinhard(blur, target)

#% Step3: adjust (s,v)
fprintf(mstring('\\nStep3: adjust\\n'))
adjust = adjustHSV(color, src, M, N)

#% Step4: paste sky (sky)
fprintf(mstring('\\nStep4: paste sky\\n'))
[skyMask, mask_threshold, mask_dilate, mask_erode] = findSky(src)
changeSky = pasteSky(adjust, sky, skyMask)

#% Step5: add light
fprintf(mstring('\\nStep5: add light\\n'))
[light, light_filter] = addLight(src, changeSky, M, N)

#% Step6: sharpening
dst = imsharpen(light)

#% show
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
figure()
imshow(dst)
title(mstring('Step6: sharpening'))

#% save
imwrite(blur, mstring('Step1_median_filtering.jpg'))
imwrite(color, mstring('Step2_color_transfer.jpg'))
imwrite(adjust, mstring('Step3_adjust.jpg'))
imwrite(mask_threshold, mstring('Step4-1_threshold.jpg'))
imwrite(mask_dilate, mstring('Step4-2_dilation.jpg'))
imwrite(mask_erode, mstring('Step4-3_erosion.jpg'))
imwrite(changeSky, mstring('Step4_paste_sky.jpg'))
imwrite(light_filter, mstring('Step5-1_light_filter.jpg'))
imwrite(light, mstring('Step5_add_light.jpg'))
imwrite(dst, mstring('Step6_sharpening.jpg'))