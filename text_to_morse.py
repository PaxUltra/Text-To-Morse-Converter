import pandas as pd

# Use Pandas to easily grab the translation from the CSV, and turn it into a dictionary.
morse_df = pd.read_csv('morse-code.csv')
morse_dict = {row.character: row.morse for (_, row) in morse_df.iterrows()}

def encode(text: str) -> str:
    '''
    Converts an alphanumeric string to Morse Code.

    Parameters:
        text (str):The string to convert. Must only consist of A-Z, 0-9, and whitespace.
    
    Returns:
        morse_output(str):The Morse Code representation of text.
    '''
    morse_list = [morse_dict[char] for char in text.upper()]
    morse_output = ' '.join(morse_list)

    return morse_output