# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#hiddencell

from pbl_tools import *
# -

# # Stage 1
#
# # 0. Intro
# ![iris_inner (1)](https://user-images.githubusercontent.com/39521155/221115190-e4adf0a9-4aa8-42c7-9dac-068f0ea9a618.png)
#
# ## 0.1. 소개
# 꽃과 머신러닝. 언뜻 생각하기엔 생뚱맞은 조합이죠?  
# 포근한 향이 특징인 붓꽃은 꽃받침과 꽃잎의 길이, 너비로 그 품종을 예측해 볼 수 있어 데이터 분석을 공부할 때 매우 널리 쓰이는 예제 중 하나입니다.  
#
# 지금까진 그저 붓꽃을 보며 ‘예쁘다’고만 생각하셨나요?  
# 이번 프로젝트를 통해 눈으로 볼 땐 보이지 않는 차이를 데이터로 느껴 보세요!
#
# ## 0.2. 프로젝트의 목적
#
# 본 프로젝트에서는 의사 결정 나무(Decision Tree)를 이용해 간단한 예측을 진행합니다.  
# 데이터 분석이 익숙하지 않더라도 차근차근 모델을 만들고 데이터를 학습시키면서 대회 과정을 경험해 보세요!

# # 1. Pandas import
#
# [문제 1]  
# 판다스 라이브러리를 불러와 봅시다.

import pandas as pd

# +
#checkcode
ensure_vals(globals(), 'pd')
@check_safety
def check(user_answer = pd):
    c_point1 = hasattr(pd, 'DataFrame')

    if c_point1:
        return True
    else:
        return False

check()
# -

# ### Inst.
#
# 라이브러리를 불러오는 코드를 복습해 봅시다.  
# 파이썬에서는 `import <라이브러리 이름>` 명령어을 사용해 필요한 라이브러리를 불러옵니다.
# `import pandas as pd`에서 as 를 사용한 이유는 자주 사용하는 명령어를 조금 더 쉽게 사용할 수 있도록 라이브러리를 할당하는 역할을 합니다.
# import pandas로 라이브러리를 불러온다면 pandas.함수명을 사용하야하는데, 해당 라이브러리를 여러 번 사용해야한다면 오랜 시간이 소요될 수 있습니다.
# 반면, as를 사용했다면 pd.함수명으로도 사용할 수 있기 때문에 편리하게 라이브러리를 활용할 수 있습니다.

# ### Hint.
# import 명령어를 사용하여 라이브러리를 불러올 수 있습니다.

# + [markdown] jp-MarkdownHeadingCollapsed=true tags=[]
# ### Solution.
# ```
# import pandas as pd
# ```
# -

# # 2. 학습(Train) 데이터 불러오기

train = pd.read_csv('train.csv')
print('데이터 개수: ', len(train))

# +
#checkcode
#empty
# -

# ### Inst.
#
# `read_csv()` 함수는 (‘파일이 있는 위치/파일명.csv‘)의 형식을 받아 데이터프레임(DataFrame) 형태로 데이터를 불러옵니다. 여기서 데이터프레임이란 데이터를 행과 열이 존재하는 2차원 테이블 입니다. read_csv뒤에는 괄호가 있는데, 해당 부분에는 '인자'를 넣을 수 있습니다.
# 해당 경우에는 train.csv라는 인자를 넣어서 파일을 불러온 경우입니다.

# ### Hint.
# empty

# + [markdown] tags=[]
# ### Solution.
# empty
# -

# # 3. 테스트(Test) 및 정답지 불러오기

# +
test = pd.read_csv('test.csv')
submission = pd.read_csv('sample_submission.csv')

print('test 데이터 개수: ', len(test))
print('submission 데이터 개수: ', len(submission))

# +
#checkcode
#empty
# -

# ### Inst.
# 판다스를 활용하여 test.csv 파일과 sample_submission.csv 파일을 불러와주세요.

# ### Hint.
# empty

# + [markdown] tags=[]
# ### Solution.
# empty
# -

# # 4. Submission 데이터 확인하기
# [문제 1]  
# 아래 빈칸을 채워 데이터프레임 submission의 값의 앞부분 10개를 확인해 봅시다.

submission.___(___)


# +
#checkcode
def check(
    user_answer = _,
    num=10
):
    c_point1 = len(user_answer) == num

    if c_point1:
        return True
    else:
        return False

check()
# -

# ### Inst.
#
# `head` 함수를 사용하여 submission의 데이터를 확인해주세요.  
# head에 인자를 아무것도 입력하지 않을 경우 상위 5개의 값만 출력이 됩니다.    

# ### Hint.
# `head()`함수에서 확인하고 싶은 갯수를 10개로 변경하고 싶다면 괄호 안에 10을 입력해보세요! 

# + [markdown] tags=[]
# ### Solution.
# ```
# submission.head(10)
# ```
# -

# # 5. CSV 파일 저장하기

submission.to_csv('submission.csv', index=False)

# +
#checkcode
#empty
# -

# ### Inst.
#
# to_csv 함수를 활용하여 파일을 저장해봅시다.
# `to_csv('파일명')` 으로 저장할 수 있어요.
# to_csv 함수 안에 `index = False` 라고 적혀있는데, 행의 인덱스를 사용하지 않기 위해서 위와 같이 지정합니다.
# 만약 index의 값을 True로 할당한다면 제출이되지 않을 수도 있으니 반드시 index = False 로 설정해주세요.  

# ### Hint.
# empty

# + [markdown] tags=[]
# ### Solution.
# empty
