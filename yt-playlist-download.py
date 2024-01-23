import os, shutil, subprocess
from pytube import Playlist, YouTube
from moviepy.editor import VideoFileClip
from tqdm import tqdm
import os

def run(pl, path):
    # insert the downloads destination (optional)
    
    # get linked list of links in the playlist
    links = pl.video_urls
    
    # download each item in the list
    for l in tqdm(links):
        
        # converts the link to a YouTube object
        yt = YouTube(l, use_oauth=True, allow_oauth_cache=True)
        
        # takes first stream; since ffmpeg will convert to mp3 anyway
        # changes: added filter with file extension of mp4
        music = yt.streams.filter(file_extension="mp4").first()
        
        # gets the filename of the first video stream
        default_filename = music.default_filename
        print(default_filename)
        print("Downloading " + default_filename + "...")
        
        # downloads first video stream and rename the first video stream
        music.download(output_path='Downloads')
        default_filename_remove_spaces = default_filename.replace(" ", "")
        try:
            # if its already renamed then pass
            os.rename(default_filename, default_filename_remove_spaces)
        except:
            pass
            
        # replaces mp4 with mp3 for ffmeg output
        new_filename = default_filename.replace("mp4", "mp3")
        new_filename_remove_spaces = new_filename.replace(" ", "")
        print("Converting to mp3....")
        
        # converts mp4 video to mp3 audio and moving the audio to folder input
        # NOTE: MUST HAVE "ffmpeg.exe" DOWNLOADED AND PLACED INSIDE THE DIRECTORY
        subprocess.call(f"ffmpeg -i {default_filename_remove_spaces} {new_filename_remove_spaces}", shell=True)
        # if exception then create download folder if not exists and store the downloaded audios
        def convert_mp4_to_mp3(input_path, output_path):
          video_clip = VideoFileClip(input_path)
          audio_clip = video_clip.audio
          audio_clip.write_audiofile(output_path, codec='mp3')
          video_clip.close()
          audio_clip.close()
        convert_mp4_to_mp3(path+'Downloads/'+default_filename, path+'Downloads/'+new_filename_remove_spaces)
        os.remove(path+'Downloads/'+default_filename)
    print("Download finished.")

if __name__ == "__main__":
    url = 'https://www.youtube.com/playlist?list=PLjSNRjMbBcgk0_lhj8IFe4HddGtLrnerS'
    path = '/content/'
    pl = Playlist(url)
    run(pl, path)