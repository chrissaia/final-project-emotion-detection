import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotions(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]
        for statement, expected in test_cases:
            result = emotion_detector(statement)
            emotion = max(result['emotionPredictions'][0]['emotion'], key=result['emotionPredictions'][0]['emotion'].get)
            self.assertEqual(emotion, expected)

if __name__ == '__main__':
    unittest.main()