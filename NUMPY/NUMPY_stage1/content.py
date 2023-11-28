# %%
#hiddencell
from pbl_tools import *

# %% [markdown]
# # 스테이지 1
# # 0.개요
# 
# ![numpy_inner](https://user-images.githubusercontent.com/75363345/222646563-c2399890-a7c1-49ed-9a1a-94a403524826.png)
# 
# 
# ## 0.1.소개
# 
# 단순한 문법과 폭 넓은 호환성으로 널리 사용되고 있는 파이썬!  
# 그러나 대규모 수치 연산을 할 땐 느려진다는 치명적인 단점이 있는데요.
# 
# 이를 보완하기 위해 만들어진 파이썬 라이브러리가 바로 Numerical Python, 줄여서 넘파이(Numpy)입니다.
# 
# C 언어로 구현되어 있는 넘파이는 연산 속도가 빠르며, 다양한 함수와 배열 연산 기능을 제공합니다.  
# 이러한 넘파이를 속속들이 이해하고 다룰 수 있다면, 데이터 분석에도 큰 도움이 되겠죠?
# 
# 넘파이 완전 정복을 위한 넘파이 첫걸음 프로젝트, 지금 시작합니다!
# 
# ## 0.2.프로젝트의 목적
# 
# 이번 프로젝트를 통해 우리는 넘파이의 기초적인 개념과 더불어 함수를 이해하고, 데이터의 차원에 관해 학습할 것입니다. 이를 토대로 간단한 연산을 실습하며 개념을 차근차근 다져 보겠습니다!

# %% [markdown]
# # 1.numpy의 이해

# %%
import numpy 

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# Numpy란 무엇일까요? Numpy는 파이썬에서 사용되는 과학 계산용 라이브러리입니다. 이 라이브러리는 **대규모 다차원 행렬**과 **행렬 연산**에 필요한 여러 유용한 기능을 제공합니다. 또한, 데이터분석, 머신러닝, 딥러닝 등 다양한 분야에서 사용되고 있습니다.
# 
# 먼저 numpy 라이브러리를 불러오도록 하겠습니다.  파이썬에서는 `import <라이브러리 이름>` 명령어을 사용해 필요한 라이브러리를 불러옵니다.

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 2.라이브러리 import
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
# 

# %% [markdown]
# ### Hint.
# np는 numpy의 약칭입니다. import 와 as를 이용해서 numpy 라이브러리를 불러와주세요.

# %% [markdown]
# ### Solution.
# ```python
# import numpy as np
# ```

# %% [markdown]
# # 3.np.zeros()

# %%
np.zeros(3)

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# array 배열을 만드는 방법에는 여러가지가 있습니다. 먼저 numpy에서 제공해주는 `np.zeros`를 이용해 보겠습니다. `np.zeros`는 배열을 **모두 0으로 채워주는 함수**입니다. 
# 형태는 `np.zeros(shape)`  입니다. shape에는 몇 차원을 출력할건지를 적어주면 됩니다. 위의 결과를 보면 세 개의 0을 요소로 가지는 1차원 array가 생성된 것을 확인할 수 있습니다. 
# 
# 참고로, 차원에 대한 자세한 내용은 뒤에서 배울 예정입니다!
# 

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty

# %% [markdown]
# # 4.np.ones()

# %%
np.ones(2)

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# `np.ones`는 배열을 모두 1로 채워주는 함수입니다. 형태는 `np.ones(shape)` 입니다. `np.zeros`와 비슷하죠? 위의 결과를 보면 두 개의 1을 요소로 가지는 1차원 array가 생성된 것을 확인할 수 있습니다. 

# %% [markdown]
# ### Hint.
# empty

# %% [markdown]
# ### Solution.
# empty


