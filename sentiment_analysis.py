# -*- coding: utf-8 -*-
"""Sentiment Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R-6gfet45v4FynY4vW0Bwt0SkZFIkNUw

# **Sentiment Analysis**

*   Processes any textual message and recognizes the emotion embedded in it.
*   Compatible with 5 different emotion categories as Happy, Angry, Sad, Surprise and Fear.

## 1. Install the package
"""

pip install text2emotion

import text2emotion as te

"""## 2. Analyzing emotion in user speech"""

text = "I was asked to sign a third party contract a week out from stay. If it wasn't an 8 person group that took a lot of wrangling I would have cancelled the booking straight away. Bathrooms - there are no stand alone bathrooms. Please consider this - you have to clear out the main bedroom to use that bathroom. Other option is you walk through a different bedroom to get to its en-suite. Signs all over the apartment - there are signs everywhere - some helpful - some telling you rules. Perhaps some people like this but It negatively affected our enjoyment of the accommodation. Stairs - lots of them - some had slightly bending wood which caused a minor injury."

te.get_emotion(text)

"""Output in terms of dictionary where we have emotion categories along with the respective score.

Now, if we think about the scores of the relative emotion categories then **Fear** score is 0.45 & **Sad** score is 0.32. So on overall analysis we can say that the statement we took as input has the Fear & Sad tone.
"""

text = "The times are difficult! Our sales have been disappointing for the past three quarters for our data analytics product suite. We have a competitive data analytics product suite in the industry. However, we are not doing a good job at selling it, and this is really frustrating."

te.get_emotion(text)

"""Short messages:"""

text = "Good n8"
te.get_emotion(text)

text = "That night was so horrible."
te.get_emotion(text)

text = "I just love this surprise."
te.get_emotion(text)

text = "I can't understand what to do now."
te.get_emotion(text)

"""Statements which contain emojis:

"""

text = "you got this man 😆😂"
te.get_emotion(text)

text = "I am extremely interested in software."
te.get_emotion(text)