import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

#세계 국가의 데이터에서 기대수명만 뽑아서 시리즈 만들기
life_expectancy = data['Life Expectancy']

print(type(life_expectancy))
#각 국가의 기대수명에서 25%, 50%, 75%에 해당하는 값 확인하기
life_expectancy_quartiles = np.quantile(life_expectancy,[0.25, 0.5, 0.75])
#print(life_expectancy_quartiles)

#세계 국가의 데이터에서 GDP만 뽑아서 시리즈 만들기
gdp = data.GDP
#GDP의 중앙값을 구하고, 중앙값보다 높은 GDP Dataframe, 낮거나 같은 GDP Dataframe 만들기 
median_gdp = np.median(gdp)
low_gdp = data[data.GDP <= median_gdp]
print(low_gdp)
high_gdp = data[data.GDP > median_gdp]

#GDP의 중앙값보다 낮거나 같은 값을 가지는 국가들 중에서 25%, 50%, 75%에 해당하는 기대수명 확인하기
low_gdp_quartiles = np.quantile(low_gdp['Life Expectancy'], [0.25, 0.5, 0.75])
#GDP의 중앙값보다 높은 값을 가지는 국가들 중에서 25%, 50%, 75%에 해당하는 기대수명 확인하기
high_gdp_quartiles = np.quantile(high_gdp['Life Expectancy'],[0.25, 0.5, 0.75] )

#전체 GDP의 중앙값보다 높은 GDP를 가지는 국가들의 기대수명 값으로 50%의 투명도로 High GDP의 제목으로 히스토그램 plot하기
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
#전체 GDP의 중앙값보다 낮거나 같은 GDP를 가지는 국가들의 기대수명 값으로 50%의 투명도로 High GDP의 제목으로 히스토그램 plot하기
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
#자동으로 범례주기
plt.legend()
plt.show()