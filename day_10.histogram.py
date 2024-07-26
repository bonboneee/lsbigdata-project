import numpy as np
import matplotlib.pyplot as plt

#0~1사이의 10개 숫자를 뽑아 히스토그램으로 만들기
#예제 넘파이 배열 생성
data = np.random.rand(10)

#히스토그램 그리기
plt.hist(data, bins=4, alpha=0.7, color = 'blue')
plt.title('Histogram of Numpy Vector')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()
plt.clf()



#0~1사이에서 5개의 표본, 10000번 반복하여 표본의 평균을 히스토그램으로
#data_1 = np.random.rand(50000).reshape(-1,5).mean(axis = -1)
data_1 = np.random.rand(10000, 5).mean(axis = -1)
data_1
plt.hist(data_1, bins = 30, alpha = 0.7, color = 'blue')
plt.title('Histogram of Numpy Vector')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()
plt.clf()



