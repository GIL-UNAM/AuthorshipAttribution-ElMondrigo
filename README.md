# AuthorshipAttribution-ElMondrigo

## Data

***

The data folder contains two folders that are used for the móndrigo experiments, the first called "corpus" is used by Samuel Ramos's experiments, check his work in the "presentations" folder; and the second called "SVC" is used for Brian Sánchez's experiment

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

## Run

***

| Args           | Description                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------|
| `burrows`      | Measure distances of styles with the Delta method                                                          |
| `clustering`   | unsupervised learning algorithm using K-means                                                              |
| `kilgariff`    | Distance between texts using Kilgariff's method                                                            |
| `mendenhall`   | method based on the average length of the words used by the author in his writings, represented by a curve |
| `tagger`       | Parts of Speech Model                                                                                      |
| `svm`          | Authorship prediction table based on SVM and stylometric markers                                           |
| `svm_Chimal`   | Authorship prediction table based on SVM and stylometric markers including Alberto Chimal                  |

> __Below we assume the working directory is the repository root.__

For example, if you want to run the burrows and kilgariff experiments:
  ```bash
  python main.py burrows kilgariff
  ```