import os
import argparse
import subprocess
import json
import streamlit as st

def read_exif_with_exiftool(directory):
    exif_data = {}

    for filename in os.listdir(directory):
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        if ext in ['.tif', '.tiff', '.jpg', '.jpeg']:
            full_path = os.path.join(directory, filename)

            result = subprocess.run(['exiftool', '-G', '-j', '-n', full_path], capture_output=True, text=True)
            
            metadata = json.loads(result.stdout)[0]

            exif_data[filename] = metadata

    return exif_data

def main_streamlit():
    st.title("EXIF Data Reader")

    directory = st.text_input("Enter the directory path:", value="")
    if st.button("Read EXIF data"):
        if directory:
            try:
                exif_data = read_exif_with_exiftool(directory)
                for filename, exif in exif_data.items():
                    st.write(f"{filename}: {exif}")
            except FileNotFoundError as e:
                st.error(str(e))
            except ValueError as e:
                st.error(str(e))
        else:
            st.error("Please enter a valid directory path.")

def main_cli():
    parser = argparse.ArgumentParser(description='Read EXIF data from images in a directory using exiftool.')
    parser.add_argument('directory', type=str, help='The directory containing the images.')
    args = parser.parse_args()

    directory = args.directory

    exif_data = read_exif_with_exiftool(directory)

    for filename, exif in exif_data.items():
        print(f"{filename}: {exif}")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='EXIF Data Reader')
    parser.add_argument('--streamlit', action='store_true', help='Run in Streamlit mode')
    args, _ = parser.parse_known_args()

    if args.streamlit:
        st.title('UAVs multispectral image corrections')
        main_streamlit()
    else:
        main_cli()


def run():
    main_streamlit()
  
   
    
    
# ---
try:
    run()
except Exception as e:
    st.error(f'**An exception ocurred:** {e}')
    st.stop()