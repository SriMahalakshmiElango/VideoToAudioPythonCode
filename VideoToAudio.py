import moviepy.editor as mp
def extract_audio(video_path,savename):
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(savename)

video_path = 'Downloads/videofile.mp4'
savename = 'Downloads/audiofile.mp3'
extract_audio(video_path,savename)
print('Done')
