"""
This is a translator (English to French module)
"""
from typing import Type
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


"""
API KEY AND URL
"""
URL_S2T = ""
IAM_APIKEY_S2T = ""

authenticator = IAMAuthenticator(IAM_APIKEY_S2T)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL_S2T)

def englishtofrench(_eng):
    """
    English to French Translation Function
    """
    if _eng is None or _eng == "":
        return "Argument Cannot Be Null or Empty"
    try: #Tests if argument is empty or not
        french_translation = language_translator.translate(
            text=_eng,
            model_id='en-fr').get_result()
        return french_translation['translations'][0]['translation']
    except TypeError:
        raise AssertionError("Please check your argument")
    except NameError:
        return "Name Error. Please Check Your Argument"
    except SyntaxError:
        return "Syntax Error. Please Check Your Argument"
    except ValueError:
        return "Argument Cannot Be Null or Empty"
    except: # pylint: disable=W0702 disable=bare-except disable=W0105
        return "Please check your argument"

def englishtogerman(_eng):
    """
    English to German Translation Function
    """
    if _eng is None or _eng == "":
        return "Argument Cannot Be Null or Empty"
    try: #Tests if argument is empty or not
        german_translation = language_translator.translate(
            text=_eng,
            model_id='en-de').get_result()
        return german_translation['translations'][0]['translation']
    except TypeError:
        raise AssertionError("Please check your argument")
    except NameError:
        return "Name Error. Please Check Your Argument"
    except SyntaxError:
        return "Syntax Error. Please Check Your Argument"
    except ValueError:
        return "Value Error. Please Check Your Argument"
    except: # pylint: disable=W0702 disable=bare-except disable=W0105
        return "Please check your argument"
