# %%
#hiddencell
from pbl_tools import *

# %% [markdown]
# # 스테이지 6

# %% [markdown]
# # 1.라이브러리 import
# [문제 1]  
# numpy 라이브러리를 불러와 주세요. 단, numpy는 자주 사용하는 라이브러리이므로 축약어인 np로 불러와주세요.  
# 아래 빈칸을 채워주세요.

# %%


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
# # 2.누적합1(cumsum)

# %%
two_dimension = np.array([[5,10],
                          [15,20]])

np.cumsum(two_dimension)

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 이번 스테이지에서는 간단한 수학적 연산을 배워보겠습니다.
# 
# cumsum 함수를 이용하면 각 원소들의 누적 합을 출력합니다. row와 columns의 구분은 없어지고, 순서대로 sum을 합니다. 
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
# # 3.누적합2(cumsum)

# %%
two_dimension = np.array([[5,10],
                          [15,20]])

np.cumsum(two_dimension, axis = 1)

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# `cumsum` 함수를 이용하면 각 원소들의 누적 합을 출력합니다. row와 columns의 구분은 없어지고, 순서대로 sum을 합니다. `axis`를 설정하면 같은 축끼리의 누적 합을 출력합니다. axis = 1 이므로 행끼리의 누적합이 출력되겠네요.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 4.누적합3(cumsum) 
# [문제 2]  
# two_dimension 배열에서 같은 row 끼리의 누적합을 출력해보세요.

# %%
two_dimension = np.array([[5,10],
                          [15,20]])

np.___(___, axis = ___)

# %%
#checkcode
ensure_vals(globals(),'two_dimension')
@check_safety
def check(user_answer=_):
    check1 = (user_answer == np.cumsum(two_dimension, axis = 0)).all()
    if check1:
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# `cumsum` 함수를 이용하면 각 원소들의 누적 합을 출력합니다. `axis`를 설정하면 같은 축끼리의 누적 합을 출력합니다. 

# %% [markdown]
# ### Hint.
# cumsum 함수와, axis = 0으로 하여 열끼리의 누적합을 구해보세요.

# %% [markdown]
# ### Solution.
# ```python
# np.cumsum(two_dimension, axis = 0)
# `````

# %% [markdown]
# # 5.지수함수1(exp)

# %%
np.exp(2)

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# exp 함수는 자연상수(e = 2.71828...)의 지수배에 대한 값을 계산해 줍니다. 파라미터에는 간단한 숫자뿐만 아니라 list 형태로도 삽입이 될 수 있습니다.
# 
# `np.exp(2)` -> e^2 라는 의미입니다.  

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 6.지수함수2(exp) 
# [문제 3]   
# e의 1,2,3,4의 거듭제곱을 리스트 형태로 넣고 출력해보세요.

# %%
np.___(___)



# %%
#checkcode
ensure_vals(globals())
@check_safety
def check(user_answer=_):
    check1 = (user_answer == np.exp([1,2,3,4])).all()
    if check1:
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# exp 함수는 자연상수(e = 2.71828...)의 지수배에 대한 값을 계산해 줍니다. 파라미터에는 간단한 숫자뿐만 아니라 list 형태로도 삽입이 될 수 있습니다.

# %% [markdown]
# ### Hint.
# exp 함수는 자연상수(e = 2.71828...)의 지수배에 대한 값을 계산해 줍니다. list의 형태는 `[1, 2, 3, 4]` 입니다.

# %% [markdown]
# ### Solution.
# ```python
# np.exp([1,2,3,4])
# ```

# %% [markdown]
# # 7.제곱근1(sqrt)

# %%
np.sqrt(4)

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# sqrt 함수는 제곱근을 계산해 줍니다. exp 함수와 마찬가지로 파라미터에는 간단한 숫자뿐만 아니라 list 형태로도 삽입이 될 수 있습니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 8.제곱근2(sqrt)
# 
# [문제 4]  
# 4,9,16의 제곱근을 리스트 형태로 넣고 출력해보세요.

# %%
np.___(___)

# %%
#checkcode
ensure_vals(globals())
@check_safety
def check(user_answer=_):
    check1 = (user_answer == np.sqrt([4,9,16])).all()
    if check1:
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# sqrt 함수는 제곱근을 계산해 줍니다. 파라미터에는 간단한 숫자뿐만 아니라 list 형태로도 삽입이 될 수 있습니다.

# %% [markdown]
# ### Hint.
# sqrt 함수는 제곱근을 계산해 줍니다. list의 형태는 `[4, 9, 16]` 입니다.

# %% [markdown]
# ### Solution.
# ```python
# np.sqrt([4,9,16])
# ```


