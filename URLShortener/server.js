const express = require('express');
const bodyParser = require('body-parser');
const app = express();

const shortener = require('./shortener');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("static"));

app.get('/:shortcode', (req, res) => {
  let url = shortener.expand(req.params.shortcode);
  console.log(url);
  res.redirect(url);
});

app.post('/api/v1/shorten', function (req, res) {
    let url = req.body.url;
    let shortcode = shortener.shorten(url);
    res.send(shortcode);
    console.log(shortcode);
});

app.get('/api/v1/expand/:shortcode', function (req, res) {
    let shortcode = req.body.shortcode;
    console.log(shortcode);
    let url = url.expand(shortcode);
    res.send(url);
});

app.listen(8080, function() {
  console.log('Listening on port 8080');
});
