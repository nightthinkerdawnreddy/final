from ibm_watson import SpeechToTextV1, speech_to_text_v1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator
apikey="eF72RIHBKl_82wy0Nua2MLG3obJF00l0gRMQr7NZ9KMQ"
url="https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/13caf4f9-fea0-45eb-a135-c36410192eb5"
authenticator = IAMAuthenticator(apikey)
sst=SpeechToTextV1(authenticator=authenticator)
sst.set_service_url(url)
with open("working.webm","rb") as f:
    res = sst.recognize(audio=f,content_type="audio/webm",model="en-US_NarrowbandModel",continuous=True).get_result()
print(res)
