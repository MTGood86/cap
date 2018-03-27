# Overview:
My capstone project will be a web based MIDI Sequencer.
Canetis

## Functionality:

I plan to have a grid format presentation with the y axis representing octave (currently planned for octaves 3-5) and the x axis being time. Each square in the grid will represent a whole note with options for the user to change tempo (represented by a vertical bar moving from left to right) and note lengths with two clicks that represent start and stop locations and an option for color themes. User will be able to have their track play/loop while adding notes.

In a later version I will add more octaves, either by increasing the height of the track or by adding a vertical scroll bar to access higher or lower octaves..

[wireframe] (https://wireframe.cc/P8hzDF)

I'd like to implement an option to save produced tracks as MIDIs. Currently only plans for just a synthesized tone using tone js, but would like to add instruments as options as well.

## Data Model:

Data that will need to be stored for the application will include: note frequency, length of note, position of note in time and user's track. If I'm able to add the use of instruments I will need to store that information as well.

## Schedule:

Most of the time will be devoted to getting the storage of information correct so the first two weeks will likely be allocated to writing models and views while the final week will be for designing the visual representation aspect. Post project work would include adding instruments and refining user experience.
