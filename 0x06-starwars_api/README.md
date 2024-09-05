Star Wars API

Setup Instructions
    Install Node 10
Copy code
    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
Install Semistandard
Copy code
    $ sudo npm install semistandard --global
Install Request Module
Copy code
    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules


0. Star Wars Characters
    0-starwars_characters.js contains a script that prints all characters of a Star Wars movie with the following requirements:
    The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”.
    Display one character name per line in the same order as the “characters” list in the /films/ endpoint.
    You must use the Star wars API.
    You must use the request module.
