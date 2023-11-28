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

# # Stage 6

# # 1. import 및 데이터 불러오기 
# [문제 1]  
# 아래 빈칸을 채우고 데이터를 불러오세요. 그리고 피처 이름을 변경하고 종속변수와 독립변수로 데이터를 분리하십시오.

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

feature_names = ['petal_width', 'petal_length', 'petal_length', 'petal_width']
train_x = train[___]
train_y = train['species']

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
# pandas 라이브러리는 `read_csv('파일명')` 함수를 이용해 CSV 파일을 불러올 수 있어요.

# ### Hint.
# CSV 파일을 불러오기 위해서 `read_csv('파일명')` 함수를 사용해 보세요. 피처 이름을 변경하기 위해서는 `rename()`함수에 `columns`을 넣어주어야 합니다.

# ### Solution.
#
# ```python
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
#
# feature_names = ['petal_width', 'petal_length', 'petal_length', 'petal_width']
# train_x = train[feature_names]
# train_y = train['species']
# ```

# # 2. Decision Tree 모델 학습
# [문제 2]  
# 아래 빈칸을 채워 Decision Tree 모델을 학습해 봅시다.

# +
from sklearn.tree import ___

model = ___(max_depth=5, random_state=32)
model.___(train_x, train_y)

# +
#checkcode
ensure_vals(globals(), 'model')
@check_safety
def check(
    user_answer=model
):
    c_point1 = hasattr(user_answer, 'fit')

    if c_point1:
        return True
    else:
        return False

check()
# -

# ### Inst.
# empty

# ### Hint.
# `DecisionTreeClassifier`는 분류 문제에 사용되는 Decision Tree입니다. 모델을 학습할 때에는 `fit()`함수를 사용하십시오.

# ### Solution.
#
# ```python
# from sklearn.tree import DecisionTreeClassifier
#
# model = DecisionTreeClassifier(max_depth=5, random_state=32)
# model.fit(train_x, train_y)
# ```

# # 3. 예측
# [문제 3]  
# 빈칸을 채워 예측에 필요한 피처만 사용하도록 데이터를 만들어 주세요.

# +
feature_names = ['petal_width', 'petal_length', 'petal_length', 'petal_width']
test_x = test[___]

pred = model.predict(___)
pred

# +
#checkcode
ensure_vals(globals(), 'pred')
@check_safety
def check(user_answer=pred):
    c_point1 = pred is not None

    if c_point1:
        return True
    else:
        return False

check()
# -

# ### Inst.
# `predict`함수를 이용해 예측을 할 수 있습니다.

# ### Hint.
# 데이터프레임은 `[]` 안에 리스트를 넣어 피처를 선택할 수 있습니다. 모델 예측 시 `test_x`를 사용하세요.

# ### Solution.
#
# ```python
# feature_names = ['petal_width', 'petal_length', 'petal_length', 'petal_width']
# test_x = test[feature_names]
#
# pred = model.predict(test_x)
# pred
# ```

# # 4. submission 정답 변경하기

submission['species'] = pred
submission.head(10)

# +
#checkcode
#empty
# -

# ### Inst.
#
# submission은 정답지 입니다. 예측한 데이터로 값을 변경해 보세요.

# ### Hint.
# empty

# ### Solution.
# empty

# # 5. CSV 파일 저장하기
# [문제 4]  
# 아래 빈칸을 채우고 제출파일을 만들어 봅시다.

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
#
# to_csv 함수를 활용하여 파일을 저장해봅시다.
# `to_csv('파일명')` 으로 저장할 수 있어요.
# to_csv 함수 안에 `index = False` 라고 적혀있는데, 행의 인덱스를 사용하지 않기 위해서 위와 같이 지정합니다.
# 만약 index의 값을 True로 할당한다면 제출이되지 않을 수도 있으니 반드시 index = False 로 설정해주세요.  

# ### Hint.
#
# 데이터프레임은 `to_csv('파일명')`함수를 이용해 CSV로 저장할 수 있어요.

# ### Solution.
#
# ```python
# submission.to_csv('submission.csv', index=False)
# ```
