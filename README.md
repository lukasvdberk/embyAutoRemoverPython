# About
About a script to remove movies/series that are played on my emby server.

# Installation
Clone repo and install pipenv then in the directory run.

Edit the .example-env file with your configuration and change the name to .env. (Emby key can be retrieved from the settings web page on your server settings -> api keys)

To install dependencies for this project:
```bash
pipenv install
```

And then run remove.py with 
```
pipenv shell && python remove.py
```

You can make this a cronjob on Linux so this runs everyday for example.