import json
import requests
from analysis import Analysis

headers = "application/json"
with open("config_requests.json") as f:
    config = json.load(f)


def get_analyzed_text(text):
    analyzis = Analysis(text)
    analyzis.language = get_detect_language(text)
    analyzis.sentiment = get_sentiment(text)
    analyzis.topic = get_topic(text)
    analyzis.summarized = get_summarized_text(text)

    return analyzis


def get_detect_language(text):
    language_response = requests.request(
        "POST",
        config.get("detect_language"),
        params={"input": text},
        headers=headers
    )
    return language_response


def get_sentiment(text):
    sentiment_response = requests.request(
        "POST",
        config.get("sv_sentiment"),
        params={"input": text},
        headers=headers
    )
    return sentiment_response


def get_topic(text):
    topic_response = requests.request(
        "POST",
        config.get("topic"),
        params={"input": text},
        headers=headers
    )
    return topic_response


def get_summarized_text(text):
    summarize_response = requests.request(
        "POST",
        config.get("summarize_text"),
        params={"input": text},
        headers=headers
    )
    return summarize_response
