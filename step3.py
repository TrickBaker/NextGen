import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from step1 import cleaned_data, likert_columns

# # Bar Chart for Department Distributionp
# departments = cleaned_data['Your Department/ Bộ phận:'].value_counts()
# plt.figure(figsize=(10, 6))
# departments.plot(kind='bar', color='skyblue')
# plt.xlabel('Department')
# plt.ylabel('Number of Respondents')
# plt.title('Distribution of Respondents by Department')
# plt.xticks(rotation=45)
# plt.show()


# # Pie Chart for Job Level Distribution
# job_levels = cleaned_data['Your job level / Cấp bậc:'].value_counts()
# plt.figure(figsize=(8, 8))
# job_levels.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightgreen', 'lightcoral', 'lightskyblue'])
# plt.title('Proportion of Respondents by Job Level')
# plt.ylabel('')
# plt.show()

# # Assuming we have a column for age, we will create a histogram
# # For this example, we will simulate age data as it is not provided in the sample


# # Simulated age data
# np.random.seed(0)
# ages = np.random.randint(22, 60, size=len(cleaned_data))
# cleaned_data['Age'] = ages

# print(len(cleaned_data))

# plt.figure(figsize=(10, 6))
# plt.hist(cleaned_data['Age'], bins=10, color='lightblue', edgecolor='black')
# plt.xlabel('Age')
# plt.ylabel('Number of Respondents')
# plt.title('Age Distribution of Respondents')
# plt.show()

# # List all column names to identify the exact column name
# column_names = cleaned_data.columns.tolist()
# column_names


# # Correct column name identification
# usability_score_column = 'Rate the following STATEMENTS according to your experience:'

# # Step 1: Data Preparation (continued)
# usability_scores = cleaned_data[usability_score_column]

# # Step 2: Descriptive Statistics (continued)
# # Calculate frequencies for categorical data
# gender_freq = cleaned_data['Gender'].value_counts(normalize=True) * 100
# job_level_freq = cleaned_data['Your job level / Cấp bậc:'].value_counts(normalize=True) * 100
# department_freq = cleaned_data['Your Department/ Bộ phận:'].value_counts(normalize=True) * 100

# # Measure Central Tendency and Variability
# likert_descriptive_stats = cleaned_data[likert_columns].describe()

# # Output frequencies and descriptive statistics
# gender_freq, job_level_freq, department_freq, likert_descriptive_stats

# # Box Plot for Usability Satisfaction Scores
# plt.figure(figsize=(10, 6))
# plt.boxplot(usability_scores.dropna(), vert=False, patch_artist=True)
# plt.xlabel('Usability Scores')
# plt.title('Distribution of Satisfaction Scores on System Usability')
# plt.show()

# # Cross-tabulation example
# cross_tab = pd.crosstab(cleaned_data['Your Department/ Bộ phận:'], usability_scores)
# cross_tab.plot(kind='bar', stacked=True, figsize=(12, 8))
# plt.xlabel('Department')
# plt.ylabel('Frequency')
# plt.title('Department vs Ease of Use Satisfaction Levels')
# plt.xticks(rotation=45)
# plt.show()



# # Assuming we have a column for overall satisfaction
# overall_satisfaction_column = 'How satisfied are you with the range of features and functions offered by our systems?'

# # Correlation analysis example
# correlation = cleaned_data[[usability_score_column, overall_satisfaction_column]].corr()
# correlation


# # Extract the relevant column for the pie chart
# system_usage_column = 'Which system do you usually use for your daily tasks? Please use this system as the reference for other questions in this survey./\xa0Bạn thường sử dụng hệ thống nào cho các nhiệm vụ hàng ngày của mình? '

# # Count the frequencies of each system used
# system_usage_counts = cleaned_data[system_usage_column].value_counts()

# # Draw the pie chart
# plt.figure(figsize=(8, 8))
# system_usage_counts.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink'])
# plt.title('System Usage Distribution for Daily Tasks')
# plt.ylabel('')
# plt.show()


# # Extract the relevant columns
# usage_frequency_column = 'How frequently do you use this system in a month?/Bạn thường sử dụng hệ thống này mỗi tháng bao nhiêu lần?'
# system_usage_column = 'Which system do you usually use for your daily tasks? Please use this system as the reference for other questions in this survey./\xa0Bạn thường sử dụng hệ thống nào cho các nhiệm vụ hàng ngày của mình? '

# # Clean data
# cleaned_data = cleaned_data.dropna(subset=[usage_frequency_column, system_usage_column])

# # Create a cross-tabulation
# cross_tab = pd.crosstab(cleaned_data[system_usage_column], cleaned_data[usage_frequency_column])

# # Plot the cross-tabulation as a stacked bar chart
# cross_tab.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='viridis')
# plt.xlabel('System Used')
# plt.ylabel('Frequency')
# plt.title('Cross-Tabulation of System Usage and Frequency of Use')
# plt.xticks(rotation=45)
# plt.legend(title='Usage Frequency', bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.show()

from scipy.stats import ttest_1samp

# Relevant columns for Hypothesis 1
ease_of_use_col = 'How easy do you use the system?/ Bạn có thấy dễ dàng khi sử dụng hệ thống?'
visual_appeal_col = "What do you think of the visual appeal of the system's user interface?/ Bạn thấy giao diện của hệ thống như thế nào?\n"
trouble_logging_in_col = 'Rate the FREQUENCY of the following ISSUES\xa0according to your experience with the system /\nĐánh giá TẦN SUẤT của các VẤN ĐỀ sau dựa trên trải nghiệm của bạn với hệ thống.\n.Trouble logging in or session'
error_messages_col = 'Rate the FREQUENCY of the following ISSUES\xa0according to your experience with the system /\nĐánh giá TẦN SUẤT của các VẤN ĐỀ sau dựa trên trải nghiệm của bạn với hệ thống.\n.Error messages when submittin'
slow_performance_col = 'Rate the FREQUENCY of the following ISSUES\xa0according to your experience with the system /\nĐánh giá TẦN SUẤT của các VẤN ĐỀ sau dựa trên trải nghiệm của bạn với hệ thống.\n.Slow performances or system c'
incorrect_data_col = 'Rate the FREQUENCY of the following ISSUES\xa0according to your experience with the system /\nĐánh giá TẦN SUẤT của các VẤN ĐỀ sau dựa trên trải nghiệm của bạn với hệ thống.\n.Incorrect data or information'
improvement_suggestions_col = 'In your opinion, what should the system improve to better support your work?/\xa0Theo ý kiến của bạn, hệ thống cần cải thiện những gì để hỗ trợ công việc của bạn tốt hơn?'

# Clean the data by dropping NA values in relevant columns
cleaned_data = cleaned_data.dropna(subset=[ease_of_use_col, visual_appeal_col, trouble_logging_in_col, error_messages_col, slow_performance_col, incorrect_data_col])

# Descriptive statistics for ease of use and visual appeal
ease_of_use_stats = cleaned_data[ease_of_use_col].describe()
visual_appeal_stats = cleaned_data[visual_appeal_col].describe()

# Frequency of reported issues
trouble_logging_in_freq = cleaned_data[trouble_logging_in_col].value_counts(normalize=True) * 100
error_messages_freq = cleaned_data[error_messages_col].value_counts(normalize=True) * 100
slow_performance_freq = cleaned_data[slow_performance_col].value_counts(normalize=True) * 100
incorrect_data_freq = cleaned_data[incorrect_data_col].value_counts(normalize=True) * 100

# One-sample t-test against a threshold value (3)
ease_of_use_ttest = ttest_1samp(cleaned_data[ease_of_use_col], 3)
visual_appeal_ttest = ttest_1samp(cleaned_data[visual_appeal_col], 3)

# Display results
ease_of_use_stats, visual_appeal_stats, trouble_logging_in_freq, error_messages_freq, slow_performance_freq, incorrect_data_freq, ease_of_use_ttest, visual_appeal_ttest
