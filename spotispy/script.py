import os
from subprocess import PIPE, run 

PLAYLISTS = 'playlists.txt'

with open(PLAYLISTS) as f:
    for line in f:

        # Remove tracking artifacts (fat url)
        line = line.split('?si=')[0].strip()

        # Visit link and save as variable title
        title = run(['curl', '-s', line], stdout=PIPE).stdout.decode('utf-8')
        title = title.split('title')[1].split('>')[1].split(' - playlist by')[0]

        # Create folder with title if it does not exist already
        if not os.path.exists(title):
            os.mkdir(title)
        os.chdir(title)

        # Download playlist using spotdl
        run(['spotdl', 'sync', line, '--format', 'flac', '--save-file', f'{title}.sync.spotdl'])
        print(f'Downloaded {title} to {os.getcwd()}')

        # Return to parent directory
        os.chdir('..')


        

