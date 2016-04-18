# Example Node.js Server

This server presents a simple page that can take the user through the Authentication Code Flow and show them their roster.

## Setup

1. Install `node` through your package manager of choice, or from https://nodejs.org/en/
- Download/Clone this repository and navigate to the `node_server` folder
- Run `npm i`
- Create an application through the [Tanda Developer Portal](https://my.tanda.co/api/oauth/applications)
  - Set the Redirect URI to be `http://localhost:6789/callback`
- Edit `index.js` and replace `YOUR_APPLICATION_ID` and `YOUR_APPLICATION_SECRET` with your application id and secret

## Running

Simply run `node index.js` to start the server.
