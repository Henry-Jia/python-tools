import cv2
import numpy as np
from matplotlib import pyplot as plt

img_1 = cv2.imread('1.jpg')
img1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
img_2 = cv2.imread('2.jpg')
img2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
img_3 = cv2.imread('3.jpg')
img3 = cv2.cvtColor(img_3, cv2.COLOR_BGR2GRAY)

trainImg = [img2, img1, img3]
sift = cv2.xfeatures2d.SIFT_create()

s = trainImg[0]
temp = img_2
temp1 = img_1
for i in trainImg[1:]:
    print("loop....")
    kp1, des1 = sift.detectAndCompute(i, None)
    kp2, des2 = sift.detectAndCompute(s, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    good = []
    for m in matches:
        if m[0].distance < 0.5 * m[1].distance:
            good.append(m)

    matches = np.asarray(good)

    if len(matches[:, 0]) >= 4:

        print("reach here")
        src = np.float32([kp1[m.queryIdx].pt for m in matches[:, 0]]).reshape(-1, 1, 2)
        dst = np.float32([kp2[m.trainIdx].pt for m in matches[:, 0]]).reshape(-1, 1, 2)
        H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
        # print H
    else:
        raise AssertionError("Can’t find enough keypoints.")

    dst = cv2.warpPerspective(temp1, H, (temp.shape[1] + temp1.shape[1], temp.shape[0]))
    plt.subplot(122), plt.imshow(dst), plt.title("Warped Image")
    plt.show()
    plt.figure()
    dst[0:temp1.shape[0], 0:temp1.shape[1]] = temp1
    s = dst
    temp = img_3
    temp1 = dst
cv2.imwrite("output.jpg", dst)
plt.imshow(dst)
plt.show()





