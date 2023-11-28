# %%
#hiddencell
from pbl_tools import *

# %% [markdown]
# # 스테이지 5

# %% [markdown]
# # 1.라이브러리 import
# [문제 1]  
# numpy 라이브러리를 불러와 주세요. 단, numpy는 자주 사용하는 라이브러리이므로 축약어인 np로 불러와주세요.  
# 아래 빈칸을 채워주세요.

# %%
___ numpy ___ np

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
twelve_array = np.array([[3,4,5,4],
                         [1,5,6,7],
                         [9,2,6,4]])

twelve_array

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 2차원 행렬(3행 X 4열) 데이터를 만들었습니다.
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
# # 3.최댓값(max)

# %%
np.max(twelve_array)

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# `max` 함수는 최댓값을 출력하는 함수입니다. `axis`를 기본값으로 실행하면 twelve_array 데이터의 모든 요소에서의 최댓값을 출력합니다.
# 가장 큰 값 9가 출력되겠네요.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 4.최솟값(min)
# 
# [문제 2]  
# twelve_array 모든 요소에서의 최솟값을 출력해 보세요.  
# 아래 빈칸을 채워보세요.

# %%
np.___(twelve_array)

# %%
#checkcode
ensure_vals(globals(),'twelve_array')
@check_safety
def check(user_answer=_):
    if (user_answer==np.min(twelve_array)):
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# `min` 함수는 최솟값을 출력하는 함수입니다. `axis`를 기본값으로 실행하면 twelve_array 데이터의 모든 요소에서의 최솟값을 출력합니다.
# 

# %% [markdown]
# ### Hint.
# np.min

# %% [markdown]
# ### Solution.
# ```python
# np.min(twelve_array)
# ```

# %% [markdown]
# # 5.최댓값(max)

# %%
np.max(twelve_array, axis = 0)

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# <img width="282" alt="image" src="https://user-images.githubusercontent.com/75363345/
# 221075468-6aac70f7-7aaf-4b58-a663-ad01fc64e43a.png">
# 
# stage2에서 axis(축)에 대해서 배웠습니다. 기억이 나시나요? 최댓값을 구해볼 twelve_array 배열은 2차원 배열입니다. 축이 2개 있겠네요. axis = 0과 axis = 1이 존재하지요. axis를 지정하면 지정한 축의 최댓값이 출력됩니다. 우리는 axis = 0 인 **각 열의 최댓값**을 구해봅시다.
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
# # 6.최솟값(min)
# 
# [문제 3]  
# twelve_array 에서 각 행의 최솟값을 구해보세요.  
# 아래 빈칸을 채워보세요.

# %%
np.___(twelve_array, axis = ___)

# %%
#checkcode
ensure_vals(globals(),'twelve_array')
@check_safety
def check(user_answer=_):
    check1 = 3 in _
    check2 = 1 in _
    check3 = 2 in _
    if check1 and check2 and check3:
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# `min` 함수를 사용하면 배열의 최솟값이 출력됩니다. `axis`를 지정하면 지정한 축의 최솟값을 구할 수 있습니다.
# 

# %% [markdown]
# ### Hint.
# min, axis = 1 함수를 사용하면 행의 최솟값을 구할 수 있습니다.

# %% [markdown]
# ### Solution.
# ```python
# np.min(twelve_array, axis = 1)
# ```

# %% [markdown]
# # 7.합계(sum)

# %%
np.sum(twelve_array)

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# `axis`를 기본값으로 실행하면 twelve_array 데이터의 모든 요소의 합을 출력합니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 8.합계(sum)
# [문제 4]  
# twelve_array 에서 각 행의 합계를 구해보세요.  
# 아래 빈칸을 채워보세요.

# %%
np.___(___, axis = ___)

# %%
#checkcode
ensure_vals(globals(),'twelve_array')
@check_safety
def check(user_answer=_):
    if (user_answer==np.sum(twelve_array, axis =1)).all():
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# `axis`를 1로 실행하면 twelve_array 행의 합을 출력합니다.

# %% [markdown]
# ### Hint.
# `sum, axis = 1` 함수를 사용하면 행의 합을 구할 수 있습니다.

# %% [markdown]
# ### Solution.
# ```python
# np.sum(twelve_array, axis = 1)
# ```


