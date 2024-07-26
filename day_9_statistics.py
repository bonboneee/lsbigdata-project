#균일 확률 변수 만들기
import numpy as np
np.random.rand(1)

def X(num):
    return np.random.rand(num)
    
X(1)
X(1)
X(1)
#= X(3)


#베르누이 확률변수 모수: P 만들어보세요!
def Y(num, p):
    x = np.random.rand(num)
    return np.where(x < p, 1, 0)
#Y(5, 0.5) #array([0, 1, 0, 1, 0])

Y(num = 100, p = 0.5).mean()
Y(num = 10000, p = 0.5).mean() #대수법칙: 시행횟수가 많아지면 0.5에 더욱 가까워짐.

#새로운 확률 변수
#가질 수 있는 값: 0, 1, 2
#20%, 50%, 30%
 

def Z():
    x = np.random.rand(1)
    return np.where(x <0.2, 0, np.where(x<0.7, 1,2))

Z()


#
p = np.array([0.2,0.5,0.3])
def Z(p):
    x = np.random.rand(1)
    p_cumsum = p.cumsum()
    return np.where(x < p_cumsum[0], 0, np.where(x< p_cumsum[1],1, 2))

Z(p)


#E[X] 구하기
import numpy as np
sum(np.arange(4)*np.array([1, 2, 2, 1]) /6)




