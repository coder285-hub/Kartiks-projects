# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.

## Random Partitioning

In terms of accessibility and having a backup on other boats in the event of a potential boat data loss, distributing the data around three boats can be beneficial, but it takes up needless space. Instead, if every boat had its own time zone, it would make better use of available capacity.

## Partitioning by Hour

Each database doesn't need to require more space if the data is split up into three fields based on time periods. Since each database must operate on its own schedule, it may be more effective.


## Partitioning by Hash Value

By searching for small hash values rather than the whole date in possible date searches, entering the hash value reduces the amount of time the database takes to operate. Indexing can also help to speed up the search process. Giving the same hash value to the same date can occasionally be challenging, even if all hash values are provided.

