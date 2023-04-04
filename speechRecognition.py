import requests

API_KEY_ASSEMBLYAI = "fed83bbeb54f4efc929579e670b83f8d"
filename = "output.wav"
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {'authorization': API_KEY_ASSEMBLYAI}


# upload
def upload(filewav):
    def read_file(filewav, chunk_size=5242880):
        with open(filewav, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint,
                                    headers=headers,
                                    data=read_file(filewav))
    audio_url = upload_response.json()['upload_url']
    return audio_url


# transcribe
def transcribe(audio_url):
    transcript_request = {"audio_url": audio_url}
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    job_id = transcript_response.json()['id']
    return job_id


# poll
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_result_url(audio_url):
    transcript_id = transcribe(audio_url)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']


def audioToTxt(filename):
    print('Transcribing')
    try:
        audio_url = upload(filename)
        # transcript_id = transcribe(audio_url)
        # print(transcript_id)  # job_id
        data, error = get_transcription_result_url(audio_url)
        return data['text']
    except:
        return 'ZERO.'
