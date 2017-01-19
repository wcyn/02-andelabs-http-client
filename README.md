# Day 2 - HTTP Command Line Application

This repo contains Python3 code that performs a simple GET and POST to a public [JSONPlaceholder API](https://jsonplaceholder.typicode.com/).

Some [__Test Cases__](#running-the-tests) are provided as well.


## Getting Started
These instructions should help you run the code on your machine.

### Prerequisites
The code is written in Python3.

### Libraries Used
- requests (in-built module)

Used by simply importing the module:

```
import requests
```

### Installing

Clone the repository from GitHub:
```
$ git clone https://github.com/wcyn/02-andelabs-http-client
```

### Running the program
Change Directory into the project folder
```
$ cd 02-andelabs-http-client
```

Run the python file with the code by typing:
```
$ python http_and_web.py
```

## Running the Tests
There are 4 tests in the Python test file.
In order to run these tests, use the following command while in the project folder:

```
$ python test_http_and_web.py
```

### The test cases
1. `def test_get_returns_nothing_to_show_out_of_range(self)` : should return '* Nothing to show *' if input is not within 1 and 100 

2. `def test_get_raises_value_error_for_non_int(self)` : should raise Value Error if input is not integer

3. `def test_correct_get_returns_response_object(self)` : A correct get request should return Response object

4. `def test_correct_post_returns_response_object(self)` : A correct post request should return Response object
