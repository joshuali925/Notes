## Leaf query clauses
### match
- full text search
```json
{
  "query": {
    "match" : {
      "<field>" : {
        "query" : "<value>"
      }
    }
  }
}
```

### term
- exact term for a field, use for precise value (ID, username)
- [avoid use for `text` fields](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-term-query.html#avoid-term-query-text-fields)
```json
{
  "query": {
    "term" : {
      "<field>" : {
        "value" : "<value>"
      }
    }
  }
}
```

### range
```json
{
  "query": {
    "range" : {
      "<field>" : {
        "gte" : 10,
          "lte" : 20,
          "boost" : 2.0
      }
    }
  }
}
```

## Compound query clauses
### bool
- matches boolean combinations of queries (boolean clauses) of these occurrance types:
| Occur      | Description                                                                                                              |
|------------|--------------------------------------------------------------------------------------------------------------------------|
| `must`     | The clause (query) must appear in matching documents and will contribute to the score. (logical AND)                     |
| `filter`   | The clause (query) must appear in matching documents. Scoring is ignored and clauses are considered for caching.         |
| `should`   | The clause (query) should appear in the matching document. (logical OR)                                                  |
| `must_not` | The clause (query) must not appear in the matching documents. Scoring is ignored and clauses are considered for caching. |

```json
{
  "query": {
    "bool" : {
      "must" : {
        "term" : { "<field>" : "<value>" }
      },
      "filter": {
        "term" : { "<field>" : "<value>" }
      },
      "must_not" : {
        "range" : {
          "<field>" : { "gte" : 10, "lte" : 20 }
        }
      },
      "should" : [
        { "term" : { "<field1>" : "<value1>" } },
        { "term" : { "<field2>" : "<value2>" } }
      ]
    }
  }
}
```

## Nested queries
```json
{
  "query": {
    "nested": {
      "path": "tags",
      "query": {
        "match": {
           "tags.key": "error"
        }
      }
    }
  }
}
```

```json
{
  "query": {
    "nested": {
      "path": "tags",
        "bool" : {
          "must" : [
          { "match" : {"obj1.name" : "blue"} },
          { "match" : {"obj1.name2" : "blue2"} }
          ]
        }
    }
  }
}
```

## Aggregations
```json
{
  "aggs" : {
    "<aggregation_name>" : {
      "<aggregation_type>" : {
        <aggregation_body>
      }
      [,"meta" : {  [<meta_data_body>] } ]?
      [,"aggs" : { [<sub_aggregation>]+ } ]?
    }
    [,"<aggregation_name_2>" : { ... } ]*
  }
}
```

## Scripts
```json
{
  "query": {
    "bool": {
      "filter": {
        "script": {
          "script": """
            return doc["<field>"].value > 1;
          """
        }
      }
    }
  },
  "aggs": {
    "<aggregation_name>": {
      "terms": {
        "script": """
          long endTime = doc['endTime'].value.toInstant().toEpochMilli();
          long startTime = doc['startTime'].value.toInstant().toEpochMilli();
          return endTime - startTime;
        """
      }
    }
  }
}
```
