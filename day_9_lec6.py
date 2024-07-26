#강의안 6. 행렬

import numpy as np
# 두 개의 벡터를 합쳐 행렬 생성
matrix = np.column_stack((np.arange(1, 5),
 np.arange(12, 16)))
print("행렬:\n", matrix)

matrix = np.vstack((np.arange(1, 5),
 np.arange(12, 16)))
print("행렬:\n", matrix) #프린트함수를 쓰면 어레이에서 형식이 바뀜

#빈행렬만들기
np.zeros(5)
np.zeros([5, 4])

#채우면서 리쉐입하기기
np.arange(1, 5).reshape((2, 2))
np.arange(1, 7).reshape((2, 3))
#-1을 통해서 크기를 자동으로 결정할 수 있음
np.arange(1, 7).reshape((2, -1))

#quiz.0에서 99까지 수 중 랜덤하게 50개 숫자를 뽑아서
#5 by 10행렬을 만드세요.
import numpy as np
np.random.seed(2024)
a = np.random.randint(1, 100, 50).reshape((5, -1))
a

# 행우선, 열우선
np.arange(1, 21).reshape((4, 5), order = "F")
np.arange(1, 5).reshape((2, 2), order='C')


mat_a = np.arange(1, 21).reshape((4, 5), order = "F")
mat_a

#인덱싱
mat_a[0, 0] #np.int64(1)
mat_a[1, 1] #np.int64(6)
mat_a[2, 3] #np.int64(15)

mat_a[0:2, 3] #array([13, 14])
mat_a[1:3, 1:4]

#행자리, 열자리 비어있는 경우 전체 행, 또는 열 선택
mat_a[3, ]
mat_a[3, :] #array([ 4,  8, 12, 16, 20])
mat_a[3,::2] #array([ 4, 12, 20])

#짝수행만 선택하려면?
mat_b = np.arange(1, 101).reshape((20, -1))
mat_b
mat_b[1::2, :]

mat_b = np.arange(1, 101).reshape((20, -1))
mat_b
mat_b[[1, 4, 6, 14], ]

#행렬 필터링
x = np.arange(1, 11).reshape((5, 2)) * 2
print("행렬 x:\n", x)
filtered_elements = x[[True, True, False, False, True], 0]
print("첫 번째 열의 첫 번째, 두 번째, 다섯 번째 행의 원소:\n", filtered_elements)

mat_b[:,1] #벡터
mat_b[:,1].reshape((-1,1)) #행렬
mat_b[:,(1,)]
mat_b[:,1:2]#행렬
mat_b[:,[1]]
mat_b[:,1:2]


#필터링
mat_b[mat_b[:,1]%7 == 0, :] #7의 배수가 있는 줄을 다 불러옴.
mat_b[mat_b[:,1]%7 == 0, 2] #7의 배수가 있는 줄에서 3번째 요소를 불러옴.


#사진은 행렬이다.
import numpy as np
import matplotlib.pyplot as plt

# 난수 생성하여 3x3 크기의 행렬 생성
np.random.seed(2024)
img1 = np.random.rand(3, 3)
print("이미지 행렬 img1:\n", img1)

plt.imshow(img1, cmap='gray', interpolation='nearest')
plt.colorbar()
plt.show()


#강의안 6.0.6.b 행렬에서 사진으로(0이 검은색, 1에 가까울 수록 흰색)
a = np.random.randint(0, 10, 20).reshape((4, -1))
a/9 #9는 a 원소 개수, 9로 나누니 0~1의 값으로 형성
plt.imshow(a/9, cmap='gray', interpolation='nearest')
plt.colorbar()
plt.show()

#6.0.7 행렬의 연산
# 5행 2열의 행렬 생성
x = np.arange(1, 11).reshape((5, 2)) * 2
print("원래 행렬 x:\n", x)
transposed_x = x.transpose()
print("전치된 행렬 x:\n", transposed_x)

#18페이지에서 코드 따와서 사진 저장함.
import urllib.request
img_url = "https://bit.ly/3ErnM2Q"
urllib.request.urlretrieve(img_url, "jelly.png")

!pip install imageio
import imageio
import matplotlib.pyplot as plt

# 이미지 읽기
jelly = imageio.imread("img/jelly.png")
print("이미지 클래스:", type(jelly))
print("이미지 차원:", jelly.shape)
print("이미지 첫 4x4 픽셀, 첫 번째 채널:\n", jelly[:4, :4, 0])


#첫 3개의 채널은 해당 위치의 빨강, 녹색, 파랑의 색깔 강도를 숫자로 표현합니다.
#마지막 채널은 투명도를 결정합니다.
jelly[:,:,0]
jelly[:,:,1]
jelly[:,:,2]
jelly[:,:,3]


jelly[:,:,0].shape
jelly[:,:,0].transpose().reshape #첫번째 장이 그린임을 알 수 있음.

plt.imshow(jelly[:,:,0].transpose())
plt.axis('off') #축 정보 없애기
plt.show()
plt.clf()

plt.imshow(jelly[:,:,0]) #R
plt.axis('off') #축 정보 없애기
plt.show()
plt.clf()

plt.imshow(jelly[:,:,1]) #G
plt.axis('off') #축 정보 없애기
plt.show()
plt.clf()

plt.imshow(jelly[:,:,2]) #B
plt.axis('off') #축 정보 없애기
plt.show()
plt.clf()

plt.imshow(jelly[:,:,3]) #투명도
plt.axis('off') #축 정보 없애기
plt.show()
plt.clf()

#강의안 16p
import numpy as np
# 두 개의 2x3 행렬 생성
mat1 = np.arange(1, 7).reshape(2, 3)
mat1
mat2 = np.arange(7, 13).reshape(2, 3)
mat2

my_array = np.array([mat1, mat2])
my_array
my_array.shape #(2, 2, 3) 2 by 3짜리가 두장 있다. #장,행,열 순으로로


first_slice = my_array[0, :, :]
first_slice

filtered_array = my_array[:, :, :-1]
filtered_array


#연습해보기
my_array[:, :, [0, 2]]
my_array

my_array[:, 0, :]
my_array

my_array[0, 1, 1:3]
#my_array[0, 1, [1, 2]]

mat_x = np.arange(1, 101).reshape((5, 5, 4))
mat_x

mat_y = np.arange(1, 101).reshape((10,5, 2))
mat_y
len(mat_y) #장수를 의미

my_array2 = np.array([my_array, my_array])
my_array2
my_array2[0, :, :, :]
my_array2.shape


#넘파이 어레이 메서드
a = np.array([[1, 2, 3], [4, 5, 6]])
a.sum()
a.sum(axis = 0)
a.sum(axis = 1)

a.mean()
a.mean(axis = 0)
a.mean(axis = 1)

mat_b = np.random.randint(1, 100, 50).reshape((5, -1))
mat_b

#가장 큰수?
mat_b.max()

#행별로 가장 큰 수?
mat_b.max(axis = 1)

#열별로 가장 큰 수?
mat_b.max(axis = 0)


a = np.array([1, 3, 2, 5]).reshape((2, 2))
a.cumsum()


mat_b = np.random.randint(1, 100, 50).reshape((5, -1))
mat_b
mat_b.sum()
mat_b.cumsum(axis = 1) #행별 누적합

a = np.array([1, 3, 2, 5]).reshape((2, 2))
a.cumprod(axis = 1)


mat_b.reshape((2, 5, 5)) #3차원
mat_b.flatten() #1차원으로 배열해줌

#6.0.13 clip
d = np.array([1, 2, 3, 4, 5])
d.clip(2, 4) #최대, 최소 설정

type(d) #array
type(d.tolist()) #list








