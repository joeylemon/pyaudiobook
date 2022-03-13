# pyaudiobook

A Python script to apply metadata to audiobook directories, including applying cover art images to each file.

<p align="center"><img src="https://user-images.githubusercontent.com/8845512/158066173-042030e7-7e5f-4024-892e-eab01e53bb3c.png" /></p>

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

Running the below command will apply the appropriate metadata to each mp3 file in the directory:
```sh
> python pyaudiobook.py "~/Desktop/Book 07 - Harry Potter and the Deathly Hallows" \
  --cover "~/Desktop/cover.jpg" \
  --author "J.K. Rowling" \
  --title "Harry Potter and the Deathly Hallows"
```

You must set the title property if you wish for each of the audiobook files to fall under the same audiobook in many popular audiobook programs.

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
