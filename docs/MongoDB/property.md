---
title: Properties
layout: default
parent: MongoDB
---

Properties are defined as the first parameter of the function call `append*()` (e.g., `appendNumber()` and `appendBool()`) in the file [plan_explainer_impl.cpp](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp). Some descriptions are copied from [MongoDB Documents](https://docs.mongodb.com/manual/reference/explain-results/#explain-query-plans).


| Property                    | Category      | Reference                                                                                              | Description                                                                                                                                                                                                                        |
| --------------------------- | ------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| advanced                    | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L224) | An "advanced" query plan refers to a query plan that requires additional processing or resources beyond what is typical for a simple query.                                                                                        |
| alreadyHasObj               | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L339) | Unknown property that has not been observed in practice.                                                                                                                                                                           |
| chunkSkips                  | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L432) | Estimated number of chunks skipped.                                                                                                                                                                                                |
| collation                   | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L285) | "collation" refers to a set of rules that determine how string values are compared and sorted. Collation can affect the results of queries and can be used to perform case-insensitive or accent-insensitive searches and sorting. |
| direction                   | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L323) | Estimated direction of scanning.                                                                                                                                                                                                   |
| docsExamined                | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L338) | Estimated number of documents read.                                                                                                                                                                                                |
| docsRejected                | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L471) | Estimated number of documents dropped.                                                                                                                                                                                             |
| dupsDropped                 | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L460) | "dupsDropped" refers to the number of duplicate documents that were removed during the execution of a query or aggregation pipeline.                                                                                               |
| dupsTested                  | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L459) | Unknown property that has not been observed in practice.                                                                                                                                                                           |
| executionTimeMillisEstimate | Cost          | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L220) | Estimated time to execute the associated operation.                                                                                                                                                                                |
| failed                      | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L230) | "failed" refers to the number of documents that could not be processed during the execution of a query or aggregation pipeline.                                                                                                    |
| filter                      | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L212) | Filter out data by predicates.                                                                                                                                                                                                     |
| indexBounds                 | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L329) | Permissible values for all fields in the index.                                                                                                                                                                                    |
| indexName                   | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L311) | The name of the index.                                                                                                                                                                                                             |
| indexPrefix                 | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L465) | The fields that go in the index first.                                                                                                                                                                                             |
| indexVersion                | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L294) | The index version.                                                                                                                                                                                                                 |
| isEOF                       | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L231) | Specifies whether the execution stage has reached the end of the stream                                                                                                                                                            |
| isMultiKey                  | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L315) | Whether it uses multiple keys.                                                                                                                                                                                                     |
| isPartial                   | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L293) | Whether it is a partial index.                                                                                                                                                                                                     |
| isSparse                    | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L292) | Whether the index is sparse.                                                                                                                                                                                                       |
| isUnique                    | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L291) | Whether the index enforces a uniqueness constraint                                                                                                                                                                                 |
| keyPattern                  | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L282) | The key pattern.                                                                                                                                                                                                                   |
| keysExamined                | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L333) | "keyExamined" refers to the number of index keys that were examined during the execution of a query.                                                                                                                               |
| limitAmount                 | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L408) | Estimated number of limited returned rows.                                                                                                                                                                                         |
| memLimit                    | Cost          | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L440) | The maximum available memory.                                                                                                                                                                                                      |
| memUsage                    | Cost          | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L239) | Estimated memory usage.                                                                                                                                                                                                            |
| nBucketsDiscarded           | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L424) | Estimated number of buckets dropped.                                                                                                                                                                                               |
| nBucketsUnpacked            | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L484) | Estimated number of buckets unpacked.                                                                                                                                                                                              |
| nCounted                    | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L272) | Estimated number of documents.                                                                                                                                                                                                     |
| needTime                    | Cost          | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L225) | Estimated time needed.                                                                                                                                                                                                             |
| needYield                   | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L226) | "needYield" refers to whether the query execution engine needs to temporarily release its control of the server resources to allow other operations to run.                                                                        |
| nMatched                    | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L490) | "nMatched" refers to the number of documents that matched the query criteria and were modified or deleted in an update or delete operation.                                                                                        |
| nReturned                   | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L217) | Estimated number of documents returned.                                                                                                                                                                                            |
| nSkipped                    | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L273) | Estimated number of documents skipped.                                                                                                                                                                                             |
| nWouldDelete                | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L305) | Estimated number of documents dropped.                                                                                                                                                                                             |
| nWouldModify                | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L491) | Estimated number of documents modified.                                                                                                                                                                                            |
| nWouldUpsert                | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L492) | Estimated number of documents inserted.                                                                                                                                                                                            |
| parsedTextQuery             | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L467) | The query.                                                                                                                                                                                                                         |
| restoreState                | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L228) | Estimated number of times that the query stage restored a saved execution state, for example after recovering locks that it had previously yielded.                                                                                |
| saveState                   | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L227) | Estimated number of times that the query stage suspended processing and saved its current execution state, for example in preparation for yielding its locks.                                                                      |
| seeks                       | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L395) | Estimated number of times that we had to seek the index cursor to a new position to complete the index scan.                                                                                                                       |
| skipAmount                  | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L436) | "skipAmount" refers to the estimated number of documents that were skipped in a query or aggregation pipeline.                                                                                                                     |
| sortPattern                 | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L439) | "sortPattern" refers to the order in which the documents in the result set are sorted.                                                                                                                                             |
| spills                      | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L452) | "spills" refers to the estimated number of times that the query or aggregation pipeline had to write data to disk due to memory constraints.                                                                                       |
| textIndexVersion            | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L468) | The version of the text index.                                                                                                                                                                                                     |
| totalDataSizeSorted         | Cardinality   | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L449) | Estimated size of data to sort.                                                                                                                                                                                                    |
| transformBy                 | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L411) | Original data for a projection operation.                                                                                                                                                                                          |
| type                        | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L446) | The sort type.                                                                                                                                                                                                                     |
| usedDisk                    | Cost          | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L451) | Estimated disk usage.                                                                                                                                                                                                              |
| warning                     | Configuration | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L196) | Warning information.                                                                                                                                                                                                               |
| works                       | Status        | [Link](https://github.com/mongodb/mongo/blob/a857380c/src/mongo/db/query/plan_explainer_impl.cpp#L223) | "works" refers to the total number of operations that were performed during the query execution.                                                                                                                                   |




## References
* [MongoDB Documents](https://docs.mongodb.com/manual/reference/explain-results/#explain-query-plans)
* [MongoDB Github Commit: a857380c](https://github.com/mongodb/mongo/blob/a857380c)