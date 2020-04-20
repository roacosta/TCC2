import moviepy.editor as mp
clip = mp.VideoFileClip("Amaj.mp4").subclip(0,20)
clip.audio.write_audiofile("GravaçõesTCC\Amaj.wav")