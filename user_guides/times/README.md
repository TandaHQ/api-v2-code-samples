All times in the Tanda API are rendered as [Unix time](https://en.wikipedia.org/wiki/Unix_timestamp). This is done to avoid confusion as not all users are based within the same time zone.

It's possible that rather than a Unix time you will want to present times retrieved from the API in a user's local time zone. This guide describes how to use information from the API to do that.

**1. Getting the time zone**

A user's timezone can be retrieved from the both the [User endpoint](#users-user-get). If you know a user's ID you can make a GET to `/api/v2/users/{id}` - eg. `/api/v2/users/123456`. This will return two fields - `time_zone` (a string) and `utc_offset` (an integer). You should store both of these somewhere, as you can use either to cast times to the user's zone.

A snipped example response:

```
{
  "id": 123456,
  "name": "Lenny Leonard",
  "time_zone": "Australia/Brisbane",
  "utc_offset": 36000,
}
```

**2. Present times in user's time zone**

First, you'll need to take your unix timestamp and parse it into a date, datetime, or time object. Most programming languages will have a way of doing this in their standard library. Here's some examples:

* [Ruby](http://stackoverflow.com/a/4578301)
* [JavaScript](http://stackoverflow.com/a/847200)
* [c#](http://stackoverflow.com/a/1674258)

The next step is to cast this time object to the appropriate time zone. The `time_zone` string returned from the info is a standard [tzinfo](https://github.com/tzinfo/tzinfo) name. This uses information from the [IANA Time Zone Database](http://www.iana.org/time-zones). Most programming languages will have libraries that help you work with time zone information. Here's some examples:

* Ruby: use [tzinfo](https://github.com/tzinfo/tzinfo) or [Rails](http://stackoverflow.com/a/1386889)
* JavaScript: use [moment-timezone](http://stackoverflow.com/a/18612568)
* [c#](https://msdn.microsoft.com/en-us/library/bb397769(v=vs.110).aspx#Anchor_1)

If you are having trouble using the `time_zone` provided by the API, you can always use the `utc_offset` field which doesn't require you to match to particular time zone names. However, this field will not take into consideration adjustments for daylight savings. Therefore we recommend using the `time_zone` name if possible.