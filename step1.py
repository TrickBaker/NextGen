from app import data

# Convert categorical responses to numerical codes
# Example: Gender coding
data['Gender'] = data['Gender'].map({'1. Male': 1, '2. Female': 2})
data['With the current system, can you self-explore it?'] = data['With the current system, can you self-explore it?'].map({'1. Yes': 1, '2. No': 2})
# Example: How frequently do you use this system in a month? remove lan '< 2 times/lần' -> '< 2 times'
data['How frequently do you use this system in a month?'] = data['How frequently do you use this system in a month?'].str.replace('/lần', '')

# Example: Likert scale items
# Apply this logic from the columns has index 13 to 37 ignore the t 38 and get from 39 to 43
# Define the columns containing Likert scale responses

likert_columns = data.columns[13:37].append(data.columns[38:46])
likert_scale_mapping = {
    '1 - Very Difficult to use': 1,
    '2 - Somewhat Difficult to use': 2,
    '3 - Neutral': 3,
    '4 - Somewhat Easy to use': 4,
    '5 - Very Easy to use': 5,
    '2 - Somewhat Difficult/ Khó khăn': 2,
    '2 - Somewhat Difficult': 2,   
    '3 -  Neutral / Bình thường': 3,
    '3 -  Neutral': 3,
    '4 - Somewhat Easy': 4,
    '4 - Somewhat Easy/ Dễ dàng': 4,
    '5 - Very Easy': 5,
    '5 - Very Easy/ Rất dễ dàng': 5,
    '1 - Very Difficult to use': 1,
    '1 - Very Difficult to use/ Rất khó khăn để sử dụng': 1,
    '2 - Somewhat Difficult to use': 2,
    '2 - Somewhat Difficult to use/ Khó khăn đề sử dụng': 2,
    '3 - Neutral': 3,
    '3 - Neutral ': 3,
    '3 - Neutral/ Bình thường': 3,
    '4 - Somewhat Easy to use': 4,
    '4 - Somewhat Easy to use/ Dễ dàng sử dụng': 4,
    '5 - Very Easy to use': 5,
    '5 - Very Easy to use/ Rất dễ dàng sử dụng': 5,
    'Always': 1,
    'Always/ Luôn luôn': 1,
    'Never': 5,
    'Never/ Không bao giờ': 5,
    'Rarely': 4,
    'Rarely/ Hiếm khi': 4,
    'Sometimes': 3,
    'Sometimes/ Thỉnh thoảng': 3,
    'Usually': 2,
    'Usually/ Thường xuyên': 2,
    'Somewhat Useful': 4,
    'Somewhat Useful/ Khá hữu ích': 4,
    'Somewhat Useless': 2,
    'Somewhat Useless/ Khá không hiệu quả': 2,
    'Useful': 5,
    'Useful/ Hữu ích': 5,
    'Somewhat Difficult': 2,
    '2 - Somewhat Difficult/ Khó khăn': 2,
    'Somewhat Easy': 4,
    '4 - Somewhat Easy/ Dễ dàng': 4,
    'Very Easy': 5,
    '5 - Very Easy/ Rất dễ dàng': 5,
    'Somewhat unsatisfied' : 2,
    'Somewhat satisfied' : 4,
    'Very satisfied' : 5,
    'Neutral' : 3,
    'Very unsatisfied' : 1,
    '3 - Neutral /Bình thường': 3,
    'Rarely / Hiếm khi': 2,
    'Neutral / Bình thường': 3,
    'Very Difficult': 1,
    'Never/Không bao giờ': 1,
    'Useless/ Không hiệu quả': 1,
    'Useless': 1,
    '2 - Only a little': 2,
    '2 - Only a little/ Chỉ một ít': 2,
    '3 - To some extent': 3,
    '3 - To some extent/ Tương đối': 3,
    '4 - Rather much': 4,
    '4 - Rather much/ Khá nhiều': 4,
    '5 - Very much': 5,
    '5 - Very much/ Rất nhiều': 5,
    '1 - Not at all': 1,
    '1 - Not at all/ Không có gì': 1,
    'Strongly Agree': 5,
    'Strongly Agree/ Hoàn toàn đồng ý': 5,
    'Agree': 4,
    'Agree/ Đồng ý': 4,
    'Neutral': 3,
    'Neutral/ Bình thường': 3,
    'Disagree': 2,
    'Disagree/ Không đồng ý': 2,
    'Strongly Disagree': 1,
    'Strongly Disagree/ Hoàn toàn không đồng ý': 1,
    'No training was provided': 0,
    'No training was provided/ Không có buổi đào tạo nào': 0,
    'No, I did not': 1,
    'No, I did not/ Không, tôi đã không tham dự': 1,
    'Yes, I attended/ Có, tôi đã tham dự': 2,
    'Yes, I attended': 2,
    '5 - Very clear': 5,
    '5 - Very clear/ Rất rõ ràng': 5,
    '4 - Clear': 4,
    '4 - Clear/ Rõ ràng': 4,
    '3 - Neutral': 3,
    '3 - Neutral/ Bình thường': 3,
    '2 - Unclear': 2,
    '2 - Unclear/ Không rõ ràng': 2,
    '1 - Very unclear': 1,
    '1 - Very unclear/ Rất không rõ ràng': 1,
    '5 - Very competent/ Năng lực rất tốt': 5,
    '5 - Very competent': 5,
    '4 - Competent/ Có năng lực': 4,
    '4 - Competent': 4,
    '3 - Neutral': 3,
    '3 - Neutral/ Bình thường': 3,
    '2 - Incompetent/ Không có năng lực': 2,
    '2 - Incompetent': 2,
    '1 - Very incompetent/ Rất không có năng lực': 1,
    '1 - Very incompetent': 1,
    '3 - Neutral/Bình thường': 3,
    '5 - Very helpful/ Rất hữu ích': 5,
    '4 - Quite helpful/ Khá hữu ích': 4,
    '0 - No material was provided/ Không có tài liệu đào tạo': 0,
    '0 - No material was provided': 0,
    '2 - Not very helpful': 2,
    '2 - Not very helpful/ Không hữu ích lắm': 2,
    '3 - Neutral/Bình thường': 3,
    '4 - Quite helpful': 4,
    '4 - Quite helpful/ Khá hữu ích': 4,
    '5 - Very helpful/ Rất hữu ích': 5,
    '5 - Very helpful': 5,
}

# Apply mappings
for column in likert_columns:
    data[column] = data[column].replace(likert_scale_mapping)

# Save the cleaned and mapped data to an Excel file, checking the path
output_path = 'Updated_Cleaned_Survey_Data_V1.0.xlsx'  # Adjust path as necessary
data.to_excel(output_path, index=False)

