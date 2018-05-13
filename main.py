from urllib.request import urlopen
import json

response = urlopen("https://player.vimeo.com/video/267763406/config?autopause=1&autoplay=1&byline=0&collections=1&context=Vimeo%5CController%5CClipController.main&default_to_hd=1&outro=nothing&portrait=0&share=1&title=0&watch_trailer=0&s=2d73c25a664101d9ac5b702e42db2d7bb295731b_1526276366")
video_json = json.load(response)
print(video_json)

video_url = video_json['request']['files']['progressive'][0]['url']
response = urlopen(video_url)
video = response.read()

f = open('a.mp4', 'wb')
f.write(video)
f.close()