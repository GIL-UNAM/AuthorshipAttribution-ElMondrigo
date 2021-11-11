# AuthorshipAttribution-ElMondrigo

## Prerequisites

***
> __Below we assume the working directory is the repository root.__

- Using Docker (recommended)
  > Make sure `docker` is installed. (If not go to: https://docs.docker.com/engine/install/)

    ```sh
    # Create the docker image
    docker build -t mondrigo:iimas .
    # Run the docker image
    docker run -it mondrigo:iimas bash
    ```
  
- Using pipenv

  > Make sure `pipenv` is installed. (If not, simply run: `pip install pipenv`.)
  > It is necessary to have installed **Java JDK** and declare the **JAVAHOME** environment variable with the path of the java binaries.

    ```sh
    # Activate the virtual environment
    pipenv shell
    # Install the dependencies
    pipenv install -r requirements.txt
    ```
