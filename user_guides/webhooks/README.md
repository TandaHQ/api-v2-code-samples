This guide will step you through connecting Tanda [webhooks](https://my.tanda.co/api/v2/documentation#webhooks) to another system using [Zapier](https://zapier.com). There is no programming knowledge required!

## 1. Create zap

In Zapier, go to your [dashboard](https://zapier.com/app/dashboard) and click **Make A Zap!**. Choose the following options as they come up:

- Trigger app: `Webhooks by Zapier`
- Trigger: `Catch Hook`
- Pick off child key: *skip this step*

Take a note of the URL that Zapier gives you. It will look like `https://hooks.zapier.com/hooks/catch/123456/abcdef/`

Keep this open - we'll come back to it later.

## 2. Add to Tanda

In another tab in your browser, go to your [Webhooks portal in Tanda Developers](https://my.tanda.co/api/webhooks) and click **New Webhook**.

Use the URL that you got from Zapier in step 1. You won't need a security token. For the topics, choose any of the [events from the API docs](https://my.tanda.co/api/v2/documentation#webhooks) - in this example I'm using `clockin.updated`

Click save when you're done.

## 3. Clock in

Tanda will now send data to Zapier whenever someone clocks in. So you need to make some data get from Tanda to Zapier - do that by going to your time clock and clocking in!

If you don't have a time clock handy, you can go to https://timeclock.tanda.co and set one up just for testing. You can get your access code from https://my.tanda.co/timeclocks/new if you need it.

Back in Zapier, you should be able to now successfully "test this step" and see a webhook event delivered.

## 4. Create spreadsheet

Go to [Google Sheets](https://docs.google.com/spreadsheets/u/0/?tgif=d) and create a new, blank spreadsheet.

Add some headers in the first row - one header per cell. In this example, I'm adding:

- `User ID`
- `Time`
- `Action`

You can see the full list of available fields in the [API docs](https://my.tanda.co/api/v2/documentation#clock-ins-clock-in-get) - webhooks will get the same payload that API responses get, in JSON format.

Give this spreadsheet a memorable name.

## 5. Connect spreadsheet to Zapier

Go back to Zapier, and move on to the next section. For the action app, choose the following options:

- Action app: `Google Sheets`
- Action: `Create Spreadsheet Row`
- Account: *choose your Google Sheets account*
- Set up template: *find the spreadsheet you created in step 4 here - it's usually first in the list if you just created it*

The last bit is just connecting the data sent from Tanda to the headers you've made in the spreadsheet. If you want to add or change spreadsheet headers, use the **Refresh Fields** button down the bottom. It's generally better to add new headers to the right hand side (ie. don't move all columns to the right) otherwise Zapier will mess your columns up.

Click the **Continue** button at the bottom when you're done. You can now do a test - if all worked well, you should see data in your spreadsheet! Turn the Zap on and it will update live as employees clock in.

## 6. Next steps

This is a fairly boring example, but Zapier has [many many other](https://zapier.com/app/explore) integrations that you can now connect to.

Let us know if there are new topics or fields you'd like to see in Tanda. The list of topics we support is in our [API docs](https://my.tanda.co/api/v2/documentation#webhooks) but we are always keen to add more and help you do cool stuff with them!
