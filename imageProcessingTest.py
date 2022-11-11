import cv2, numpy as np
import matplotlib.pylab as plt

# img1 = cv2.imread('../img/taekwonv1.jpg')
# img2 = cv2.imread('../img/taekwonv2.jpg')
# img3 = cv2.imread('../img/taekwonv3.jpg')
# img4 = cv2.imread('../img/dr_ochanomizu.jpg')



originImg6099 = cv2.imread('./Downloads/originImages/629/IMG_6099.JPG')
originImg6100 = cv2.imread('./Downloads/originImages/629/IMG_6100.JPG')
originImg6102 = cv2.imread('./Downloads/originImages/629/IMG_6102.JPG')
originImg6105 = cv2.imread('./Downloads/originImages/629/IMG_6105.JPG')
originImg6107 = cv2.imread('./Downloads/originImages/629/IMG_6107.JPG')
originImg6109 = cv2.imread('./Downloads/originImages/629/IMG_6109.JPG')
originImg6111 = cv2.imread('./Downloads/originImages/629/IMG_6111.JPG')
originImg6115 = cv2.imread('./Downloads/originImages/629/IMG_6115.JPG')
originImg6118 = cv2.imread('./Downloads/originImages/629/IMG_6118.JPG')
originImg6126 = cv2.imread('./Downloads/originImages/629/IMG_6126.JPG')
originImg6128 = cv2.imread('./Downloads/originImages/629/IMG_6128.JPG')
originImg6129 = cv2.imread('./Downloads/originImages/629/IMG_6129.JPG')
originImg6132 = cv2.imread('./Downloads/originImages/629/IMG_6132.JPG')
originImg6135 = cv2.imread('./Downloads/originImages/629/IMG_6135.JPG')
originImg6140 = cv2.imread('./Downloads/originImages/629/IMG_6140.JPG')
originImg6144 = cv2.imread('./Downloads/originImages/629/IMG_6144.JPG')
originImg6149 = cv2.imread('./Downloads/originImages/629/IMG_6149.JPG')
originImg6155 = cv2.imread('./Downloads/originImages/629/IMG_6155.JPG')
originImg6156 = cv2.imread('./Downloads/originImages/629/IMG_6156.JPG')
originImg6159 = cv2.imread('./Downloads/originImages/629/IMG_6159.JPG')
originImg6162 = cv2.imread('./Downloads/originImages/629/IMG_6162.JPG')
originImg6164 = cv2.imread('./Downloads/originImages/629/IMG_6164.JPG')
originImg6167 = cv2.imread('./Downloads/originImages/629/IMG_6167.JPG')
originImg6168 = cv2.imread('./Downloads/originImages/629/IMG_6168.JPG')
originImg6169 = cv2.imread('./Downloads/originImages/629/IMG_6169.JPG')

testImg629_18378216_96 = cv2.imread('./Downloads/testImages/629-18378216-96.jpg')
testImg629_18378216_97 = cv2.imread('./Downloads/testImages/629-18378216-97.jpg')
testImg629_18378216_98 = cv2.imread('./Downloads/testImages/629-18378216-98.jpg')
testImg629_18378216_99 = cv2.imread('./Downloads/testImages/629-18378216-99.jpg')
testImg629_18378216_100 = cv2.imread('./Downloads/testImages/629-18378216-100.jpg')
testImg629_18378216_101 = cv2.imread('./Downloads/testImages/629-18378216-101.jpg')
testImg629_18378216_102 = cv2.imread('./Downloads/testImages/629-18378216-102.jpg')
testImg629_18378216_103 = cv2.imread('./Downloads/testImages/629-18378216-103.jpg')
testImg629_18378216_104 = cv2.imread('./Downloads/testImages/629-18378216-104.jpg')
testImg629_18378216_105 = cv2.imread('./Downloads/testImages/629-18378216-105.jpg')
testImg629_18378216_106 = cv2.imread('./Downloads/testImages/629-18378216-106.jpg')
testImg629_18378216_107 = cv2.imread('./Downloads/testImages/629-18378216-107.jpg')
testImg629_18378216_108 = cv2.imread('./Downloads/testImages/629-18378216-108.jpg')
testImg629_18378216_109 = cv2.imread('./Downloads/testImages/629-18378216-109.jpg')
testImg629_18378216_110 = cv2.imread('./Downloads/testImages/629-18378216-110.jpg')
testImg629_18378216_111 = cv2.imread('./Downloads/testImages/629-18378216-111.jpg')
testImg629_18378216_112 = cv2.imread('./Downloads/testImages/629-18378216-112.jpg')
testImg629_18378216_113 = cv2.imread('./Downloads/testImages/629-18378216-113.jpg')

cv2.imshow('query', originImg6099)
# imgs = [img1, img2, img3, img4]
# 추가
originImages = [originImg6099,originImg6100,originImg6102,originImg6105,originImg6107,originImg6109,originImg6111,originImg6115,originImg6118,originImg6126,originImg6128,originImg6129,originImg6132,originImg6135,originImg6140,originImg6144,originImg6149,originImg6155,originImg6156,originImg6159,originImg6162,originImg6164,originImg6167,originImg6168,originImg6169]
fakeImages = [testImg629_18378216_96 ,testImg629_18378216_97 ,testImg629_18378216_98 ,testImg629_18378216_99 ,testImg629_18378216_100 ,testImg629_18378216_101 ,testImg629_18378216_102 ,testImg629_18378216_103 ,testImg629_18378216_104 ,testImg629_18378216_105 ,testImg629_18378216_106 ,testImg629_18378216_107 ,testImg629_18378216_108 ,testImg629_18378216_109 ,testImg629_18378216_110 ,testImg629_18378216_111 ,testImg629_18378216_112 ,testImg629_18378216_113]
hists = []

for i, eachOriginImage in enumerate(originImages) : 
    plt.subplot(1,len(originImages),i+1)
    plt.title('eachOriginImage%d'% (i+1))
    plt.axis('off') 
    plt.imshow(eachOriginImage[:,:,::-1])
    #---① 각 이미지를 HSV로 변환
    hsv = cv2.cvtColor(eachOriginImage, cv2.COLOR_BGR2HSV)
    #---② H,S 채널에 대한 히스토그램 계산
    hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0, 256])
    #---③ 0~1로 정규화
    cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
    hists.append(hist)


# for k, eachOriginImage in enumerate(originImages) : 
  

query = hists[0]
methods = {'CORREL' :cv2.HISTCMP_CORREL, 'CHISQR':cv2.HISTCMP_CHISQR, 
           'INTERSECT':cv2.HISTCMP_INTERSECT,
           'BHATTACHARYYA':cv2.HISTCMP_BHATTACHARYYA}

for j, (name, flag) in enumerate(methods.items()):
    print('%-10s'%name, end='\t')
    for i, (hist, img) in enumerate(zip(hists, fakeImages)):
        #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
        ret = cv2.compareHist(query, hist, flag)
        if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
            ret = ret/np.sum(query)        #비교대상으로 나누어 1로 정규화
        print("img%d:%7.2f"% (i+1 , ret), end='\t')
    print()
plt.show()