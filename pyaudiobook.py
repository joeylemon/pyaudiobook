import eyed3
import argparse
import mimetypes
import os
import re


def get_arguments() -> argparse.Namespace:
    """ Parse the command-line arguments and validate them. """

    parser = argparse.ArgumentParser(
        description="Apply cover art to audio book files")
    parser.add_argument("dir", help="the directory containing audio files")
    parser.add_argument(
        "--cover", help="specify the cover art file", default="cover.jpg")
    parser.add_argument("--author", help="specify the book author")
    parser.add_argument("--title", help="specify the book title")
    args = parser.parse_args()

    args.dir = os.path.abspath(args.dir)
    if not os.path.exists(args.dir):
        print(f"directory {args.dir} does not exist")
        exit(1)

    args.cover = os.path.join(args.dir, args.cover)
    if not os.path.exists(args.cover):
        print(f"cover art file {args.cover} does not exist")
        exit(1)

    return args


def is_mp3_path(path: str) -> bool:
    """ Check if a file is an MP3. """

    return mimetypes.MimeTypes().guess_type(path)[0] == "audio/mpeg"


def get_track_num(path: str) -> int:
    """ Try to find the track number from an audiofile path. """

    regex = re.search('(?:chapter|track|chp)(?:\s*)(\d+)', path.lower())
    if regex is None:
        raise ValueError('path has no track number')

    return int(regex.group(1))


def apply_metadata_to_file(opts: argparse.Namespace, path: str, cover_data: bytes, cover_mime: str):
    """ Apply metadata to the given audiofile path. """

    audiofile = eyed3.load(path)
    if audiofile.tag is None:
        audiofile.initTag()

    audiofile.tag.images.set(
        eyed3.id3.frames.ImageFrame.FRONT_COVER,
        cover_data, cover_mime)

    audiofile.tag.artist = opts.author
    audiofile.tag.title = opts.title

    # Attempt to set the track number
    try:
        audiofile.tag.track_num = get_track_num(path)
        print("set track num for", path, " to", get_track_num(path))
    except:
        pass

    audiofile.tag.save(version=(2, 4, 0))


def apply_metadata_to_dir(opts: argparse.Namespace):
    """ Parse the directory and apply cover art to all MP3s. """

    files = os.listdir(opts.dir)
    cover_data = open(opts.cover, "rb").read()
    cover_mime = mimetypes.MimeTypes().guess_type(opts.cover)[0]

    for filename in files:
        path = os.path.join(opts.dir, filename)
        if os.path.isfile(path) and is_mp3_path(path):
            apply_metadata_to_file(opts, path, cover_data, cover_mime)


if __name__ == "__main__":
    args = get_arguments()
    apply_metadata_to_dir(args)
