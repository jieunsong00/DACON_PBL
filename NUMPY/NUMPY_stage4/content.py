# %%
#hiddencell
from pbl_tools import *

# %% [markdown]
# # 스테이지 4

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
# # 2.1차원 배열 생성

# %%
jump_num = np.array([1,2,3,4])
same_num = np.array([2,2,2,2])

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 이번 스테이지에서는 연산에 대해 배워보기 위해 2개의 array를 생성했습니다.
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
# # 3.배열의 덧셈(+)

# %%
jump_num + same_num

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# >- jump_num = np.array([1,2,3,4]) 
# >- same_num = np.array([2,2,2,2]) 
# 
# 위에서 생성한 `jump_num` 과 `same_num` 배열을 더해보겠습니다. jump_num + same_num 와 같이 **배열의 덧셈은 각 요소의 덧셈**을 갖는 array를 만듭니다. 1+2, 2+2, 3+2, 4+2 이므로 결과는 3, 4, 5, 6 이겠네요.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 4.배열의 뺄셈(-)

# %%
jump_num - same_num

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# >- jump_num = np.array([1,2,3,4]) 
# >- same_num = np.array([2,2,2,2]) 
# 
# `jump_num` 에서 `same_num` 배열을 빼보겠습니다. jump_num - same_num 와 같이 **배열의 뺄셈은 각 요소의 뺄셈**을 갖는 array를 만듭니다. 1-2, 2-2, 3-2, 4-2 이므로 결과는 -1, 0, 1, 2 이겠네요.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 5.배열의 곱셈(*)

# %%
jump_num * same_num

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# >- jump_num = np.array([1,2,3,4]) 
# >- same_num = np.array([2,2,2,2]) 
# 
# 위에서 생성한 `jump_num` 과 `same_num` 배열을 곱해보겠습니다. jump_num * same_num 와 같이 **배열의 곱셈은 각 요소의 곱셈**을 갖는 array를 만듭니다. 1x2, 2x2, 3x2, 4x2 이므로 결과는 2, 4, 6, 8 이겠네요.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 6.배열의 거듭제곱(**)

# %%
jump_num ** same_num

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# >- jump_num = np.array([1,2,3,4]) 
# >- same_num = np.array([2,2,2,2]) 
# 
# 위에서 생성한 `jump_num` 에 `same_num` 배열을 거듭제곱 해보겠습니다. jump_num ** same_num 와 같이 **배열의 거듭제곱은 각 요소의 거듭제곱**을 갖는 array를 만듭니다. 1^2, 2^2, 3^2, 4^2 이므로 결과는 1, 4, 9, 16 이겠네요.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 7.배열의 나눗셈(/)

# %%
jump_num / same_num

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# >- jump_num = np.array([1,2,3,4]) 
# >- same_num = np.array([2,2,2,2]) 
# 
# 위에서 생성한 `jump_num` 에 `same_num` 배열을 나누어 보겠습니다. jump_num / same_num 와 같이 **배열의 나눗셈은 각 요소의 나눗셈**을 갖는 array를 만듭니다. 1/2, 2/2, 3/2, 4/2 이므로 결과는 0.5, 1, 1.5, 2 입니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 8.배열의 조건문(<)
# 

# %%
random_num = np.array([2,5,4,6]) 
same_three_num = np.array([3,3,3,3]) 

random_num < same_three_num 

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# 위에서 생성한 `random_num` , `same_three_num` 배열에 조건문을 걸어보겠습니다. 2<3, 5>3, 4>3, 6>3 이므로 결과는 True, False, False, False 입니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 9.2차원 배열 생성

# %%
two_jump_num = np.array([[4,6],
                         [12,10]])
two_same_num = np.array([[2,2],
                         [2,2]])

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 지금까지 배운 배열의 연산을 실습해보기 위해 2개의 2차원 array를 생성했습니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 10.배열 연산의 실습(1)
# 
# [문제 2]  
# 위에서 생성한 two_jump_num 과 two_same_num을 곱한 후 two_jump_num을 더해보세요.

# %%


# %%
#checkcode
ensure_vals(globals(),'two_jump_num','two_same_num')
@check_safety
def check(user_answer=_):
    if (user_answer==two_jump_num * two_same_num + two_jump_num).all():
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# 
# 위에서 배운 연산기호를 이용해 보세요. `(+,-,/,*,**)`

# %% [markdown]
# ### Hint.
# 곱셈(*), 덧셈(+)

# %% [markdown]
# ### Solution.
# ```python
# two_jump_num * two_same_num + two_jump_num
# ```

# %% [markdown]
# # 11.배열 연산의 실습(2)
# 
# [문제 3]  
# 위에서 생성한 two_jump_num와 two_same_num 을 나눈 후 two_jump_num을 곱해보세요.

# %%


# %%
#checkcode
ensure_vals(globals(),'two_jump_num','two_same_num')
@check_safety
def check(user_answer=_):
    if (user_answer==two_jump_num / two_same_num * two_jump_num).all():
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# 
# 위에서 배운 연산기호를 이용해 보세요. (+,-,/,*,**)

# %% [markdown]
# ### Hint.
# 나눗셈(/), 곱셈(*)

# %% [markdown]
# ### Solution.
# ```python
# two_jump_num / two_same_num * two_jump_num
# ```

# %% [markdown]
# # 12.배열 연산의 실습(3)
# 
# [문제 4]  
# `>` 왼쪽에는 two_same_num에 two_jump_num을 거듭제곱한 값을, `>` 오른쪽에는 two_jump_num 과 two_same_num을 곱한 값을 채워주세요.  
# 아래의 빈칸을 채워주세요.

# %%
___ > ___

# %%
#checkcode
ensure_vals(globals(),'two_same_num','two_jump_num')
@check_safety
def check(user_answer=_):
    if (sum(_) == ([2, 2])).all():
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# 위에서 배운 연산기호를 이용해 보세요. `(+,-,/,*,**)`

# %% [markdown]
# ### Hint.
# 거듭제곱(**), 곱셈(*)

# %% [markdown]
# ### Solution.
# ```python
# two_same_num ** two_jump_num > two_jump_num * two_same_num 
# ```


