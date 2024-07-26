import numpy as np
x = np.arange(33)
sum(x)/33

sum((x-16)*1/33)
(x - 16)**2


np.unique((x-16)**2)*(2/33)
sum(np.unique((x-16)**2)*(2/33)) #np.float64(90.66666666666667)


#E[X^2]
sum(x**2 * (1/33))

#Var(X) = E[X^2] - (E[X])^2
sum(X**2 * (1/33)) - 16**2



##example1
x=np.arange(4)
x
pro_x = np.array([1/6, 2/6, 2/6, 1/6])
pro_x

#기대값
EX = sum(x * pro_x)
EXX = sum(x**2 * pro_x)

#분산
EXX-EX**2
sum((x - EX)**2 * pro_x)





##example2
x=np.arange(99)
x
#1-50-1벡터
x_1_50_1 = np.concatenate((np.arange(1, 51), np.arange(49, 0, -1)))
pro_x = x_1_50_1/2500

#기대값
EX = sum(x * pro_x)
EXX = sum(x**2 * pro_x)

#분산
EXX-EX**2
sum((x - EX)**2 * pro_x)




##example3
y = np.arange(4)*2
y
pro_y = np.array([1/6, 2/6, 2/6, 1/6])
pro_y

#기대값
EX = sum(y * pro_y)
EXX = sum(y**2 * pro_y)

#분산
EXX-EX**2
sum((y - EX)**2 * pro_y)



#분산 구하기 n = 10, 표준편차 = 9.52
np.sqrt(9.52**2 / 10)












