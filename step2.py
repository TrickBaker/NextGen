from step1 import cleaned_data, likert_columns
# Calculate frequencies for categorical data
gender_freq = cleaned_data['Gender'].value_counts(normalize=True) * 100
job_level_freq = cleaned_data['Your job level / Cấp bậc:'].value_counts(normalize=True) * 100
department_freq = cleaned_data['Your Department/ Bộ phận:'].value_counts(normalize=True) * 100

gender_freq, job_level_freq, department_freq


# Calculate central tendency and variability for Likert scale items
likert_descriptive_stats = cleaned_data[likert_columns].describe()

likert_descriptive_stats
