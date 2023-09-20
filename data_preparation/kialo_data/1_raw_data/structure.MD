# Structure of scraped discussions

`dumped_discussions_first.pickle` includes a 17.832 discussions. Every discussion entry looks as follows:

````
{
   "title": ... // Title of the kialo discussion 
   "background info": ... // Background information of the kialo discussion
   "discussion": {
      "claims": [...] // All claims of the full discssion, more details later
      "locations": [...] // Location of the claims, more details later
      "touchedClaimOrLocationIds": // not relevant
   }
}
````

## Structure of claims
Every claim entry of a discussion has the following structure:
````
{
   "id": xxxx.yy // id of the claim it-self where xxxx is the discussion id, when yy is equal to 0 it is the root claim
   "authorId": "0077c272-1fdc-4202-a06a-160482dfc12d", 
   "created": 1382962412430,
   "version": 2,
   "text": "Anonymous currency discussions", // text of the claim, often empty or not relevant for root claim (i.e. 333.0)
   "lastModifiedForSitemaps": 1382962412430
}
````
## Structure of positions
There is a location entry for every claim which is not the root claim. This entry describes the position of the claim and therefore its target.
````
{
   "id":"333.1228", // id of the relation
   "targetId":"333.355", // id of the source claim
   "version":1,
   "isOrigin":true,
   "authorIdentityId":"54d22c9853057c01262a7192",
   "created":1395770583629,
   "parentId":"333.338", // id of the target claim
   "relation":1, // 1 if relation is Pro, -1 if relation is Con
   "isDeleted":false, // ignore if it is true
   "lastModifiedForSitemaps":1520166022299
}
````