'''Web app using Streamlit where users can download YouTube videos'''


import streamlit as st
import re
from os import makedirs
from pytube import YouTube


makedirs('tmp', exist_ok=True)


def main():
    '''YouTube downloader'''

    st.title('YouTube Video Downloader')
    url = st.text_input('Enter YouTube video URL',
                        placeholder='https://www.youtube.com/watch?v=xxxxxxxxxxx')

    if st.button('Download Video'):
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            title = re.sub(r'[\\/*?:"<>|]', "", yt.title)
            stream.download(f'tmp/{title}.mp4')
            st.success('Video downloaded successfully!')
        except Exception as e:
            st.error(f'Error downloading: {e}')


if __name__ == '__main__':
    main()
