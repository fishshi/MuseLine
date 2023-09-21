import librosa
import numpy

y, sr = librosa.load('./data/music2.mp3')

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {} beats per minute'.format(tempo))

beat_times = librosa.frames_to_time(beat_frames, sr=sr)

beat_times = numpy.array(beat_times)
beat_times -= 1.84  #此处减去音符移动需要的时间 PS：好轴！

print(beat_times.tolist())