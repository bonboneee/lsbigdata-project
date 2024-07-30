import pandas as pd
import numpy as np

old_seat = np.arange(1, 29)

np.random.seed(20240729)

#1~28숫자 중에서 중복없이 28개의 숫자를 뽑는 방법
new_seat = np.random.choice(old_seat, 28, replace = False)
result = pd.DataFrame({"old_seat" : old_seat, "new_seat" : new_seat})

pd.DataFrame.to_csv(result, "result_csv")
