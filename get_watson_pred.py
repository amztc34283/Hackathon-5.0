from watson_developer_cloud import PersonalityInsightsV3
import json
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Correct usage is python get_watson_pred.py watson_in/<input.json> <person name>")
    else:
        file_name = sys.argv[1]
        name = sys.argv[2]
        service = PersonalityInsightsV3(version='2017-10-13',
        url='https://gateway-wdc.watsonplatform.net/personality-insights/api',
        iam_apikey='W7wjiNAzqzpVxaXhYMFMQ138rNY6g7GrwXVYj5nHzU7l')

        with open(file_name) as \
                profile_json:
            profile = service.profile(
                profile_json.read(),
                content_type='application/json', 
                raw_scores=True,
                consumption_preferences=True).get_result()

        with open("watson_out/"+ name +".json", "w+") as out_file:
            json.dump(profile, out_file, indent=2)
