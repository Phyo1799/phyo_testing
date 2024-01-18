# import pandas as pd
# from googletrans import Translator

# def translate_text(text, target_language='ar'):
#     translator = Translator()
#     translation = translator.translate(text, dest=target_language)
#     return translation.text

# def translate_csv(input_file, output_file):
#     df = pd.read_csv(input_file)

#     # Ensure the 'description' column exists
#     if 'description' not in df.columns:
#         raise ValueError("The 'description' column is not found in the CSV file.")

#     # Translate each description and create a new 'translated_description' column
#     df['translated_description'] = df['description'].apply(translate_text)

#     # Save the translated data to a new CSV file
#     df.to_csv(output_file, index=False)

# if __name__ == "__main__":
#     input_csv = r'C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\Description to fix.csv'
#     output_csv = r'C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\Description_fixed.csv'

#     translate_csv(input_csv, output_csv)


import pandas as pd
from googletrans import Translator

def translate_text(text, target_language='ar'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def translate_csv_in_batches(input_file, output_file, batch_size=100):
    df = pd.read_csv(input_file)

    # Ensure the 'description' column exists
    if 'description' not in df.columns:
        raise ValueError("The 'description' column is not found in the CSV file.")

    # Translate descriptions in batches
    translated_descriptions = []
    for i in range(0, len(df), batch_size):
        batch = df['description'].iloc[i:i + batch_size]
        translations = batch.apply(translate_text)
        translated_descriptions.extend(translations)

    # Create a new column with translated descriptions
    df['translated_description'] = translated_descriptions

    # Save the translated data to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_csv = r'C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\Description to fix.csv'
    output_csv = r'C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\Description_fixed.csv'

    translate_csv_in_batches(input_csv, output_csv, batch_size=100)
