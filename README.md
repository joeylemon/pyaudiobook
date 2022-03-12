# pyaudiobook

A Python script to apply metadata to audiobook directories, including applying cover art images to each file.

## Usage
```sh
> python pyaudiobook.py --help
usage: pyaudiobook.py [-h] [--cover COVER] [--author AUTHOR] [--title TITLE] dir

Apply cover art to audio book files

positional arguments:
  dir              the directory containing audio files

optional arguments:
  -h, --help       show this help message and exit
  --cover COVER    specify the cover art file
  --author AUTHOR  specify the book author
  --title TITLE    specify the book title
```

For example, take the below directory structure containing the chapters/tracks of an audiobook:

```
Book 07 - Harry Potter and the Deathly Hallows
├── Chapter 01 - The Dark Lord Ascending.mp3
├── Chapter 02 - In Memoriam.mp3
├── Chapter 03 - The Dursleys Departing.mp3
├── Chapter 04 - The Seven Potters.mp3
├── Chapter 05 - Fallen Warrior.mp3
├── Chapter 06 - The Goul in Pajamas.mp3
├── Chapter 07 - The Will of Albus Dumbledore.mp3
├── Chapter 08 - The Wedding.mp3
├── Chapter 09 - A Place to Hide.mp3
├── Chapter 10 - Kreacher's Tale.mp3
├── ...
```

Running the below command will apply the given cover.jpg image as the cover art to each chapter in the directory:
```sh
> python pyaudiobook.py "~/Desktop/Book 07 - Harry Potter and the Deathly Hallows" --cover "~/Desktop/cover.jpg"
```

## Installation

This script requires [Python3](https://www.python.org/downloads/). First, clone this repository and initialize a virtual Python environment.
```sh
> git clone https://github.com/joeylemon/pyaudiobook.git
> cd pyaudiobook
> python -m venv venv
> source venv/bin/activate
```

Then, install the dependencies.
```sh
> pip install -r requirements.txt
```

Now, you can run the program.
```sh
> python pyaudiobook.py --help
```