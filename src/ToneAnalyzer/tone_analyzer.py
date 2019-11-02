from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from constants import *


class ToneAnalyzer:
    """
    Responsible for recognizing the tones given a paragraph.
    Uses IBM Watson Tone Analyzer API.
    """

    def __init__(self):
        self.authenticator = IAMAuthenticator(Constants.API_KEY)
        self.tone_analyzer = ToneAnalyzerV3(
            authenticator=self.authenticator,
            version=Constants.API_VERSION
        )
        self.tone_analyzer.set_service_url(Constants.API_URL)

    def analyze(self, paragraph):
        """
        Analyze a certain paragraph.
        :param paragraph: the paragraph as one string
        :return: the scores for different tones
        """
        tones = self.tone_analyzer.tone(
            tone_input={'text': paragraph},
            content_type='application/json'
        ).get_result()

        ret = {}

        if Constants.API_FIELD_DOCUMENT_TONE not in tones.keys():
            raise Exception("Error in API call")

        for tone in tones[Constants.API_FIELD_DOCUMENT_TONE][Constants.API_FIELD_TONES]:
            ret[tone[Constants.API_FIELD_TONE_ID]] = tone[Constants.API_FIELD_TONE_SCORE]
        return ret
