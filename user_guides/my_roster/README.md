It's easy to use the Tanda API to retrieve all rosters for someone.

First, have the user [authenticate](https://github.com/TandaHQ/api-v2-code-samples/tree/master/user_guides/getting_started) and get an access token. You'll need the `me` and `roster` scopes for this guide.

Next, make a call to [`/api/v2/users/me`](https://my.tanda.co/api/v2/documentation#general-current-user-get). This will return you information about the currently authenticated user. One of the fields will be `user_ids`, an array of numbers. You should use this for the next step. Note that this list is unlikely to change regularly so you can generally cache it somewhere. However, it *will* change if the person in question starts work at another Tanda organisation. If the `user_ids` field is not returned by your API call, you can fall back to the `id` field which will return a single ID.

Finally, make a call to [`/api/v2/schedules`](https://my.tanda.co/api/v2/documentation#schedules-schedules-get-1). You'll need to provide `user_ids` (from the previous step), and `from` and `to` dates. The API will return schedules (shifts on rosters) between those dates. Note that the `user_ids` should be a comma separated list. For example:

```
https://my.tanda.co/api/v2/schedules?from=2016-11-08&to=2016-11-22&user_ids=1,2,123456
```

If you want to also include the names of the team and location being worked in for each schedule, include the `include_names` parameter in the URL.

```
https://my.tanda.co/api/v2/schedules?from=2016-11-08&to=2016-11-22&user_ids=1,2,123456&include_names=true
```
