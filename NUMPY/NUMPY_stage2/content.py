# %%
#hiddencell
from pbl_tools import *

# %% [markdown]
# # 스테이지 2

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
# # 2.차원(dimension)의 이해

# %%
one_dimension = np.ones(3)
print("---1차원 벡터---\n",one_dimension)

two_dimension = np.zeros((2,3))
print("\n---2차원 행렬---\n",two_dimension)

three_dimension = np.ones((2,3,2))
print("\n---3차원 텐서---\n",three_dimension)

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 앞에서 numpy의 주요 객체는 **다차원 배열**이라고 설명을 했었는데요. 데이터는 숫자들의 배열로 이루어져 있기때문에 **숫자로 배열된 데이터를 처리**하는 것은 매우 중요한 과정입니다. 
# 
# 이번엔 **차원(Dimension)에** 대해서 배워봅시다. 차원을 쉽게 이해하기 위해 그림으로 표현해 보았습니다.
# 
# <img width="758" alt="image" src="https://user-images.githubusercontent.com/75363345/221068717-36293173-7cf5-444f-9a98-1785c13a1a0d.png">
# 
# 
# 
# - 1차원 array는 **벡터(vector)** 라고 부릅니다.
# - 2차원 array는 **행렬(matric)** 라고 부릅니다.
# - 3차원 array는 **텐서(tensor)** 라고 부릅니다.
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
# # 3.1차원 배열

# %%
one_array = np.array([1,2,3])
one_array

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 이번엔 axis(축)에 대해서 살펴보도록 하겠습니다.
# 
# <img width="773" alt="image" src="https://user-images.githubusercontent.com/75363345/221082390-69c21d15-358f-4809-bd35-5f8515607454.png">
# 
# 1차원 배열부터 살펴볼건데요! 그림에서와 같이 1차원 배열은 axis = 0 하나뿐입니다. 행과 열의 개념이 없죠. 그래서 위에 출력된 값을 보면 1부터 3까지 벡터로 나열된것을 확인할 수 있습니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 4.2차원 배열

# %%
np.array([[1,2,3],
          [4,5,6]])

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# <img width="282" alt="image" src="https://user-images.githubusercontent.com/75363345/221075468-6aac70f7-7aaf-4b58-a663-ad01fc64e43a.png">
# 
# 2차원 배열은 2차원이니 축이 2개 있습니다. axis = 0과 axis = 1이 존재하지요. 위의 결과는 **행과 열**이 존재하는 행렬이 출력되었네요. 행은 2개 열은 3개인 array 입니다.
# 
# 

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 5.3차원 배열

# %%
np.array([[[1,2],
           [3,4],
           [5,6]],
           [[7,8],
           [9,10],
           [11,12]]])

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# <img width="637" alt="image" src="https://user-images.githubusercontent.com/75363345/221083181-0c3544d3-a1ec-418e-8fa3-55a932207d2f.png">
# 
# 3차원 배열은 3차원이니 축이 3개 있습니다. axis = 0, axis = 1, axis = 2가 존재하지요. 위의 결과는 **깊이, 행, 열**이 존재하는 텐서가 출력되었네요. 깊이 2개 행 3개 열은 2개인 array 입니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 6.2차원 배열 복습
# 
# [문제 2]  
# 행이 2개, 열이 3개인 **0으로 채워진 행렬**을 만들어보세요.  
# 아래 빈칸을 채워주세요.

# %%
np.zeros((___))

# %%
#checkcode
ensure_vals(globals())
@check_safety
def check(user_answer=_):
    check0 = user_answer.shape == (2,3)
    check1 = 0 in user_answer
    
    if check0 and check1: 
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# `np.zeros`는 배열을 모두 0으로 채워주는 함수입니다. 형태는 `np.zeros(shape)` 입니다

# %% [markdown]
# ### Hint.
# np.zeros(행,열)

# %% [markdown]
# ### Solution.
# ```python
# np.zeros((2,3))
# ```

# %% [markdown]
# # 7.3차원 배열 복습
# 
# [문제 3]  
# 깊이 2개, 행이 3개, 열이 4개인 **1으로 채워진 텐서**을 만들어보세요.  
# 아래 빈칸을 채워주세요.

# %%
np.___((___))

# %%
#checkcode
ensure_vals(globals())
@check_safety
def check(user_answer=_):
    check0 = user_answer.shape == (2,3,4)
    check1 = 1 in user_answer
    
    if check0 and check1: 
        return True
    else:
        return False
check()

# %% [markdown]
# ### Inst.
# `np.ones`는 배열을 모두 0으로 채워주는 함수입니다. 형태는 `np.ones(shape)` 입니다

# %% [markdown]
# ### Hint.
# np.ones(깊이, 행, 열)

# %% [markdown]
# ### Solution.
# ```python
# np.ones((2,3,4))
# ```


