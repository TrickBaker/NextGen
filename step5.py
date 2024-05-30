from scipy.stats import ttest_ind, f_oneway

# Assuming we have two groups to compare for simplicity
group1 = cleaned_data[cleaned_data['Your Department/ Bộ phận:'] == '1. Human Resources']['How satisfied are you with the range of features and functions offered by our systems?'].dropna()
group2 = cleaned_data[cleaned_data['Your Department/ Bộ phận:'] == '2. Information Technology']['How satisfied are you with the range of features and functions offered by our systems?'].dropna()

t_stat, p_value = ttest_ind(group1, group2)
t_stat, p_value

import statsmodels.api as sm

# Regression analysis
X = cleaned_data[['Rate the following STATEMENTS according to your experience:/ Đánh giá các KHẲNG ĐỊNH sau dựa trên trải nghiệm của bạn:.Ease of use / Dễ sử dụng', 'Did you attend the training session for the system?']]
X = sm.add_constant(X)
Y = cleaned_data['How satisfied are you with the range of features and functions offered by our systems?']

model = sm.OLS(Y.dropna(), X.dropna()).fit()
model_summary = model.summary()
model_summary
