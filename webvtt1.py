import webvtt
vtt = webvtt.read('video.vtt')
for line in vtt:
    print('------')
    print(line.start)
    print(line.raw_text)
    print(line.end)
    print('------')
    #if line.text == line.raw_text:
        # only phrases without cues
        #print(line)

