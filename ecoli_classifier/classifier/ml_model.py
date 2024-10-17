import joblib
from django.core.cache import cache
from django.conf import settings
import os
import pandas as pd
import numpy as np

def load_model():
    model_key = 'ecoli_model'
    model = cache.get(model_key)
    if model is None:
        model_path = os.path.join(settings.BASE_DIR, 'classifier', 'ecoli_classifier_final.joblib')
        model = joblib.load(model_path)
        cache.set(model_key, model, timeout=None)
    return model

def load_encoder():
    encoder_key = 'ecoli_encoder'
    encoder = cache.get(encoder_key)
    if encoder is None:
        encoder_path = os.path.join(settings.BASE_DIR, 'classifier', 'ecoli_encoder.joblib')
        encoder = joblib.load(encoder_path)
        cache.set(encoder_key, encoder, timeout=None)
    return encoder

def predict_sequence(sequence):
    model = load_model()
    encoder = load_encoder()
    
    # Preprocess the sequence
    sequence_df = pd.DataFrame([list(sequence)], columns=[f'Pos_{i}' for i in range(len(sequence))])
    
    # Encode the sequence
    encoded_sequence = encoder.transform(sequence_df)
    
    # Make prediction
    prediction = model.predict(encoded_sequence)
    
    return 'Positive' if prediction[0] == 1 else 'Negative'