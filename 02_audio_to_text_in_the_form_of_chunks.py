# Converting the audio to text (Here text is in the form of chunks) and save them in the "jsons" folder
import whisper
import json
import os

# Using Open AI's whisper's base model for converting the audio to text
model = whisper.load_model("base")

audios = os.listdir("audios")

for audio in audios:
    tutorial_number = audio.split("_")[0]
    file_name = audio.split("_")[1].split(".mp3")[0]
    print(tutorial_number, file_name)

    try:
        result = model.transcribe(audio = f"audios/{audio}", 
                                language = "hindi", # The spoken language is Hindi.
                                task = "translate", # Convert Hindi speech into English text. If you use "transcribe" instead of "translate", it will convert Hindi speech into Hindi text.
                                word_timestamps = False) # word_timestamps = False means, we don't want the start and end time of each word, we want the start and end time of each segment/chunk. If you want the start and end time of each word, then set word_timestamps = True.
        print(f"{audio} completed")

    except Exception as e:
        print(f"Error in {audio}: {e}")
        continue

    # We will get to know, what is: result["segments"], segment["start"], segment["end"], segment["text"] and result["text"]; If we print(result) and we will get the answer of all these questions.

    chunks = []
    for segment in result["segments"]:
        chunk = {
            "tutorial_number": tutorial_number,
            "file_name": file_name,
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        }
        chunks.append(chunk)


    chunks_with_metadata = {
        "chunks": chunks,
        "text": result["text"]
    }

    # Note: Create "jsons" folder manually before running this code, otherwise it will give an error.
    with open(f"jsons/{audio}.json", "w") as f:
        json.dump(chunks_with_metadata, f)