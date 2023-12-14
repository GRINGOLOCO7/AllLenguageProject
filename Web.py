import streamlit as st
import pandas as pd
import numpy as np
import subprocess
import sys
venv_python_path = sys.executable
#st.write(f"Python Executable Path: {venv_python_path}")

# streamlit run Web.py
# streamlit run c:/Users/orlan/OneDrive/Desktop/1semestre/AllLenguadge_Project_Technology/SumUp/AllLenguageProject/Web.py


st.title('Parla - WeSpeack')

# Allow users to select languages
st.write("LANGUAGES ALLOW:\n\n\n"
            "English: 'en'\nSpanish: 'es'\nFrench: 'fr'\n"
        "German: 'de'\nItalian: 'it'\nJapanese: 'ja'\n"
        "Chinese (Simplified): 'zh-CN'\nChinese (Traditional): 'zh-TW'\n"
        "Russian: 'ru'\nArabic: 'ar'\nKorean: 'ko'\n\n")
language_speaker1 = st.text_input("Enter language for Speaker 1 (e.g., 'en' for English):").strip().lower()
language_speaker2 = st.text_input("Enter language for Speaker 2 (e.g., 'es' for Spanish):").strip().lower()

# Create a button to start the communication
if st.button("Start Communication"):
    st.text("Communication has started. Speak now or say 'stop' to end.")

    # Run the speech-to-speech communication script using subprocess
    command = [venv_python_path, "main.py", language_speaker1, language_speaker2]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=r"C:\\Users\\orlan\\OneDrive\\Desktop\\1semestre\\AllLenguadge_Project_Technology\\SumUp\\AllLenguageProject\\")
    st.write(process)
    st.write(command)

    # # Capture and display the output
    # while process.poll() is None:
    #     output = process.stdout.readline()
    #     if output:
    #         st.text(output.strip())

    # # Display any error message
    # error_output = process.stderr.read()
    # if error_output:
    #     st.text(f"Error: {error_output.strip()}")

    # st.text("Communication has ended.")
