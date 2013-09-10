#!/usr/bin/python

import sys
import os
import json
import urllib2
from collections import namedtuple

def has_date(item):
    try:
        if item['date']['#text']:
            return item['date']['#text']
    except Exception, e:
        return None

def is_now_playing(item):
    try:
        if item['@attr']['nowplaying'] == 'true':
            return True
    except Exception, e:
        return False

def main():
    # define the Track namedtuple for storing last.fm tracks
    Track = namedtuple('Track', ['artist', 'album', 'song', 'date', 'now_playing'])
    args = sys.argv[1:]
    if args:
        user = args[0]
    else:
        user = 'macklinu'
    api_key = '670e6afbc4541d7add99db2238d4abf9'
    url = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=%s&api_key=%s&limit=10&format=json' % (user, api_key)
    # load the raw JSON via HTTP GET request
    j = json.load(urllib2.urlopen(url))
    all_tracks = []  # where we will store all da tracks
    for item in j['recenttracks']['track']:
        t = Track(artist=item['artist']['#text'],
                  album=item['album']['#text'],
                  song=item['name'],
                  date=has_date(item),
                  now_playing=is_now_playing(item)
                 )
        all_tracks.append(t)  # add that track to the tracks!

    # printing it all to the console
    height, width = os.popen('stty size', 'r').read().split()  # via http://stackoverflow.com/a/943921/1798762
    break_line = '%s' % ('-'*int(width))
    print break_line
    for i in all_tracks:
        if i.now_playing:
            s = '%s - %s (%s)' % (i.artist, i.song, i.album)
            top =  '%s%s%s' % ('*'*30, 'NOW PLAYING', '*'*30)
            bottom = '%s' % ('*'*len(top))
            print '%s\n%s\n%s' % (top, s, bottom)
        else:
            s = '%s: %s - %s (%s)' % (i.date, i.artist, i.song, i.album)
            print s
    print break_line

if __name__ == '__main__':
    main()