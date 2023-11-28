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

# # Stage 3

# # 1. import 및 데이터 불러오기 
# [문제 1]  
# 아래 빈칸을 채우고 데이터를 불러오세요. 그리고 피처 이름을 변경해 봅시다.

# +
___ ___ as pd

train = pd.___('train.csv')
test = pd.___('test.csv')
submission = pd.___('sample_submission.csv')

feature_names = {
    'sepal length (cm)': 'sepal_length',
    'petal length (cm)': 'petal_length',
    'sepal width (cm)': 'sepal_width',
    'petal width (cm)': 'petal_width'
}
train = train.rename(___=feature_names)
test = test.rename(___=feature_names)

print('train 데이터 개수: ', len(train))
print('test 데이터 개수: ', len(test))
print('submission 데이터 개수: ', len(submission))

# +
#checkcode
ensure_vals(globals(), 'train', 'test', 'submission')
@check_safety
def check(
    train=train,
    test=test,
    submission=submission,
):
    c_point1 = hasattr(train, 'sepal_length')
    c_point2 = hasattr(test, 'sepal_width')
    c_point3 = hasattr(submission, 'head')

    if c_point1 and c_point2 and c_point3:
        return True
    else:
        return False

check()
# -

# ### Inst.
# pandas 라이브러리는 `read_csv('파일명')` 함수를 이용해 CSV 파일을 불러올 수 있습니다. 

# ### Hint.
# 판다스(Pandas)는 `read_csv('파일명')`함수를 이용해 CSV 파일을 불러옵니다. 피처 이름을 변경할 때에는 `rename` 함수 안에 `columns`을 넣어줍니다.

# ### Solution.
#
# ```
# import pandas as pd  
#
# train = pd.read_csv('train.csv')  
# test = pd.read_csv('test.csv')  
# submission = pd.read_csv('sample_submission.csv')  
#
# feature_names = {  
#     'sepal length (cm)': 'sepal_length',  
#     'petal length (cm)': 'petal_length',  
#     'sepal width (cm)': 'sepal_width',  
#     'petal width (cm)': 'petal_width'  
# }  
# train = train.rename(columns=feature_names)  
# test = test.rename(columns=feature_names)  
#
# print('train 데이터 개수: ', len(train))  
# print('test 데이터 개수: ', len(test))  
# print('submission 데이터 개수: ', len(submission)) 
# ```

# # 2. 머신러닝 모델이란

train.head()

# +
#checkcode
#empty
# -

# ### Inst.
#
# 머신러닝 알고리즘은 데이터에서 패턴을 찾아내고 학습하는 알고리즘 입니다. 그리고 학습된 머신러닝은 예측을 실행합니다. 머신러닝은 크게 Supervised Learning, Unsupervised Learning 으로 나눌 수 있습니다. Supervised Learning은 머신러닝에게 정답지를 제공하는 형태의 학습 방법 입니다. 예를 들어 붓꽃의 품종을 예측하는 알고리즘을 학습 할 때, 꽃의 종류가 무엇인지 미리 알려주어 꽃의 종류마다 어떠한 특성을 가지고 있는지 학습하도록 합니다. 반면 항상 데이터에 정답이 존재하지는 않습니다. 정답지가 없는 경우에는 정답지 없이 머신러닝을 진행하는데 이러한 방법을 Unsupervised Learning 이라고 합니다.

# ### Hint.
# empty

# ### Solution.
# empty

# # 3. 클래스별 데이터 확인 (1)

train[train['species'] == 0].head(50)

# +
#checkcode
#empty
# -

# ### Inst.
#
# 종의 이름이 Setosa일 때의 데이터를 살펴 봅시다. head 명령어를 이용하면 쉽게 데이터를 확인 할 수 있습니다.

# ### Hint.
# empty

# ### Solution.
# empty

# # 4. 클래스별 데이터 확인 (2)
# [문제 2]  
# species가 1인 데이터를 조회해 봅시다. 인덱스 0부터 순서대로 50개 조회해 봅시다.

train[train['species'] ___ 1].___(___)


# +
#checkcode
def check(
    user_answer=_,
    length = 50,
    species = 1
):
    c_point1 = len(user_answer) <= length
    c_point2 = user_answer['species'].unique()[0] == species

    if c_point1 and c_point2:
        return True
    else:
        return False

check()
# -

# ### Inst.
#
# 종의 이름이 versicolor일 때의 데이터를 살펴 봅시다. head 명령어를 이용하면 쉽게 데이터를 확인 할 수 있습니다.

# ### Hint.
# Python에서 동등 비교를 할 때는 `==` 를 사용합니다.  
# 데이터프레임에서 앞에서부터 순서대로 확인할 때에는 `head()` 를 사용할 수 있습니다

# ### Solution.
# ```
# train[train['species'] == 1].head(50)
# ```

# # 5. 클래스별 데이터 확인 (3)
# [문제 3]  
# species가 2인 데이터를 조회해 봅시다. 인덱스 0부터 순서대로 50개 조회해 봅시다.

train[train['species'] ___ 2].___(___)


# +
#checkcode
def check(
    user_answer=_,
    length = 50,
    species = 2
):
    c_point1 = len(user_answer) <= length
    c_point2 = user_answer['species'].unique()[0] == species

    if c_point1 and c_point2:
        return True
    else:
        return False

check()


# -

# ### Inst.
#
# 종의 이름이 virginica일 때의 데이터를 살펴 봅시다. head 명령어를 이용하면 쉽게 데이터를 확인 할 수 있습니다.

# ### Hint.
# Python에서 동등 비교를 할 때는 `==` 를 사용합니다.  
# 데이터프레임에서 앞에서부터 순서대로 확인할 때에는 `head()` 를 사용할 수 있습니다

# ### Solution.
# ```
# train[train['species'] == 2].head(50)
# ```

# # 6. if문으로 분류기 만들어 보기

def model(row):
    if row['petal_width'] < 1:
        return 0
    elif row['petal_length'] < 5:
        return 1
    else:
        return 2


# +
#checkcode
#empty
# -

# ### Inst.
#
# 위 데이터를 살펴보고 각 종별로 특징을 살펴봅시다. 먼저 species가 0일 때에는 petal_width의 값이 다른 종에 비해 작은 것을 확인 할 수 있습니다. 이를 이용해 petal_width가 1보다 작으면 species를 0으로 예측 하겠습니다. 두번째로 species가 1이 2와 비교해서 petal_length가 작은 것을 확인 할 수 있습니다. 이를 이용해 petal_width가 5보다 작으면 species를 1로 예측 하겠습니다.

# ### Hint.
# empty

# ### Solution.
# empty

# # 7. Test 데이터 예측해보기

test['species'] = test.apply(model, axis=1)
test.head(10)

# +
#checkcode
#empty
# -

# ### Inst.
#
# `apply()` 함수를 이용하면 데이터프레임을 앞에서 정의한 함수를 적용해 줄 수 있습니다.

# ### Hint.
# empty

# ### Solution.
# empty

# # 8. Submission파일에 예측값 넣기
# [문제 4]  
# 앞에서 예측한 값을 submission의 species피처에 넣어 봅시다.

submission['species'] = ___['___'].to_list()
submission.head(10)

# +
#checkcode
ensure_vals(globals(), 'submission', 'test')
@check_safety
def check(
    user_answer=submission,
    test=test
):
    c_point1 = user_answer['species'].sum() == test['species'].sum()

    if c_point1:
        return True
    else:
        return False

check()
# -

# ### Inst.
#
# `to_list()` 함수를 이용하면 데이터프레임을 앞에서 정의한 함수를 적용해 줄 수 있습니다.

# ### Hint.
# `submission['species']`에 `test['species']`데이터를 넣어 봅시다.

# ### Solution.
# ```
# submission['species'] = test['species'].to_list()  
# submission.head(10)
# ```

# # 8. CSV 파일 저장하기
# [문제 4]  
# 앞에서 예측한 값을 submission의 species피처에 넣어 봅시다.

submission.___('submission.csv', index=False)

# +
#checkcode
ensure_vals(globals(), 'test')
@check_safety
def check(test=test):
    user_answer = pd.read_csv('submission.csv')
    c_point1 = len(user_answer) == len(test)

    if c_point1:
        return True
    else:
        return False

check()
# -


# ### Inst.
# empty

# ### Hint.
# `to_list()` 함수를 이용하면 데이터프레임을 앞에서 정의한 함수를 적용해 줄 수 있습니다.

# ### Solution.
# ```
# submission.to_csv('submission.csv', index=False)
# ```
