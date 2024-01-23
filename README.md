# Copy from [here](https://github.com/modkhi/yt-playlist), i revise the converter funtion

# yt-playlist
A YouTube playlist downloader. Requires [Python 3.11+](https://www.python.org/downloads/), [pytube](https://github.com/nficano/pytube), and [ffmpeg](https://www.ffmpeg.org/) to work.

This script will download the audio of every song in a YouTube playlist, then convert the audio to mp3. To use, place it in the folder in which you want to download the playlist.

I'm not author, clone from [here](https://github.com/modkhi/yt-playlist) then revise mp4 to mp3 converter and save logistic.

## Packages and versions
- pytube==12.1.0

## Installation
1. git clone ``https://github.com/modkhi/yt-playlist.git`` or download the source code
2. navigate to the folder
3. do ``pip install -r requirements.txt`` to install the package from requirements.txt
4. do ``py yt-playlist-download.py``
5. enjoy!

## Usage
- ``Please enter the url of the playlist you wish to download: `` - playlist from youtube only
    - e.g. ``https://www.youtube.com/playlist?list=OLAK5uy_lbX9HmX4ZrMSrS5wpDonp-EFy4IrhQeCc``
- ``Downloads destination (optional): `` - must insert the full path and code will create a folder call ``Downloads``
    - e.g. ``/content/``
- If `Pytube` occur bug when download: - install from github
    - e.g. ``python -m pip install git+https://github.com/nficano/pytube``