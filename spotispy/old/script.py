#~!/usr/bin/env python3

from subprocess import run
from tkinter import N 
import yaml, os
# import pdb; pdb.set_trace()

OPTIONS_F = 'data/options'
PLAYLISTS_D = 'playlists'
M3U_DIR = 'data/m3us/'

MUSIC_DIR = 'playlists'


# TODO: move to separate maintained file: json?
# TODO: automatically remove queries from html strings and save to file.

playlists = '''https://open.spotify.com/playlist/2uoWjRviBkrFoEhxOk97sX - house
    https://open.spotify.com/playlist/419eC6mQ44YpMlMXF8a8Bi - sobriety
    https://open.spotify.com/playlist/094Mcu4G0UN1vcFaqamqaw - rock trip
    https://open.spotify.com/playlist/37i9dQZF1EJvWQurTyZry7 - roble
    https://open.spotify.com/playlist/5GV3xR63wCz8pMV5Q66LVG - woo
    https://open.spotify.com/playlist/6kAVAkqNg8RJyfBhP6c6eJ - psychedelicate
    https://open.spotify.com/playlist/6mTk5l5UapuJHy4vavgi22 - rap recap
    https://open.spotify.com/playlist/5juS18bdrpccYPTFoXy5Gv - mix vocals
    https://open.spotify.com/playlist/2z4zWkRgpadOXiFtH8WnAZ - techno darko
    https://open.spotify.com/playlist/0afvsXSN2qY7pTXHjKPvca - 🌁 psyco atmo
    https://open.spotify.com/playlist/4ukGYSdkJ8UOrTenR4PzQy - dj vocals'''

def setup():
    '''
    Prepares application for fetching.
    '''
    with open(OPTIONS_F + '.yaml') as f:
        options = yaml.safe_load(f)

        # # if key 'path' in options is not set, prompt user to input it
        # if not options['path']:
        #     options['path'] = input('Enter path to music directory: ')
        #     with open(OPTIONS_F + '.yaml', 'w') as f:
        #         yaml.dump(options, f)

        # # if options['path'] does not exist, alert user
        # if not os.path.exists(options['path']):

    # set current directory to `playlists` using absolute path
    path = os.path.join(os.path.abspath(options['path']), PLAYLISTS_D)
    try: os.chdir(path) 
    except FileNotFoundError: 
        print(f'No playlists directory found at {path}.\nCreating new directory.')
        os.mkdir(path)
        os.chdir(path)


    # TODO: Fetch m3us and only fetch if they have updated. 


def fetch():
    '''
    Fetches above playlists into the `playlists` directory. 
    '''
    pl_urls = {url.split('-')[1].strip(): url.split('-')[0].strip() for url in playlists.split('\n')}

    # fetch playlists
    for pl, url in pl_urls.items():

        print(f'fetching {pl}')

        run(['mkdir', pl])
        os.chdir(pl)

        # Fetch playlist and print warning if error occurs
        errors = []
        try: 
            run(['spotdl', 'sync', url, '--format', 'flac', '--save-file', f'{pl}.sync.spotdl']) 
        except Exception as e:
            errors.append(f'Error fetching {pl}: {url}, please check if it is public.')
            print(errors[-1])

        os.chdir('..')

    print(error for error in errors)



def main():
    # pdb.set_trace()

    # try:

    setup()
    fetch()

    # except Exception as e:
    #     print(f'{type(e)} {e}')

if __name__ == '__main__':
    # pdb.set_trace()
    main()
