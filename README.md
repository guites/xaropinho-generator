## Xaropinho Generator

![the xaropinho itself](xaropinho.jpg)

This project is an homage to the greatest tv show rat to ever live.

### Dependencies:

1. [youtube-dl](https://github.com/ytdl-org/youtube-dl)
2. [videogrep](https://github.com/antiboredom/videogrep)
3. [webvtt-py](https://webvtt-py.readthedocs.io/en/latest/usage.html)


#### Cheatsheet:

Download youtube video with subtitles

    youtube-dl --sub-lang pt --write-auto-sub 'https://www.youtube.com/watch?v=nhP0XU4s61Q'

List available subtitles for youtube video

    youtube-dl --list-subs 'https://www.youtube.com/watch?v=nhP0XU4s61Q'

Cut video based on word \(returns whole subtitle line\)

    videogrep --input "./XaropinhoNomeandoPlacasDeTransito.mp4" --search 'Tropicão'

Cut video based on multiple words \(returns specific use of word based on cue tags\)

    videogrep --input "./video.mkv" --search 'para|amanhã|já|pobre|é|cachorro' -vtt -st word
