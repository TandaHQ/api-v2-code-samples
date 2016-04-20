// ********************** VARIABLES TO MODIFY **********************

var port         = 6789
  , clientId     = "YOUR_APPLICATION_ID"
  , clientSecret = "YOUR_APPLICATION_SECRET"

// *****************************************************************





// ************************** SERVER CODE **************************

var homePage = "http://localhost:" + port
var redirectUri = homePage + "/callback"
var site = "https://my.tanda.co/api"
var scopes = [
  "me",
  "roster"
]

// Usually token information would be stored in a database for a user
var token

// Setting variables once is a lazy man's cache
var userInfo
var rosterInfo

// Setup the requirements and express server
var request = require("request")
var open = require("open")
var express = require("express")
var morgan = require("morgan")
var app = express()
app.set("views", __dirname + "/views")
app.engine("html", require("ejs").renderFile)
app.use(morgan("dev"))

// Setup the OAuth 2 settings
var oauth2 = require("simple-oauth2")({
  clientID: clientId,
  clientSecret: clientSecret,
  site: site,
  tokenPath: "/oauth/token",
  authorizationPath: "/oauth/authorize"
})

// HELPER FUNCTIONS
var makeGetRequestToTanda = function(url, callback) {
  refreshTokenIfNeeded(function() {
    oauth2.api("GET", url, {
      access_token: token.token.access_token
    }, callback)
  })
}

var getUserInfo = function(callback) {
  if (userInfo || !token) {
    callback(userInfo || {})
  } else {
    makeGetRequestToTanda("/v2/users/me", function(err, body) {
      userInfo = body
      callback(userInfo)
    })
  }
}

var getRosterInfo = function(callback) {
  if (rosterInfo || !token) {
    callback(rosterInfo || {})
  } else {
    makeGetRequestToTanda("/v2/rosters/current", function(err, body) {
      rosterInfo = body
      callback(rosterInfo)
    })
  }
}

var refreshTokenIfNeeded = function(callback) {
  if (token.expired()) {
    token.refresh(function(err, result) {
      if (err) {
        console.log("Access Token Error", error.message)
        res.sendStatus(500)
      } else {
        token = result
        callback()
      }
    })
  } else {
    callback()
  }
}

var toState = function(obj) {
  if (!obj) {
    return ""
  }
  return new Buffer(JSON.stringify(obj)).toString("base64") || ""
}

var fromState = function(string) {
  if (!string) {
    return {}
  }
  return JSON.parse(new Buffer(string, "base64").toString("ascii")) || {}
}

// ROUTES
app.get("/authenticate", function(req, res) {
  console.log("--- Getting Token ---")
  res.redirect(oauth2.authCode.authorizeURL({
    redirect_uri: redirectUri,
    scope: scopes.join(" "),
    state: toState({redirect: req.query.redirect})
  }))
})

app.get("/callback", function(req, res) {
  oauth2.authCode.getToken({
    code: req.query.code,
    redirect_uri: redirectUri
  }, function(err, result) {
    if (err) {
      console.log("Access Token Error", error.message)
      res.sendStatus(500)
    } else {
      token = oauth2.accessToken.create(result)

      var redirect = fromState(req.query.state).redirect || "/"
      res.redirect(redirect)
    }
  })
})

app.get("/", function(req, res) {
  if (!token) {
    res.render("index.html")
  } else {
    refreshTokenIfNeeded(function() {
      getUserInfo(function(userInfo) {
        res.render("authed_index.html", {user_info: userInfo})
      })
    })
  }
})

app.get("/roster", function(req, res) {
  if (!token) {
    res.redirect("/authenticate?redirect=" + encodeURIComponent("/roster"))
  } else {
    refreshTokenIfNeeded(function() {
      getRosterInfo(function(rosterInfo) {
        res.render("roster_info.html", {roster_info: rosterInfo})
      })
    })
  }
})

app.listen(port, function() {
  console.log("listening on port: " + port)
  console.log("make sure that " + redirectUri + " is set as a redirect uri for your app")
  open(homePage)
})
