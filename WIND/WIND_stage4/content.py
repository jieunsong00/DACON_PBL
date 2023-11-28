# %%
#hiddencell
%pip install seaborn 

import pandas as pd 
from pbl_tools import *
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
plt.style.use("ggplot")

fe = fm.FontEntry(fname = 'NotoSansKR-Regular.otf', name = 'NotoSansKR')
fm.fontManager.ttflist.insert(0, fe)
plt.rc('font', family='NotoSansKR')

# %% [markdown]
# # 스테이지 4. EDA(2)
# - Feature 간 관계 이해
# - Target 와 Feature 간 관계 이해

# %% [markdown]
# # 1. 데이터 불러오기

# %%
import pandas as pd  

train = pd.read_csv('train.csv') 

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# empty
# 

# %% [markdown]
# ### Hint.
# 
# empty  

# %% [markdown]
# ### Solution.
# 
# empty

# %% [markdown]
# # 2. 독립변수별 분포 확인

# %%
plt.style.use("ggplot")

lm_features = ['temperature', 'pressure', 'humidity', 'wind_speed',
       'wind_direction', 'precipitation', 'cloudiness']

plt.figure(figsize=(30,15))
plt.suptitle("독립변수별 분포 확인", fontsize = 30)

for i in range(len(lm_features)):
  plt.subplot(2,7,i+1)
  plt.title(lm_features[i], fontsize = 20)
  plt.boxplot(train[lm_features[i]])
plt.show()

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# train 데이터셋에는 `Id` 피처와 `target` 피처를 제외한 독립변수가 총 8개 존재합니다. 앞선 스테이지에서 언급한 바와 같이, boxplot은 사분위값을 이용해서 데이터의 분포를 확인할 수 있는데요. boxplot을 이용하여 카테고리형 변수인 snowing을 제외한 **7개 독립변수들의 분포를 확인**해 보겠습니다. 
# 

# %% [markdown]
# ### Hint.
# 
# empty  

# %% [markdown]
# ### Solution.
# 
# empty

# %% [markdown]
# # 3. target X temperature

# %%
import seaborn as sns

fig, ax = plt.subplots(figsize = (10,5))
sns.scatterplot(x = train['temperature'], y = train['target'])

plt.show()

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 이번엔 우리가 예측해야 할 `target` 변수와 피처인 `temperature` 간에 어떠한 관계가 있는지 seaborn 라이브러리의 scatterplot(산점도)을 통해 확인해 보려 합니다.
# 출력된 결과를 보니 특별한 규칙이 있어 보이진 않습니다. 이로써 **온도(temperature)는 풍력 발전량(target)에 큰 영향을 미치지 않는다**는 사실을 알 수 있겠네요.
# 

# %% [markdown]
# ### Hint.
# 
# empty  

# %% [markdown]
# ### Solution.
# 
# empty

# %% [markdown]
# # 4. target X pressure
# [문제 1]  
# seaborn의 scatterplot을 이용하여 train 데이터셋의 pressure 피처와 target 피처의 관계를 시각화해 보세요.

# %%
fig, ax = plt.subplots(figsize = (10,5))

x_pressure = ___
y_target = ___

sns.scatterplot(x = x_pressure, y = y_target)

plt.show()

# %%
#checkcode
ensure_vals(globals(),'x_pressure','y_target')
@check_safety
def check(user_answer_x=x_pressure, user_answer_y=y_target, number = 100):

    c_point0 = sum(user_answer_x == train['pressure']) == number
    c_point1 = sum(user_answer_y == train['target']) == number

    if c_point0 and c_point1:
        return True
    else:
        return False

check()

# %% [markdown]
# ### Inst.
# x_pressure 변수에는 train 데이터셋의 `pressure` 피처를, y_target 변수에는 train 데이터셋의 `target` 피처를 할당해 주세요. 
# 
# 출력된 결과를 보니 pressure 값은 대체로 **1010과 1020 사이에 모여** 있다는 것을 알 수 있습니다. 그밖에 pressure과 target 간에 특별한 규칙이 있어 보이진 않네요.
# 
# 

# %% [markdown]
# ### Hint.
# 
# 형태는 `데이터셋['피처명']` 입니다.

# %% [markdown]
# ### Solution.
# ```python
# fig, ax = plt.subplots(figsize = (10,5))
# 
# x_pressure = train['pressure']
# y_target = train['target']
# 
# sns.scatterplot(x = x_pressure, y = y_target)
# 
# plt.show()
# ```

# %% [markdown]
# # 5. target X wind_speed

# %%
fig, ax = plt.subplots(figsize = (10,5))
sns.regplot(x = train['wind_speed'], y = train['target'])

plt.show()

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# 우리가 예측해야 할 `target` 변수와 피처인 `wind_speed` 간에 어떠한 관계가 있는지 seaborn 라이브러리의 regplot(추세선) 을 통해 확인해 보겠습니다. 출력된 결과에서 우상향하는 모양을 확인할 수 있네요! 즉, **풍력 발전량과 풍속은 양의 상관관계**라고 할 수 있습니다.
# 

# %% [markdown]
# ### Hint.
# 
# empty  

# %% [markdown]
# ### Solution.
# 
# empty

# %% [markdown]
# # 6. temperature X humidity
# [문제 2]  
# seaborn의 scatterplot을 이용하여 train 데이터셋의 temperature 피처와 humidity 피처의 관계를 시각화해 보세요.

# %%
fig, ax = plt.subplots(figsize = (10,5))

x_temperature = ___
y_humidity = ___

sns.regplot(x = x_temperature, y = y_humidity)

plt.show()

# %%
#checkcode
ensure_vals(globals(),'x_temperature','y_humidity')
@check_safety
def check(user_answer_x=x_temperature, user_answer_y=y_humidity, number = 100):

    c_point0 = sum(user_answer_x == train['temperature']) == number
    c_point1 = sum(user_answer_y == train['humidity']) == number

    if c_point0 and c_point1:
        return True
    else:
        return False

check()


# %% [markdown]
# ### Inst.
# 
# 지금까지는 feature와 target 간에
#  어떤 관계가 있는지를 시각화해 보았는데요. 이번에는 **feature 간에 서로 어떤 관계가 있는지**를 시각화해 보려 합니다.   
# 
# 먼저 train 데이터셋의 `temperature` 피처와 `humidity` 피처 간에 어떤 관계가 있는지 **seaborn의 regplot**을 이용하여 살펴보겠습니다. x_temperature 변수에는 train 데이터셋의 `temperature` 피처를, y_humidity 변수에는 train 데이터셋의 `humidity` 피처를 할당해 주세요.
# 출력된 결과를 보니 온도가 증가할수록 습도가 낮아지는군요! 즉, **온도와 습도는 음의 상관관계**임을 알 수 있습니다.

# %% [markdown]
# ### Hint.
# 
# 형태는 `데이터셋['피처명]` 입니다.

# %% [markdown]
# ### Solution.
# ```python
# fig, ax = plt.subplots(figsize = (10,5))
# 
# x_temperature = train['temperature']
# y_humidity = train['humidity']
# 
# sns.regplot(x = x_temperature, y = y_humidity)
# 
# plt.show()
# ```

# %% [markdown]
# # 7. cloudiness X precipitation

# %%
fig, ax = plt.subplots(figsize = (10,5))

x_cloudiness = train['cloudiness']
y_precipitation = train['precipitation']

sns.regplot(x = train['cloudiness'], y = train['precipitation'])

plt.show()

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# train 데이터셋의 wind_speed 피처와 wind_direction 피처 간에는 어떤 관계가 있을까요? 출력된 결과를 보니 구름의 양이 증가할수록 강수량 수치가 높아지는 걸 확인해 볼 수 있습니다. 하지만 그렇지 않은 데이터들도 보이네요. 즉, **구름의 양과 강수량은 대체로 양의 상관관계**임을 알 수 있습니다.
# 
# 
# 
# 
# 
# 

# %% [markdown]
# ### Hint.
# 
# empty

# %% [markdown]
# ### Solution.
# emtpy

# %% [markdown]
# # 8. humidity X cloudiness
# [문제 3]  
# seaborn의 scatterplot을 이용하여 train 데이터셋의 humidity 피처와 cloudiness 피처의 관계를 시각화해 보세요.

# %%
fig, ax = plt.subplots(figsize = (10,5))

x_humidity = ___
y_cloudiness = ___

sns.regplot(x = x_humidity, y = y_cloudiness)

plt.show()

# %%
#checkcode
ensure_vals(globals(),'x_humidity','y_cloudiness')
@check_safety
def check(user_answer_x=x_humidity, user_answer_y=y_cloudiness, number = 100):

    c_point0 = sum(user_answer_x == train['humidity']) == number
    c_point1 = sum(user_answer_y == train['cloudiness']) == number

    if c_point0 and c_point1:
        return True
    else:
        return False

check()

# %% [markdown]
# ### Inst.
# 
# x_humidity 변수에는 train 데이터셋의 `humidity` 피처를, y_cloudiness 변수에는 train 데이터셋의 `cloudiness` 피처를 할당해 주세요.
# 
# train 데이터셋의 humidity 피처와 cloudiness 피처 간에는 어떤 관계가 있을까요? 출력된 결과를 보니 습도가 증가할수록 흐린 정도의 수치가 높아지는 걸 확인해 볼 수 있습니다. 하지만 그렇지 않은 데이터들도 보이네요! 즉, **습도와 흐린 정도는 대체로 양의 상관관계**임을 알 수 있습니다.

# %% [markdown]
# ### Hint.
# 
# 형태는 `데이터셋['피처명']` 입니다.

# %% [markdown]
# ### Solution.
# ```python
# fig, ax = plt.subplots(figsize = (10,5))
# 
# x_humidity = train['humidity']
# y_cloudiness = train['cloudiness']
# 
# sns.regplot(x = x_humidity, y = y_cloudiness)
# 
# plt.show()
# ```

# %% [markdown]
# # 9. heatmap

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
sns.heatmap(train.corr(), annot = True, fmt = ".2f")

plt.show()

# %%
#checkcode
#empty

# %% [markdown]
# ### Inst.
# 
# `heatmap` 함수를 이용하면 변수 간 상관계수를 직관적으로 확인할 수 있습니다. heatmap은 독립변수간의 다중공선성 파악에도 용이합니다. 
# 

# %% [markdown]
# ### Hint.
# 
# empty  

# %% [markdown]
# ### Solution.
# 
# empty


