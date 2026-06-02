"""
Emotion Detection Module using Watson NLP
"""
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion in the provided text using IBM Watson NLP.
    
    Args:
        text_to_analyse (str): The text to analyze for emotions
        
    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion,
              or an error response if the input is invalid
    """
    
    # Handle blank input
    if not text_to_analyse or not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Initialize Watson NLP authenticator
    authenticator = IAMAuthenticator({'apikey': 'YOUR_API_KEY'})
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator,
        service_url='YOUR_SERVICE_URL'
    )
    
    try:
        # Analyze emotions using Watson NLP
        response = nlu.analyze(
            text=text_to_analyse,
            features=Features(emotion=EmotionOptions())
        ).get_result()
        
        # Extract emotion scores
        emotions = response['emotion']['document']['emotion']
        
        # Find dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': emotions.get('anger'),
            'disgust': emotions.get('disgust'),
            'fear': emotions.get('fear'),
            'joy': emotions.get('joy'),
            'sadness': emotions.get('sadness'),
            'dominant_emotion': dominant_emotion
        }
    except Exception as exception:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
