import os

import numpy

ORIGIN_IMAGES_PATH = './originImages/'
FAKE_IMAGES_PATH = './testImages/'

originImagesArray = []
fakeImageObject = {}

for i in os.listdir(ORIGIN_IMAGES_PATH):
    if i.__contains__('DS_Store'):
        continue
    else:
        path = ORIGIN_IMAGES_PATH+i+'/'
        # print('for i['+i+'] >>> path: '+path)
        tempJArray = []
        name = i
        for j in os.listdir(path):
            # print('\tfor ['+i+'] j : '+j)
            tempJArray.append(j)
        originImagesArray.append(
            {'photoGroup': name, 'imageArray': tempJArray})

# 응애...

arr = numpy.empty(shape=30000)

# print(arr)
print('fakeImage List JSON 생성중 ...')
# idx, x in enumerate(xs)
lengthh = len(os.listdir(FAKE_IMAGES_PATH))
# print(lengthh)
for index, i in enumerate(os.listdir(FAKE_IMAGES_PATH)):
    # print(i)
    prefix = i.split("-")[0]
    # print(prefix)
    if prefix not in fakeImageObject:
        fakeImageObject[prefix] = []

    fakeImageObject[prefix].append(i)

    print(index+1, ' of ', lengthh)

print(fakeImageObject)
