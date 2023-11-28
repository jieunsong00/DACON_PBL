# %%
#hiddencell
from pbl_tools import *

# %% [markdown]
# # 스테이지 3

# %% [markdown]
# # 1.라이브러리 import
# [문제 1]  
# numpy 라이브러리를 불러와 주세요. 단, numpy는 자주 사용하는 라이브러리이므로 축약어인 np로 불러와주세요.  
# 아래 빈칸을 채워주세요.

# %%
import ___ as np

# %%
#checkcode
ensure_vals(globals(), 'np')
@check_safety
def check(user_answer_pandas=np):
    if hasattr(user_answer_pandas, 'array'):
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# 
# 파이썬에서는 `import <라이브러리 이름>` 명령어을 사용해 필요한 라이브러리를 불러옵니다. `import numpy as np`에서 as 를 사용한 이유는 자주 사용하는 명령어를 매번 입력해야 하는 수고를 덜기 위함입니다. 즉, 자주 사용하는 명령어를 쉽게 사용할 수 있도록 라이브러리를 할당하는 역할을 합니다. 이후에는 `np`라는 이름으로 Numpy 라이브러리의 함수와 기능을 사용할 수 있습니다. 

# %% [markdown]
# ### Hint.
# np는 numpy의 약칭입니다. import 와 as를 이용해서 numpy 라이브러리를 불러와주세요.

# %% [markdown]
# ### Solution.
# ```python
# import numpy as np
# ```

# %% [markdown]
# # 2.2차원 배열 생성

# %%
two_array = np.array([[1,2,3],
                      [4,5,6]])
two_array

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 2차원 배열은 2차원이니 축이 2개 있습니다. axis = 0과 axis = 1이 존재하지요. 위의 결과는 행과 열이 존재하는 행렬이 출력되었네요.
# 
# 
# 
# 

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 3.ndim

# %%
two_array.ndim

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst. 
# `.ndim` 함수를 사용하면 해당 배열(two_array)의 **차원 수(배열의 축 수)** 를 알 수 있습니다. 위에서 말했다시피 two_array는 2차원 배열이므로 2가 출력될 것입니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 4.shape

# %%
two_array.shape

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# `.shape` 함수를 이용하면 배열 **각 차원의 크기**가 튜플 형태로 출력됩니다. 위에서 출력된 값은 1차원에 2, 2차원에 3을 (2,3)으로 표현합니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 5.size

# %%
two_array.size

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# `.size` 함수를 이용하면 **전체 원소의 갯수**를 출력합니다. two_array의 원소는 1,2,3,4,5,6으로 6개의 원소가 존재합니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 6.dtype

# %%
two_array.dtype

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# `.dtype` 함수를 이용하면 배열의 **데이터 유형**이 출력됩니다. two_array는 정수로 이루어져 있으므로 int가 출력되네요.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 7.3차원 배열 생성

# %%
three_array = np.array([[[1.0,2.0],
                         [3.0,4.0],
                         [5.0,6.0]],
                        [[7.0,8.0],
                         [9.0,10.0],
                         [11.0,12.0]]])
three_array

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 3차원 배열은 3차원이니 축이 3개 있습니다. axis = 0, axis = 1, axis = 2가 존재하지요. 위의 결과는 깊이, 행, 열이 존재하는 텐서가 출력되었네요.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 8.차원의 수
# 
# [문제 2]  
# 위에서 생성한 three_array가 몇 차원 array인지 확인하는 코드를 작성해 보세요.  
# 아래 빈칸을 채워주세요.  

# %%
three_array.___

# %%
#checkcode
ensure_vals(globals(),'three_array')
@check_safety
def check(user_answer=_):
    if user_answer == three_array.ndim:
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# 해당 배열의 차원 수 (배열의 축 수)를 알 수 있는 함수를 작성해 보세요. three_array는 3차원 배열이므로 3이 출력될 것입니다.

# %% [markdown]
# ### Hint.
# `.ndim` 함수를 사용하면 해당 배열의 차원 수 (배열의 축 수)를 알 수 있습니다.

# %% [markdown]
# ### Solution.
# ```python
# three_array.ndim
# ```

# %% [markdown]
# # 9.차원의 크기
# 
# [문제 3]  
# three_array에서 배열 각 차원의 크기를 튜플 형태로 출력해 보세요.  
# 아래 빈칸을 채워주세요.  

# %%
three_array.___

# %%
#checkcode
ensure_vals(globals(),'three_array')
@check_safety
def check(user_answer=_):
    if user_answer == three_array.shape:
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# 
# 배열 각 차원의 크기가 튜플 형태로 출력되는 함수를 작성해 보세요. three_array는 1차원에 2, 2차원에 3, 3차원에 2가 (2,3,2)로 표현될 것입니다.

# %% [markdown]
# ### Hint.
# `.shape` 함수를 이용하면 배열 **각 차원의 크기**가 튜플 형태로 출력됩니다.

# %% [markdown]
# ### Solution.
# ```python
# three_array.shape
# ```

# %% [markdown]
# # 10.전체 원소의 갯수
# [문제 4]  
# three_array에서 전체 원소의 갯수를 출력해 보세요.  
# 아래 빈칸을 채워주세요.  

# %%
three_array.___

# %%
#checkcode
ensure_vals(globals(),'three_array')
@check_safety
def check(user_answer=_):
    if user_answer == three_array.size:
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# 전체 원소의 갯수가 출력되는 함수를 작성해 보세요. three_array의 원소는 총 12개의 원소가 존재합니다.

# %% [markdown]
# ### Hint.
# `.size` 함수를 이용하면 전체 원소의 갯수를 출력합니다.

# %% [markdown]
# ### Solution.
# ```python
# three_array.size
# ```

# %% [markdown]
# # 11.데이터 타입
# 
# [문제 5]  
# three_array의 데이터 유형을 출력해 보세요.

# %%


# %%
#checkcode
ensure_vals(globals(),'three_array')
@check_safety
def check(user_answer=_):
    if user_answer == three_array.dtype:
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# 데이터 유형을 출력하는 함수를 작성해 보세요. three_array는 소수로 이루어져 있으므로 float 타입입니다.

# %% [markdown]
# ### Hint.
# `.dtype` 함수를 이용하면 데이터 유형을 알 수 있습니다.

# %% [markdown]
# ### Solution.
# ```python
# three_array.dtype
# ```


