**Data Streams** represent collections of data from external sources. They can be used to assist in rostering and reporting inside Tanda. You can store data of any type; sales data is treated as monetary, while all other data is treated as unit amounts.

-----------------

**Step 0. Configure Locations & Teams**

Before setting up data streams, you should ensure that you have created [locations & teams](http://help.tanda.co/hc/en-us/articles/211009963) inside your account. This is because you will generally want to associate data stream data with a location or team for comparision purposes. More on that later.

You can create locations & teams at [my.tanda.co/locations](http://my.tanda.co/locations), or using the [Location](https://my.tanda.co/api/v2/documentation#locations) and [Team](https://my.tanda.co/api/v2/documentation#teams-&#40;departments&#41;) API endpoints.

-----------------

**Step 1. Create Data Streams**

You should create a data stream for each distinct source of data. For example, let's say we want to send data sales data from our point of sale system, and foot traffic data from another system. We would create two data streams. One would be called *Sales* (or *Revenue* - the name doesn't really matter), the other might be called *Foot Traffic*.

Use the [Create Data Stream endpoint](https://my.tanda.co/api/v2/documentation#data-streams-data-stream-list-post) to do this. Make sure you provide a data interval - this describes the granularity of data you will provide for this stream. For example, if your POS only lets you export hourly revenue data, your data interval is 3600 seconds.

Once your data streams are created, you will be able to see them at [my.tanda.co/datastreams](https://my.tanda.co/datastreams)

-----------------

**Step 2. Upload Store Stats**

Store stats are individual data points that live within a data stream. In the above example, each hourly chunk of sales data would be an individual store stat. Thus, there will be many store stats associated with a data stream.

Use the [Create Store Stats for Datastream endpoint](https://my.tanda.co/api/v2/documentation#store-stats-create-store-stats-for-datastream-post) to upload store stats into Tanda. Each stat has a `time`, `stat`, and `type`. The `type` field can be any string you like. If it is "sales", the stat will be treated as revenue data, so it will be displayed with a dollar sign in front of it inside Tanda. Otherwise, the stat will be treated as a unit count. In the above example your types might be "sales" (for the POS) and "people" (for the foot traffic counter).

Once your store stats are being uploaded, you'll be able to see the sum of their values at [my.tanda.co/datastreams](https://my.tanda.co/datastreams) under the data stream they're associated with.

-----------------

**Step 3. Create Data Stream Joins**

Once you have started to upload your data into Tanda, you will need to link it to the Tanda objects it relates to. How you do this depends on what you're trying to achieve. Data streams can be joined to the organisation as a whole, to individual locations, or to individual teams within those locations. A data stream can be joined to multiple objects.

It's best to chat to your solutions architect about what sort of solutions will fit your need once you reach this stage of the integration. The joins you create dictate how your data streams are presented. For example, if you join your POS sales data stream to a location, then it will show up on the dashboard, and on rosters, as revenue, which will be comparable against wage costs at that location. If you join your foot traffic data stream against particular teams, you will be able to use it to guide rostering decisions, by also providing a rostering ratio. For example, you could say that for every 100 people who pass the store in a half hour period, you will need to roster one additional person.

Use the [Create Data Stream Join endpoint](https://my.tanda.co/api/v2/documentation#data-stream-joins-data-stream-join-list-post) to create joins. Once created, they will display at [my.tanda.co/datastreams](https://my.tanda.co/datastreams) - you can also create, update, or delete joins by dragging objects around on that page.