const express = require('express');
const bodyParser = require('body-parser');
const app = express();

const shortener = require('./shortener');
const port = 8080;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("static"));

app.get('/:shortcode', (req, res) => {
  shortener.expand(req.params.shortcode)
    .then((url) => {
      //console.log(url);
      res.redirect(url);
    })
    .catch((error) => {

    });
});

app.post('/api/v1/shorten', (req, res) => {
    let url = req.body.url;
    let shortcode = shortener.shorten(url);
    res.send(shortcode);
});

app.get('/api/v1/expand/:shortcode', (req, res) => {
    let shortcode = req.body.shortcode;
    let url = url.expand(shortcode);
    res.send(url);
});

app.listen(port, function() {
  console.log('Listening on port '+ port);
});
