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
    
    if response.status_code == 400:
        for emotion in responseTeamB.keys():
            responseTeamB[emotion] = None
        return responseTeamB
    else:
            strongestEmotion:str = "???"
            strongestValue:float = 0
            for emotion in responseTeamB.keys():
                value = responseTeamB[emotion]
                if value > strongestValue:
                    strongestEmotion = emotion
                    strongestValue = value

            responseTeamB["dominant_emotion"] = strongestEmotion

    return responseTeamB