# Contribution guidelines

- Jupyter-book supports [multiple content types](https://jupyterbook.org/file-types/index.html). Their flavour of Markdown is preferred.
- Please start each sentence on a new line in the documentation. This allows
  for better diffs and pull requests.

## Building docs locally

The documentation currently uses [Jupyter-book](https://jupyterbook.org/).
To build the documentation locally, to test before opening Pull Requests for example,
a helper script `./build-helper.sh` is provided which automates the setup and build process.

Run `./build-helper.sh -h` to see all available options.

The most commonly used options are:

- `-c`: create a new virtual environment (in `.venv`) and install the required packages
- `-b`: build the book, creating the HTML files in `./source/_build/html`
- `-w`: watch the `source` directory for changes and rebuild automatically (requires `inotifywait`)
- `-p`: publish the built book to GitHub pages (requires commit access to the repository)
- `-s`: build the book as a single page HTML file
- `-m`: build the book as a single page HTML file and convert it to a single Markdown file
- `-X`: clean the book build files

### Manual setup (alternative to `-c`)

If you prefer to set up the environment manually, you can use a virtual environment:

```
  # Create a new virtual environment
  $ python3 -m venv ./.venv
  # Activate the virtual environment
  $ source .venv/bin/activate
  # Install the necessary Python packages
  $ pip install -r requirements-book.txt
  # Build the docs
  $ jupyter-book build ./source
  # This will create the HTML files in ./source/_build/html
```

To deactivate the virtual environment:

```
  $ deactivate
```

More information on Python virtual environments can be found in the Python documentation [here](https://docs.python.org/3.9/library/venv.html).

The build helper script will automatically use [uv](https://github.com/astral-sh/uv)
to create the virtual environment if it is available on your system, falling back
to `python3 -m venv` otherwise.

## Publishing the book

The book is published using GitHub pages, using the `ghp-import` tool.

```
  # Use the helper script to publish
  $ ./build-helper.sh -p
```

This will import the HTML files built by `jupyter-book` to the `gh-pages` branch.
More information on this can be found in the [official documentation](https://jupyterbook.org/publish/gh-pages.html).
