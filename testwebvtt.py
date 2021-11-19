import webvtt

for caption in webvtt.read('video.vtt'):
    print(caption.start)
    print(caption.end)
    print(caption.text)
