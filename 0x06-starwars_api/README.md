Setup Instructions
Install Node 10
bash
Copy code
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Install Semistandard
bash
Copy code
$ sudo npm install semistandard --global
Install Request Module
bash
Copy code
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules


Write a script that prints all characters of a Star Wars movie, using the Star Wars API. The script takes a movie ID as the first argument and prints character names in the order they appear in the "characters" list from the /films/ endpoint.

Positional Argument: Movie ID (e.g., 3 = "Return of the Jedi")
Requirements:
Use the Star Wars API.
Use the request module to make API calls.