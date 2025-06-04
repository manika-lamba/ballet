from dotenv import load_dotenv
import os
import openai
import pandas as pd

file_path = 'data.csv'
df = pd.read_csv(file_path)

# Load environment variables from .env file
load_dotenv()

for i in range (0,5):
    file_content = df['text'][i]  
    # Initialize the OpenAI client
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    messageinput = "Analyze the following text and summarize the information in the format: ' Year	Ballet	BalletCompany	Venue	City	Country	For	Choreographer1	Choreographer2	Choreographer3	Choreographer4	Regisseur	Muse1	Muse2	Muse3	YearMusic1	Composer1	YearMusic2	Composer2	YearArrangements	Arrangements	YearStory	BasedOn	Librettist	CostumeDesigner	Décor	Scenery	Other	Other2	Other3',please find all the element in the following content I gave you. If you can not find one element please leave it as none, like 'Muse1 : none'. Here is the text contect for the ballet dance: " + file_content
    # Create a chat completion request for text analysis with specific output format
    completion = client.chat.completions.create(
      model="gpt-4",
      messages=[
        {"role": "system", "content": "You are an insightful assistant, skilled in analyzing text about ballet and summarizing the findings in a structured format."},
        {"role": "user", "content": messageinput }
      ]
    )

# Print the structured summary
    filename = 'result_4/' + str(i) + '.txt'
    with open(filename,'w') as file:
      file.write(completion.choices[0].message.content)
