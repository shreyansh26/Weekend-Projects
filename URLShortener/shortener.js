var firebase = require('firebase');
const r = require('convert-radix64');

var config = {
    apiKey: "AIzaSyDvKUSBHzQAOPq14DsXm_yJpxwWLDi59Z4",
    authDomain: "url-shortener-afca5.firebaseapp.com",
    databaseURL: "https://url-shortener-afca5.firebaseio.com",
    storageBucket: "url-shortener-afca5.appspot.com",
};

firebase.initializeApp(config);

const hasha = require('hasha');
const hashMap = {};

module.exports = {
  shorten: function (url) {
    hash = hasha(url, {encoding: 'base64', algorithm: 'md5'});
    hash = hash.slice(0, 4);  // For 4 character shortened URL
    hash = hash.replace('/', '-');
    hash = hash.replace('+', '_');
    hashMap[hash] = url;
    writeUserData(url, r.from64(hash), hash);

    return hash;
  },

  expand: function (shortcode) {
    var ref = firebase.database().ref('/'+shortcode);
    ref.once('child_added').then(function (snapshot) {
      let username = snapshot.val().url;
      console.log("converted value =  "+username);
      return hashMap[shortcode];
    });
  }
};

function writeUserData(url, shortcode, code) {
  console.log('writedata');
  firebase.database().ref('/'+shortcode).set({
    code: code,
    url: url
  });
}
