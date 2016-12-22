# @author : coenni
# @date   : Dec 22 2016
# @brief  : addding playlist download to youtube downloader.

import urllib, urllib.parse, urllib.request
import json, pprint, codecs, sys
from urllib import request
from youtube_downloader import VideoDownloader

def main():
    print("\n--------------------------")
    print (" Youtube Video Downloader")
    print ("--------------------------\n")

    try:
        searchUrl = 'https://www.googleapis.com/youtube/v3/playlistItems'

        try:
            print("enter playlistId: ")
            playlistId = input()
        except ValueError:
            return 1

        params = {'maxResults': 50, 'key': 'YOUR_KEY', 'part': 'snippet',
                  'playlistId': playlistId}
        url = '%s?%s' % (searchUrl, urllib.parse.urlencode(params))
        response = urllib.request.urlopen(url)
        reader = codecs.getreader("utf-8")
        data = json.load(reader(response))

        try:
            print("Please select the resolution level of the video, ")
            VideoDownloader.resolution = int(
                input("1 - %d, highest to lowest, q to quit: " % (4,)))
        except ValueError:
            return 1

        while 1 > VideoDownloader.resolution > 4:
            print("Please enter the right number.")
            VideoDownloader.resolution = int(
                input("Please select the resolution of the video( 1-" + str(4) + ", highest to lowest): "))
            VideoDownloader.resolution -= 1  # get the index


        for item in data['items']:
            print('videoid:' + item['snippet']['resourceId']['videoId'])
            v_url = "https://www.youtube.com/get_video_info?video_id=" + item['snippet']['resourceId']['videoId']
            try:
                resp = request.urlopen(v_url)
            except urllib.error.HTTPError as e:
                print("Cannot open the page.")
                print(e.code)
                raise (e)
            ok = VideoDownloader.get_vid(resp)
        pprint.pprint(data)
    except :
        print("Unexpected error:", sys.exc_info()[0])
    print("\n Done.")

if __name__ == '__main__':
    main()