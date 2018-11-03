from watson_developer_cloud import PersonalityInsightsV3
import json

service = PersonalityInsightsV3(
     version='2017-10-13',
## url is optional, and defaults to the URL below. Use the correct URL for your region.
     url='https://gateway-wdc.watsonplatform.net/personality-insights/api',
     iam_apikey='W7wjiNAzqzpVxaXhYMFMQ138rNY6g7GrwXVYj5nHzU7l')

with open('test.json') as \
        profile_json:
    profile = service.profile(
        profile_json.read(),
        content_type='application/json', ## use text/plain if it is plain text
        raw_scores=True,
        consumption_preferences=True).get_result()

print(json.dumps(profile, indent=2))
