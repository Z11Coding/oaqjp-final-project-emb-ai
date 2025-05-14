import requests
import sys
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {
        "raw_document": { "text": text_to_analyse }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    responseTeamA = response.json()
    responseTeamB = responseTeamA["emotionPredictions"][0]["emotion"]
     
    strongestEmotion:str = "???"
    strongestValue:float = 0
    for emotion in responseTeamB.keys():
        value = responseTeamB[emotion]
        if value > strongestValue:
            strongestEmotion = emotion
            strongestValue = value

    responseTeamB["dominant_emotion"] = strongestEmotion

    return print(json.dumps(responseTeamB))

if len(sys.argv[0]) > 0:
    text_to_analyze = emotion_detector(sys.argv[1])