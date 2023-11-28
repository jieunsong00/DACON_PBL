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

# # Stage 4

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
# CSV 파일을 불러오기 위해서 `read_csv('파일명')` 함수를 사용해 보세요. 피처 이름을 변경하기 위해서는 `rename()`함수에 `columns`을 넣어주어야 합니다.

# ### Solution.
#
# import pandas as pd  
#
# train = pd.read_csv('train.csv')  
# test = pd.read_csv('test.csv')  
# submission = pd.read_csv('sample_submission.csv')  
#
# feature_names = {  
# &nbsp;&nbsp;&nbsp;&nbsp;'sepal length (cm)': 'sepal_length',  
# &nbsp;&nbsp;&nbsp;&nbsp;'petal length (cm)': 'petal_length',  
# &nbsp;&nbsp;&nbsp;&nbsp;'sepal width (cm)': 'sepal_width',  
# &nbsp;&nbsp;&nbsp;&nbsp;'petal width (cm)': 'petal_width'  
# }  
# train = train.rename(columns=feature_names)  
# test = test.rename(columns=feature_names)  
#
# print('train 데이터 개수: ', len(train))  
# print('test 데이터 개수: ', len(test))  
# print('submission 데이터 개수: ', len(submission))  

# # 2. Decision Tree 설명

from sklearn.tree import DecisionTreeClassifier

# +
#checkcode
#empty
# -

# ### Inst.
# 사이킷런(Scikit-learn)은 Python에서 사용 할 수 있는 머신러닝 라이브러리 입니다. 오픈소스 라이브러리로 분류분석(Classification analysis), 회귀분석(Regression analysis), 군집분석(Clustering analysis) 등의 다양한 모델을 사용할 수 있습니다. 그 외에도 여러 데이터 전처리 기능을 지원하고 있으며, 하이퍼 파라미터를 세팅하는 등 여러 편의 기능도 제공하고 있습니다. `import sklearn`를 입력하여 라이브러리를 불러 올 수 있습니다.  
#
# 의사결정나무(Decision Tree)는 사이킷런에서 제공하고 있는 라이브러리입니다. 의사결정나무는 지도학습(Supervised Learning) 모델이며, 분류/회귀 문제에서 사용할 수 있습니다. 해당 모델은 학습에 사용한 피처(Feature)를 이용해 분류 기준을 만듭니다. 특정 피처를 기준으로 분류한 이후, 분류한 데이터를 또다시 다른 피처를 기준으로 분류해 나갑니다. 그리고 마지막에는 분류된 그룹에 대해 예측값을 부여합니다.
#
# 의사결정나무를 그림으로 그리면 아래 그림과 같습니다.
#
# ![스크린샷 2023-02-22 오후 5 58 59](https://user-images.githubusercontent.com/39521155/220571524-a0636aaa-419a-45ef-a4d1-bd5bee5414a8.png)

# ### Hint.
# empty

# ### Solution.
# empty

# # 3. 모델 정의

model = DecisionTreeClassifier(max_depth=2, random_state=32)

# +
#checkcode
#empty
# -

# ### Inst.
#
# `max_depth`를 2로 설정하면 트리의 최대 깊이가 2로 제한됩니다.

# ### Hint.
# empty

# ### Solution.
# empty

# # 4. 학습할 데이터 정리

feature_names = ['petal_width', 'petal_length']
train_x = train[feature_names]
train_y = train['species']

# +
#checkcode
#empty
# -

# ### Inst.
#
# 데이터프레임에 피처 이름으로 구성된 리스트(list)를 넣어주면, 해당되는 피처로만 구성할 수 있습니다. 이를 이용해 독립변수(X), 종속변수(Y)를 정의해 봅시다. 스테이지3에서 사용하였던 변수를 그대로 사용해 볼까요!

# ### Hint.
# empty

# ### Solution.
# empty

# # 5. 모델 학습

model.fit(train_x, train_y)

# +
#checkcode
#empty
# -

# ### Inst.
# Scikit-learn은 모델을 학습할 때 `fit()`함수를 이용합니다. 모델을 학습해 봅시다.

# ### Hint.
# empty

# ### Solution.
# empty

# # 6. Tree 시각화 (1)

# +
import matplotlib.pyplot as plt
from sklearn import tree

plt.figure(figsize=(20,15))
tree.plot_tree(model, 
    class_names=['setosa', 'versicolor', 'virginica'],
    feature_names=feature_names,
    filled=True,
)
plt.show()

# +
#checkcode
#empty
# -

# ### Inst.
#
# tree 모듈을 이용하면 학습한 모델이 어떻게 구성되어 있는지 그림으로 볼 수 있습니다.

# ### Hint.
# empty

# ### Solution.
# empty

# # 7. 다른 데이터도 사용
# [문제 2]  
# petal_width, petal_length, petal_length, petal_width 를 다양하게 사용해서 모델을 학습해 봅시다. 그리고 `max_depth`를 변경하여 모델이 어떻게 바뀌는지 확인해 봅시다.

# +
model = DecisionTreeClassifier(max_depth=___, random_state=32)

feature_names = [___, ___, ___, ___]
train_x = train[feature_names]
train_y = train['species']

model.fit(train_x, train_y)

plt.figure(figsize=(20,15))
tree.plot_tree(model, 
    class_names=['setosa', 'versicolor', 'virginica'],
    feature_names=feature_names,
    impurity=True, filled=True,
    rounded=True
)
plt.show()

# +
#checkcode
#empty
# -

# ### Inst.
#
# `feature_names` 변수에 원하는 피처를 넣어 봅시다. 그리고 `max_depth`를 변경하여 트리의 구조를 변경해 봅시다.

# ### Hint.
# empty

# ### Solution.
#
# ```
# model = DecisionTreeClassifier(max_depth=5, random_state=32)
#
# feature_names = ['petal_width', 'petal_length', 'petal_length', 'petal_width']
# train_x = train[feature_names]
# train_y = train['species']
#
# model.fit(train_x, train_y)
#
# import matplotlib.pyplot as plt
# from sklearn import tree
#
# plt.figure(figsize=(20,15))
# tree.plot_tree(model, 
#     class_names=['setosa', 'versicolor', 'virginica'],
#     feature_names=feature_names,
#     filled=True,
# )
# plt.show()
# ```
