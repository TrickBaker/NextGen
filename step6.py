# Example of thematic analysis for open-ended responses
open_ended_responses = cleaned_data['If you faced difficulties, please describe them here']
themes = {
    'Navigation issues': 0,
    'Finding functions': 0,
    'Slow response times': 0,
    'System errors or bugs': 0,
    'Complicated forms': 0,
    'Data extraction difficulties': 0
}

for response in open_ended_responses.dropna():
    for theme in themes:
        if theme.lower() in response.lower():
            themes[theme] += 1

themes
