## Steps to create this RAG Based AI Teaching Assistent:

## step 1: Collect all your videos and store them in a folder

## step 2: Run videos_to_mp3.py to convert videos to mp3s
Convert the videos into .mp3 files using ffmpeg. (eg: ffmpeg -i file_name 1.mp3)

## step 3: Run mp3_to_json.py to convert mp3s to text
Convert the .mp3 files into english text using Open AI's Whisper where model should be "large-v2" (caution: Don't use "turbo" model)

After converting speech to text using whisper, extract the content of each segment of the audio file like title, video number, start time, end time, text etc and stote it in a .json file for each audio and then dump all jsons in a jsons folder.

## step 4: Run read_chunks.py file for storing embeddings of text of each chunk
After creating a json file for each audio file, create embeddings of the text of each chunk of audio file using ollama and it's "bge-m3" model and append these chunks in a list and using that list, create a data frame and dump that dataframe using joblib

## step 5: Run process_incoming.py(Prompt generation and feeding it to the LLM)
Now, create or convert the incoming query(question form user) into embeddings(vector form) using ollama and bge-m3 model.

Compare all the embeddings of text of each audio files with the embeddings of incoming query(i.e user question) and find the similarities

Using argsort() method , extract the indices of similarties and then load the created dataframe using joblib and then using the .loc[] function of pandas create a new dataframe consisting of chunks similar to the incoming query

Create a prompt and then use ollama models like llama3.2 or higher level models like gpt 5, etc for getting response of the prompt you created

After getting the response, compare whether it is accurate or not and if not accurate then try to use a better model. 