import PyPDF2
from tkinter import Tk     
from tkinter.filedialog import askopenfilename
import torch
from TTS.api import TTS


print("Select your pdf file: ") 
Tk().withdraw()
pdf = askopenfilename()

audio = input("Enter the desired audio file name: ") + ".wav"

tts = TTS(model_name="tts_models/en/ek1/tacotron2", progress_bar=False)
with open(pdf, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    text_content = ""
    
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        text_content += text

print(text_content)
tts.tts_to_file(text=text_content, file_path=audio)


print(f"{pdf} was saved as {audio}")
