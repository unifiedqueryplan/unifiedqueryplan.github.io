---
title: Operations
layout: default
parent: MongoDB
---

MongoDB states the operations that can be performed in a [list](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L50).





| Operation                     | Category  | Reference                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | --------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AND_HASH                      | Combinator       | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L50)  | It performs a hash-based intersection of two or more sets of documents.                                                                                                                                                                                                                                                                                                                                                                 |
| AND_SORTED                    | Combinator       | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L51)  | It performs an intersection of two or more sets of documents in order.                                                                                                                                                                                                                                                                                                                                                                  |
| BATCHED_DELETE                | Consumer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L52)  | Delete documents in batches.                                                                                                                                                                                                                                                                                                                                                                                                            |
| CACHED_PLAN                   | Executor  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L53)  | It evaluates the cost of a cached plan                                                                                                                                                                                                                                                                                                                                                                                                  |
| COLLSCAN                      | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L54)  | It scans over a collection.                                                                                                                                                                                                                                                                                                                                                                                                             |
| COLUMN_IXSCAN                 | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L55)  |  An index scan operation that returns only the indexed field values for a given collection.                                                                                                                                                                                                                                                                                                                                             |
| COUNT                         | Folder    | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L63)  | "COUNT" refers to the stage in the query execution plan that performs a count operation. The count operation counts the number of documents in a collection that match a specified filter.                                                                                                                                                                                                                                              |
| COUNT_SCAN                    | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L68)  | Used by the count command. Scans an index from a start key to an end key.                                                                                                                                                                                                                                                                                                                                                               |
| DELETE                        | Consumer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L70)  | Delete a document.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DISTINCT_SCAN                 | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L74)  | Used by the distinct command.  Executes a mutated index scan over the provided bounds.                                                                                                                                                                                                                                                                                                                                                  |
| EOF                           | Executor  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L76)  | EOF" represents no data is read and output.                                                                                                                                                                                                                                                                                                                                                                                             |
| EQ_LOOKUP                     | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L131) | Represents a lookup from a foreign collection by equality match on foreign and local fields.                                                                                                                                                                                                                                                                                                                                            |
| FETCH                         | Executor  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L78)  | This stage turns a Record Id into a BSONObj.                                                                                                                                                                                                                                                                                                                                                                                            |
| GEO_NEAR_2D                   | Folder    | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L81)  | Outputs documents in order of nearest to farthest from a specified point.                                                                                                                                                                                                                                                                                                                                                               |
| GEO_NEAR_2DSPHERE             | Folder    | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L82)  | It finds the documents that are near a given geographic location with the 2d spherical index.                                                                                                                                                                                                                                                                                                                                           |
| GROUP                         | Folder    | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L130) | Group data.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| IDHACK                        | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L84)  | A standalone stage implementing the fast path for key-value retrievals via the \_id index.                                                                                                                                                                                                                                                                                                                                              |
| IXSCAN                        | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L86)  | Stage scans over an index from startKey to endKey, returning results that pass the provided filter.                                                                                                                                                                                                                                                                                                                                     |
| LIMIT                         | Combinator       | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L87)  | Limit the number of returned rows.                                                                                                                                                                                                                                                                                                                                                                                                      |
| MOCK                          | Executor  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L89)  | "MOCK" refers to a stage that is used for testing purposes, and is not part of the actual query execution plan.                                                                                                                                                                                                                                                                                                                         |
| MULTI_ITERATOR                | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L92)  | "MULT_ITERATOR" refers to a stage that is used when multiple indexes are used to retrieve the documents in a query.                                                                                                                                                                                                                                                                                                                     |
| MULTI_PLAN                    | Executor  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L94)  | MULTI_PLAN" refers to a stage that is used when multiple query plans are generated and evaluated by the query optimizer.                                                                                                                                                                                                                                                                                                                |
| OR                            | Combinator       | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L95)  | This stage outputs the union of its children. It optionally deduplicates on RecordId.                                                                                                                                                                                                                                                                                                                                                   |
| PROJECTION_COVERED            | Projector | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L99)  | An explicit projection which is supported by an index scan (eg, for a "covered" index query).                                                                                                                                                                                                                                                                                                                                           |
| PROJECTION_DEFAULT            | Projector | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L98)  | A "default" projection, where no explicit projection is requested.                                                                                                                                                                                                                                                                                                                                                                      |
| PROJECTION_SIMPLE             | Projector | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L100) | An explicit projection which is supported by a collection access -- usually preceded by a FETCH or COLLSCAN step.                                                                                                                                                                                                                                                                                                                       |
| QUEUED_DATA                   | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L102) | "QUEUED_DATA" is a stage that is used to retrieve documents from a queue that were added to it by a preceding stage.                                                                                                                                                                                                                                                                                                                    |
| RECORD_STORE_FAST_COUNT       | Folder    | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L103) | "RECORD_STORE_FAST_COUNT" is an operation in MongoDB query plans that counts the number of documents in a collection using a fast count operation. This operation uses a metadata field called "ns" in the collection to count the number of documents without scanning the actual documents.                                                                                                                                           |
| RETURN_KEY                    | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L104) | the RETURN_KEY stage indicates that the query is a covered query, and the results can be fetched directly from the index keys without actually retrieving the full documents from the collection.                                                                                                                                                                                                                                       |
| SAMPLE_FROM_TIMESERIES_BUCKET | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L105) | the SAMPLE_FROM_TIMESERIES_BUCKET stage is specific to the MongoDB Time Series collections and is used to retrieve a random sample of documents from the specified time-series bucket.                                                                                                                                                                                                                                                  |
| SENTINEL                      | Executor  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L132) | a stage that acts as a placeholder for a query plan stage that has been pruned during optimization                                                                                                                                                                                                                                                                                                                                      |
| SHARDING_FILTER               |           | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L106) | The "SHARDING_FILTER" stage in MongoDB query plans refers to the filtering of data based on the shard key. We mapped it into the property filter.                                                                                                                                                                                                                                                                                       |
| SKIP                          | Executor  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L107) | an operation that skips the specified number of documents from the beginning of the result set. It is commonly used with "LIMIT" to implement pagination in queries.                                                                                                                                                                                                                                                                    |
| SORT_DEFAULT                  | Combinator       | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L109) | Sort data                                                                                                                                                                                                                                                                                                                                                                                                                               |
| SORT_KEY_GENERATOR            | Combinator       | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L111) | an operator that generates keys for sorting a set of documents based on the values of the specified fields.                                                                                                                                                                                                                                                                                                                             |
| SORT_MERGE                    | Combinator       | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L113) | an operation that sorts the results of two or more sub-plans and then merges them together.                                                                                                                                                                                                                                                                                                                                             |
| SORT_SIMPLE                   | Combinator       | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L110) | Sort data.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SUBPLAN                       | Executor  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L114) | It plans each clause of the $or individually and then creates an overall query plan based on the winning plan from each clause.                                                                                                                                                                                                                                                                                                         |
| TEXT_MATCH                    | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L118) | A stage that returns every document in the child that satisfies the FTS text matcher built with the query parameter.                                                                                                                                                                                                                                                                                                                    |
| TEXT_OR                       | Combinator       | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L117) | A blocking stage that returns the set of WSMs with RecordIDs of all of the documents that contain the positive terms in the search query, as well as their scores.                                                                                                                                                                                                                                                                      |
| TRIAL                         | Executor  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L121) | TrialStage runs a specified 'trial' plan for a given number of iterations, tracking the number of times the plan advanced over that duration. If the ratio of advances to works falls below a given threshold, then the trial results are discarded and the backup plan is adopted. Otherwise, we consider the trial a success and return the cached results of the trial phase followed by any further results that the plan produces. |
| UNKNOWN                       | Executor  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L123) | An operation for testing that always throws exceptions.                                                                                                                                                                                                                                                                                                                                                                                 |
| UNPACK_TIMESERIES_BUCKET      | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L125) | It unpacks data from time series buckets.                                                                                                                                                                                                                                                                                                                                                                                               |
| UPDATE                        | Consumer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L127) | Update data.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VIRTUAL_SCAN                  | Producer  | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/stage_types.h#L59)  | A VirtualScanNode is similar to a collection or an index scan except that it doesn't depend on an underlying storage implementation. It can be used to represent a virtual collection or an index scan in memory by using a backing vector of BSONArray.                                                                                                                                                                                |


## References
* [MongoDB Documents](https://docs.mongodb.com/manual/reference/explain-results/#explain-query-plans)
* [MongoDB Github Commit: a857380c](https://github.com/mongodb/mongo/blob/a857380c)