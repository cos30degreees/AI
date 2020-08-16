from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas.io.json import json_normalize
url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/889b0f18-cc04-4f13-b002-fe5e26043035"

iam_apikey_s2t = "zSZ8z72_koa2Szcir2R-e6beICeno8VBE_I9ZSlSuhHG"

authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t
filename='PolynomialRegressionandPipelines.mp3'
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
print(response.result)

json_normalize(response.result['results'],"alternatives")

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)



from ibm_watson import LanguageTranslatorV3

url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/9f9ed607-b49b-43ff-bcbd-22d27722a314'

apikey_lt='yQ-Wd_DBlHWs5yxpLdTrHy3tRPa8SPmdWku3ZGmDU0Iy'

version_lt='2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
print(language_translator)

from pandas.io.json import json_normalize
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

translation_response = language_translator.translate(\
    text=recognized_text, model_id='en-es')
print(translation_response)

translation=translation_response.get_result()

translation=translation_response.get_result()
translation
print(translation)

spanish_translation =translation['translations'][0]['translation']
spanish_translation

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
translation_eng

French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()
French_translation['translations'][0]['translation']
