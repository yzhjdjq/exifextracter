from typing import List, Dict
from os import listdir, rename
from os.path import isfile, join
import exifread
import ffmpeg

def ReadExifFromImage( filepath: str ) -> Dict:
    tags = dict()
    with open( filepath, 'rb' ) as f:
        tags = exifread.process_file( f )
    return tags

def RenameImageFile( file: str ) -> str:
    tags: Dict = ReadExifFromImage( file )
    if 'EXIF DateTimeOriginal' not in tags:
        return ''
    datetime: List[str] = tags['EXIF DateTimeOriginal'].values.replace( ' ', '_' )
    return datetime

def RenameVideoFile( file: str ) -> str:
    tags: Dict[str] = ffmpeg.probe( file )['streams'][0]['tags']
    datetime: str = tags['creation_time'].split( '.' )[0].replace( 'T', '_' )
    return datetime

if __name__ == '__main__':
    files: List[str] = [f for f in listdir('.') if isfile(join('.', f))]
    for file in files:
        datetime: str = ''
        mediatype: str = ''
        if ( '.jpg' in file.lower() or '.jpeg' in file.lower() ) and 'IMG' not in file:
            datetime = RenameImageFile( file )
            mediatype = 'IMG'
        if ( '.mov' in file.lower() or 'mp4' in file.lower() ) and 'VID' not in file:
            datetime = RenameVideoFile( file )
            mediatype = 'VID'
        if datetime == '' or mediatype == '':
            continue

        splitDatetime = datetime.split( ':' )
        datetime = ''.join( splitDatetime )
        originalFilename: List[str] = file.split( '.' )
        newFilename: str = originalFilename[0] + ' '
        newFilename += mediatype + '_' + datetime
        newFilename += '.' + originalFilename[1]
        rename( file, newFilename )
        print( file, newFilename, sep=' -> ', end=' Is success...\r\n')
