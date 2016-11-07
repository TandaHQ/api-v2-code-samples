It's easy to use the Tanda API to retrieve all rosters for someone.

First, have the user [authenticate](https://github.com/TandaHQ/api-v2-code-samples/tree/master/user_guides/getting_started) and get an access token.

Next, make a call to [`/api/v2/users/me`](https://my.tanda.co/api/v2/documentation#general-current-user-get). This will return you information about the currently authenticated user. Here you can see their name, organisation name, etc. The main thing you want here is the user's `id`. This ID is permanent so you can store it somewhere alongside the access token; you don't need to query this every time you make a call.

Finally, make a call to [`/api/v2/schedules`](https://my.tanda.co/api/v2/documentation#schedules-schedules-get-1). You'll need to provide `user_ids` (from the previous step), and `from` and `to` dates. The API will return schedules (shifts on rosters) between those dates. For example:

```
https://my.tanda.co/api/v2/schedules?from=2016-11-08&to=2016-11-22&user_ids=123456
```

If you want to also include the names of the team being worked in for each schedule, include the `include_names` parameter in the URL.

```
https://my.tanda.co/api/v2/schedules?from=2016-11-08&to=2016-11-22&user_ids=123456&include_names=true
```