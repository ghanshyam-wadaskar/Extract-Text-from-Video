import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as yta

# Define a function to retrieve the transcript data and save it to a text file
def retrieve_transcript_and_save(video_id, filename):
    try:
        # Retrieve the transcript data for the specified video ID
        data = yta.get_transcript(video_id)

        # Extract the transcribed text from the transcript data
        transcribed_text = ''
        for value in data:
            for key, val in value.items():
                if key == 'text':
                    transcribed_text += val
                    final_transcript = "".join(transcribed_text.splitlines())

        # Save the transcribed text to the specified file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(final_transcript)

        return "Transcript saved successfully to " + filename, final_transcript

    except Exception as e:
        return "Error: " + str(e), None

# Define the Streamlit app
def main():
    # Set page title
    st.title("YouTube Video Transcript Extractor")

    # Get the YouTube video URL or ID from the user
    youtube_video = st.text_input("Enter YouTube Video URL or ID:")

    # Get the filename from the user
    filename = st.text_input("Enter filename to save transcript (e.g., transcript.txt):")

    # Check if both the YouTube video URL/ID and filename are provided
    if youtube_video and filename:
        # Check if the input string contains the "=" delimiter
        if "=" in youtube_video:
            # Split the input string using "=" as the delimiter and get the video ID
            video_id = youtube_video.split("=")[-1]

            # Retrieve the transcript and save it to the specified file
            result, transcribed_text = retrieve_transcript_and_save(video_id, filename)

            # Display the result to the user
            st.write(result)

            # Display the YouTube video
            st.title("YouTube Video")
            st.video(youtube_video)

            # Display the extracted text
            if transcribed_text:
                st.title("Extracted Text")
                st.write(transcribed_text)

        else:
            # Display a message if the "=" delimiter is not found in the input string
            st.write("Please enter a valid YouTube Video URL or ID")

# Run the Streamlit app
if __name__ == "__main__":
    main()
