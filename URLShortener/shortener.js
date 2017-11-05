var firebase = require('firebase');
const r = require('convert-radix64');
const hasha = require('hasha');

var config = {
    apiKey: "",
    authDomain: "",
    databaseURL: "",
    storageBucket: "",
};

firebase.initializeApp(config);
const hashMap = {};

module.exports = {
  shorten: (url) => {
    hash = hasha(url, {encoding: 'base64', algorithm: 'md5'});
    hash = hash.slice(0, 4);  // For 4 character shortened URL
    hash = hash.replace('/', '-');
    hash = hash.replace('+', '_');
    hashMap[hash] = url;
    writeUserData(url, r.from64(hash), hash);

    return hash;
  },

  expand: (shortcode) => {
    return new Promise(function(resolve, reject) {
      if (shortcode === undefined) {
        reject(null);
      }
      var ref = firebase.database().ref('/'+r.from64(shortcode));
      ref.once('value').then(function(snapshot) {
        val = snapshot.val();
        if(val) {
          let url = val.url;
          resolve(url);
        } else {
          resolve(hashMap[shortcode]);
        }
      });
    });
  }
};

function writeUserData(url, shortcode, code) {
  firebase.database().ref('/'+shortcode).set({
    code: code,
    url: url
  });
}
