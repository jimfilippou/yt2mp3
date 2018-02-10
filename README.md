# υt2mp3

## Table of contents

* [Synopsis](#synopsis)
* [Prerequisites](#prerequisites)
* [Installing](#installation)
* [Documentation](#documentation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Testing](#testing)
* [License](#license)
* [Authors](#authors)

<a id="synopsis"></a>
## Synopsis

yt2mp3 is a python CLI for downloading music from youtube.

<a id="prerequisites"></a>
## Prerequisites

You'll need to have Python 2.x installed. The rest of the requirements should be handled by the installation script.

<a id="installation"></a>
## Installing

You can run the app straight from the project's root directory without installing anything by running `app.py`. You'll need the dependencies, however, so before you run the app, run this command from that directory:

```
python setup.py -v -n
```

If that doesn't work and the app crashes because it can't find a module it needs, you should install the app as a library.

To use the app as a library, you can install it by running this command from the project's root directory:

```
python setup.py install
```

<a id="documentation"></a>
## Documentation

There is no documentation yet :)

<a id="usage"></a>
## Usage

To run the app, start a command prompt, change the current working directory to the project directory, and run this command:

```
python app.py
```

The app will give you the command prompt

```
(<yt2mp3> -> )
```

To see a list of the app's commands, type `help`.

To see the details of a command, type `help <command>`. For example, for more information on the `help` command, type `help help`.

To quit the app, use the command `q`.

<a id="contributing"></a>
## Contributing

There are no style guides whatsoever, make a pull request or open an issue anytime for pretty much anything.

<a id="testing"></a>
## Testing

From a command prompt in the project directory, run the command `nose2` to automatically run all the tests.

<a id="license"></a>
## License

This project uses the MIT license. See the file `LICENSE.md` for details.

<a id="authors"></a>
## Authors

* Jim Filippou (jimfilippou@hotmail.gr) - original author
