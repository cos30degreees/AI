from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

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

print(translation)

spanish_translation =translation['translations'][0]['translation']
print(spanish_translation)

translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
print(translation_eng)

French_translation=language_translator.translate(
    text=translation_eng , model_id='en-fr').get_result()

French_translation['translations'][0]['translation']
