np
===

[\#np](http://tagdef.com/np) (now playing) : Last.fm + Python

This quick command-line tool allows me to see what song is currently playing, as well as the last 10 played tracks.

## Idea

My music is streaming from media PC and playing on speakers in my living room. I like to listen to music on random and don't have visual access to what track is currently playing. Since my PC scrobbles every track, using Last.fm to find this information seemed like a simple choice.

## Usage

+ First, download `np.py`. Then edit two parts of the file:
    + `API_KEY`: your Last.fm API key, which can be created [here](http://www.last.fm/api/account/create)
    + `USERNAME`: your Last.fm username (mine is [macklinu](http://www.last.fm/user/macklinu))
+ Make the script executable: `chmod u+x np.py`
+ Move the script: `mv np.py /usr/local/bin/np`
+ Use it:
    + `np` - displays the currently playing tracks for the default user (specified in the script)  
    + `np <username>` displays the currently playing tracks for the user passed in as an argument

## Output

Sample output of the script

#### Playing

```
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
******************************NOW PLAYING******************************
Cerulean Tapes - Nothing Nowhere ()
***********************************************************************
11 Sep 2013, 13:40: Kyle Hall - Body of Water (Must See EP)
11 Sep 2013, 13:33: Kyle Hall - Osc_2 (Must See EP)
11 Sep 2013, 13:26: Kyle Hall - Ghosten (Must See EP)
11 Sep 2013, 13:20: Kyle Hall - Must See (Must See EP)
10 Sep 2013, 22:53: Toro y Moi - Still Sound (Underneath the Pine)
10 Sep 2013, 22:42: Kyle Bobby Dunn - Touhy’s Theme (Ways Of Meaning)
10 Sep 2013, 22:27: Kyle Bobby Dunn - Movement for the Completely Fucked (Ways Of Meaning)
10 Sep 2013, 22:23: Kyle Bobby Dunn - New Pures (Ways Of Meaning)
10 Sep 2013, 22:16: Kyle Bobby Dunn - Canyon Meadows (Ways Of Meaning)
10 Sep 2013, 22:10: Kyle Bobby Dunn - Statuit (Ways Of Meaning)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

#### Not Playing

```
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
11 Sep 2013, 13:40: Kyle Hall - Body of Water (Must See EP)
11 Sep 2013, 13:33: Kyle Hall - Osc_2 (Must See EP)
11 Sep 2013, 13:26: Kyle Hall - Ghosten (Must See EP)
11 Sep 2013, 13:20: Kyle Hall - Must See (Must See EP)
10 Sep 2013, 22:53: Toro y Moi - Still Sound (Underneath the Pine)
10 Sep 2013, 22:42: Kyle Bobby Dunn - Touhy’s Theme (Ways Of Meaning)
10 Sep 2013, 22:27: Kyle Bobby Dunn - Movement for the Completely Fucked (Ways Of Meaning)
10 Sep 2013, 22:23: Kyle Bobby Dunn - New Pures (Ways Of Meaning)
10 Sep 2013, 22:16: Kyle Bobby Dunn - Canyon Meadows (Ways Of Meaning)
10 Sep 2013, 22:10: Kyle Bobby Dunn - Statuit (Ways Of Meaning)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

## Updates

+ Cleaning up code based on if album, artist information is present + more
+ Use a [Python module](https://code.google.com/p/python-lastfm/) for the Last.fm API
+ Add command-line options and documentation
    + Tweet the current track: `np -t` or `np --tweet` 
