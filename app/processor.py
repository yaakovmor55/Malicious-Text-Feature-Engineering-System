import pandas as pd
# Import dependencies
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')# Compute sentiment labels


class Processor:
    def __init__(self, collection):
        self.df = pd.DataFrame(collection)

    def rare_word_in_text(self):
            if "Text" not in self.df.columns:
                raise ValueError("DataFrame must contain 'Text' column")
            rare_words = []
            for tweet in self.df["Text"]:
                all_words = pd.Series(tweet.lower().split())
                rarest_word = all_words.value_counts().idxmin()
                rare_words.append(rarest_word)
            self.df["rarest_word"] = rare_words

    def find_text_emotion(self):
        if "Text" not in self.df.columns:
            raise ValueError("DataFrame must contain 'Text' column")
        emotion = []
        for tweet in self.df["Text"]:
            score=SentimentIntensityAnalyzer().polarity_scores(tweet)
            compound = score["compound"]
            if compound > 0.5:
                emotion.append("Positive")
            elif compound == 0.49:
                emotion.append("Neutral")
            else:
                emotion.append("Negative")

        self.df["Emotion text"] = emotion

    def find_weapons(self):
        with open("../data/weapon_list.txt", "r") as f:
            weapons = set(line.strip() for line in f)

        if "Text" not in self.df.columns:
            raise ValueError("DataFrame must contain 'Text' column")

        weapons_list = []
        for tweet in self.df["Text"]:
            weapon = None
            for word in tweet:
                if word in weapons:
                    weapon = word
                    break
            weapons_list.append(weapon)
        self.df["weapons_detected"] = weapons_list



