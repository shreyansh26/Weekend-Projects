const puppeteer = require('puppeteer');
const CREDS = require('./creds');
const mongoose = require('mongoose');
const User = require('./models/user');

async function run() {
  const browser = await puppeteer.launch({
    headless: false           // for debugging (don't use later)
  });
  const page = await browser.newPage();

  await page.goto('https://github.com/login');
  await page.screenshot({ path: 'screenshots/github.png' });

  const USERNAME_SELECTOR = '#login_field';
  const PASSWORD_SELECTOR = '#password';
  const BUTTON_SELECTOR = '#login > form > div.auth-form-body.mt-3 > input.btn.btn-primary.btn-block';

  await page.click(USERNAME_SELECTOR);
  await page.keyboard.type(CREDS.username);

  await page.click(PASSWORD_SELECTOR);
  await page.keyboard.type(CREDS.password);
  await page.screenshot({ path: 'screenshots/github_creds.png' });

  await page.click(BUTTON_SELECTOR);

  await page.waitForNavigation();

  const userToSearch = 'shreyansh'
  const searchUrl = `https://github.com/search?q=${userToSearch}&type=Users&utf8=%E2%9C%93`;

  await page.goto(searchUrl);
  await page.waitFor(2*1000);
  await page.screenshot({ path: 'screenshots/github_search.png' });

  const LIST_USERNAME_SELECTOR = '#user_search_results > div.user-list > div:nth-child(INDEX) > div.d-flex > div > a'
  const LIST_EMAIL_SELECTOR = '#user_search_results > div.user-list > div:nth-child(INDEX) > div.d-flex > div > ul > li:nth-child(2) > a'
  const LENGTH_SELECTOR_CLASS = 'user-list-item';

  let numPages = await getNumPages(page);

  console.log('NumPages: ', numPages);

  for(let h=1; h<=numPages; h++) {
    let pageUrl = searchUrl + '&p=' + h;
    await page.goto(pageUrl);

    let listLength = await page.evaluate((sel) => {
      return document.getElementsByClassName(sel).length;
    }, LENGTH_SELECTOR_CLASS);

    for(let i=1; i<=listLength; i++) {
      // change the index to the next child
      let usernameSelector = LIST_USERNAME_SELECTOR.replace('INDEX', i);
      let emailSelector = LIST_EMAIL_SELECTOR.replace("INDEX", i);

      let username = await page.evaluate((sel) => {
        return document.querySelector(sel).getAttribute('href').replace('/', '');
      }, usernameSelector);

      let email = await page.evaluate((sel) => {
          let element = document.querySelector(sel);
          return element ? element.innerHTML: null;
      }, emailSelector);

      // not all users have emails visible
      if (!email)
        continue;
      console.log(username, ' -> ', email);

    // Save to DB
    upsertUser({
      username: username,
      email: email,
      dataCrawled: new Date()
    });
  }
}

  browser.close();
}

async function getNumPages(page) {
  const NUM_USER_SELECTOR = '#js-pjax-container > div.container > div > div.column.three-fourths.codesearch-results.pr-6 > div.d-flex.flex-justify-between.border-bottom.pb-3 > h3';

  let inner = await page.evaluate((sel) => {
    // format is: "69,803 users"
    let html = document.querySelector(sel).innerHTML;
    return html.replace(',', '').replace('users', '').trim();

  }, NUM_USER_SELECTOR);

  let numUsers = parseInt(inner);
  console.log('numUsers: ', numUsers);

  let numPages = Math.ceil(numUsers/10);
  return numPages;
}

// Save to MongoDB
function upsertUser(userObj) {
  const DB_URL = 'mongodb://localhost/shreyansh26';

  if (mongoose.connection.readyState == 0){
    mongoose.connect(DB_URL);
  }

  // if the email exists, update it else insert it
  let conditions = { email: userObj.email };
  let options = { upsert: true, new: true, setDefaultsOnInsert: true };

  User.findOneAndUpdate(conditions, userObj, options, (err, result) => {
    if(err)
      throw err;
  });
}

run();
