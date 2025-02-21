import requests

API_KEY_ASSEMBLYAI = "KEY"
filename = "output.wav"
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"

headers = {'authorization': API_KEY_ASSEMBLYAI}

running = True


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


while running:
    global num
    file = open("outNumber.txt", "r")
    string = file.read()
    file.close()
    if string == '0\nTranscribing_':
        txt = audioToTxt("output.wav").split(' ', 1)
        first_word = str(txt[0]).upper()
        print(first_word.upper())
        if first_word == 'ONE.':
            num = 1
        elif first_word == 'TWO.':
            num = 2
        elif first_word == 'THREE.':
            num = 3
        elif first_word == 'FOUR.':
            num = 4
        elif first_word == 'FIVE.':
            num = 5
        elif first_word == 'SIX.':
            num = 6
        elif first_word == 'SEVEN.':
            num = 7
        elif first_word == 'EIGHT.':
            num = 8
        elif first_word == 'NINE.':
            num = 9
        elif first_word == 'TEN.' or first_word == 'THEN.':
            num = 10
        else:
            num = 0
        stringWrite = str(num) + '\nTranscribed'
        file = open("outNumber.txt", "w")
        file.write(stringWrite)
        file.close()
    elif string == '0\nExit':
        running = False
