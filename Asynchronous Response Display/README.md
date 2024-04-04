# Asynchronous Response Display

Just out of curiosity, I wanted to know how to make a webapp to show outputs from two different APIs asynchronously i.e. irrespective of when the outputs are returned from the API. A dummy POC, but now I get it.

## Run the app
```
chmod +x run.sh
NUM_WORKERS=2 ./run.sh
```

## Open the HTML script or use Python server
```
python -m http.server 5050
```

Head to `localhost:5050`.
