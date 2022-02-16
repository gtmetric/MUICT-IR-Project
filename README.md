# Information Storage and Retrieval - Project

## Introduction
The world’s first novel was written at the beginning of the 11th century[ 1],and novels have reached their peak of popularity in the last few centuries. As the
popularity of novels rose, the number of novels also grew rapidly since the first novel was written a thousand years ago. Since the number of novels only
increases over time, it has become difficult for readers to find a novel that fits their interests. Despite the advancement of technology, a tool to find a
novel that matches the exact reader’s interests is unknown. In this project, the available search engines were studied to discover the flaws, which do not
allow novel readers to find new novels freely and easily. In addition, a brand-new search system was also implemented to solidify the idea of searching for
novels based on the exact interests of the readers.

## Problems
According to the Cambridge Dictionary, a novel is defined as a long-printed story about imaginary characters and events [2]. The world’s first novel is the
Tale of Genji written at the start of the 11th century [1]. Since the first novel was written more than a thousand years ago, countless novels have been
written and published until today. For novel enthusiasts, finding and selecting a novel to read is difficult because of the huge number of novels despite the
help of current technology. Most novel search systems available today could allow users only to search by the title of the novel. However, the readers may not
always know for sure what exact novel they are looking for. In addition, most search engines do not allow users to explore new novels by searching keywords in
the actual story of the novels.

There are several types of people who may need a search system for searching for novels by the story of the novels. The first type is readers in general,
especially online readers and novel readers. This type of people would normally spend their time finding books or novels to read, or they spend their time
surfing on the Internet to explore new things. Another type of user is novel researchers. Researchers would find the system useful because they often need to
search for novels for their research or novels related to their research. The other type of users is students. Sometimes, it is a school requirement for
students to find novels to read, and some students find reading novels to be extremely enjoyable and educational. Besides, foreign students like to read novels
to practice the language that they are learning and to learn new cultures embed in the novels.

## Literature
There are a few search systems available online for searching for novels including Google Books, The Online Books Page, and the search engine on Lit2Go. Google
Books is the largest book database and the most popular search engine for books. With its advanced search, Google Books is the best search engine available
today for books [3]. The Online Books Page is another large and popular search engine maintained by the University of Pennsylvania. The Online Books Page
allows users to search for books by the title, author, and subject of the books. Although these two search engines are extremely large, powerful, and popular,
they do not offer an option to search for novels by using the story of the novels. In contrast, most search engines only allow users to search for novels by
the title, author, genre, and subject of the novels.

The search engine on the Lit2Go website does allow users to search for novels by using the story in the novels. However, the system is nowhere near perfect
since the results from the search are the chapters of the novels, which could be overwhelming. There could be many chapters in a novel, and when a query
matches to a novel, it is likely to match with most chapters. Therefore, the results would contain a lot of chapters of the same novel, which the users are not
interested in, at least not yet. Returning only the necessary information of the novel including the title, author, and genre would be enough.

## Methodology
To solve the problems mentioned above, this project aims to find a solution, which is to create a search system. The new search system should allow users to
search for novels by using the story of the novels. In addition, the results of the search should not be overwhelming, and the results should contain only the
necessary information. The necessary information may include the title, author, genre, and a link to the novel. In order to achieve in creating the search
system, a dataset is needed for the search system.

Since there is no free dataset of novels available on the Internet, the dataset must be web-scraped from the Lit2Go website. To web-scrape, Web Scraper [4],
which is a Chrome extension, has been used to extract the novels from Lit2Go. By using Web Scraper, the title, URL, author, year, origin, genre, keywords, and
the story of the novels have been extracted and stored in a CSV file. The web-scraped dataset is raw data; therefore, it must be cleaned by removing some
useless columns, merging some records, and removing meaningless characters. Some records of the raw data need to be merged because each record was initially a
chapter, and this project only interests in novels as a whole.

The raw data was cleaned by using Python since Python is a flexible language and provides the needed tools for tidying the data. The cleaned data is stored as
a structured table, yet Elasticsearch accepts only data in ND-JSON format (why Elasticsearch was selected for this project will be explained in the next part
of this report). Thus, the data needs to be converted to ND-JSON format and stored in a JSON file. Again, the data was converted by using Python as Python provides packages for manipulating JSON data. To convert to ND-JSON, the data first needs to be converted to the normal JSON format and stored in a JSON file. After that, the JSON data is read back into the Python program, and each record is extracted and stored in the new JSON file in the ND-JSON format.

## Implementation
Elasticsearch was selected to be the search engine of this project because it is fast, scalable, resilient, and provides a wide set of features [5]. To
implement a search engine in Elasticsearch, an index first has to be created through Kibana, given in Appendix A. In this project, explicit mapping has been
used because the fields in the novel records would always be the same. In addition, some values of the records must be always kept the same without going
through any analyzer in Elasticsearch. The analyzer of the index was also set manually to use the Simple Elasticsearch analyzer, remove stop words, stem words,
and change all characters to lowercase.

After the index was created, the data can be uploaded to Elasticsearch by using the Bulk API. To upload the data, cURL has been used to transfer the data file
to the Elasticsearch local server. The cURL command is given in Appendix B. The search query used in the search system, given in Appendix C, is a multi-match
query since there are many fields in the dataset. Also, the query supports fuzzy query and proximity search. The fuzzy query was set to auto, and the proximity
search distance was set to five.

Up until this point, the body of the search engine is ready to be used, and the search query can be used in Kibana as an interface for the Elasticsearch index.
However, Kibana is not an appropriate interface for general users since the search in Kibana is in the form of HTTP requests. Hence, an interface for general
users has been created by using the Tkinter package in Python.The interface is extremely simple and contains a search field and another field for the results.
After the users enter the search keyword and clicked “Search”, the results will be shown as in the given figure in Appendix D.

## Results
After the implementation was complete, several test cases were run to see how the search system performed. The results of most test cases were relevant as
given in Appendix E. Searching for a single keyword worked like a charm as can be seen in the first figure in the Appendix. When searching for “romeo”, it
returned “Romeo and Juliet” which is one of the most popular novels of all time. In addition, when searching for “julet”, it also returned “Romeo and Juliet”
despite the misspelling. This shows that the search system is able to handle spell correction well, especially for “julet”, and also returned the relevant
results.

For multi-word queries, it also worked well as shown in the third figure of the Appendix. When inserting “adventure in america” as a query, the results are
novels that the origin was America or that the story mentioned America. The first result was not related to adventure at all, but many fields included
“america” especially in origin and keywords. Because the origin and keywords are fields that contain short texts, it is weighted heavier than the story itself.
Since short fields outweigh longer fields, it returned a high score for the first result due to the occurrences of “america”. However, the other novels are
related to adventures, and most of them have “adventure” as their genre.

Although the search system works well for most cases, an irrelevant result has been identified, given in Appendix F. When searching for “nemo”, the first and
highest novel had nothing related to “nemo” because the novel was not in English. The analyzer that has been used for this search system stemmed words as if
they were all English. Therefore, the Spanish novel was stemmed in an incorrect manner because of its language, and it was retrieved incorrectly as if it were
in English.

This problem can still be solved by having a language detector or classified the dataset by languages. Since this project only aims to provide searches for
novels written in English, it would be most appropriate to have a language detector to reject or remove all documents that are not in English. However, it is
possible to have a gigantic database of novels in different languages as the backbone of the search system. As more languages are included in the database, it
is possible to implement a smart search engine. An example would be a search engine that could automatically detect different languages and return only results
in the detected language.

## Conclusion
In this project, the information needs of the novel readers have been identified and studied. The currently existing solutions including different search
engines were also explored to see and understand the flaws of those systems. After the problems were identified, a simple search system has been implemented
based on the novels on the Lit2Go. The dataset and the interface of the system were preprocessed and implemented in Python, and Elasticsearch was used for
storing data and searching. In conclusion, the search system was successfully implemented, and from the test cases, it appears to work well and could be useful
for real uses. Although the system works well in most cases, it can still be improved especially in handling novels in dif ferent languages. Overall, the
search system is simple to use, useful for novel readers, and it works for most cases, which indicates the success of this project.

## References
[1] The Editors of Encyclopaedia Britannica, "The Tale of Genji," Britannica, 27 March 2020. [Online]. Available: https://www.britannica.com/topic/The-Tale-of-Genji. [Accessed 06 December 2020].
[2] C. Dictionary, "novel," Cambridge, [Online]. Available: https://dictionary.cambridge.org/dictionary/english/novel. [Accessed 6 December 2020].
[3] Library of Congress, "Finding Novels," Library of Congress, [Online]. Available: https://guides.loc.gov/lost-titles-forgotten-rhymes/finding-novels. [Accessed 6 December 2020].
[4] webscraper.io, "Web Scraper," webscraper.io, [Online]. Available: https://webscraper.io/. [Accessed 2 December 2020].
[5] elastic, "Elasticsearch," elastic, [Online]. Available: https://www.elastic.co/what- is/elasticsearch. [Accessed 6 December 2020].

## Appendices
### Appendix A: Elasticsearch Indexing
```
PUT novels
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text"
      },
      "url": {
        "type": "keyword"
      },
      "author": {
        "type": "text"
      },
      "year": {
        "type": "integer"
      },
      "origin": {
        "type": "text"
      },
      "genre": {
        "type": "text"
      },
      "keywords": {
        "type": "text"
      },
      "story": {
        "type": "text",
        "analyzer": "stop_word_analyzer"
      }
    }
  },
  "settings": {
    "analysis": {
      "filter": {
        "stemmer": {
          "type": "stemmer",
          "name": "english"
        }
      },
      "analyzer": {
        "stop_word_analyzer": {
          "type": "simple",
          "stopwords": "_english_",
          "filter": [
            "lowercase",
            "stemmer"
          ]
        }
      }
    }
  }
}
```
### Appendix B: cURL Command for Uploading the Data to Elasticsearch
```
curl -H "Content-Type:application/x-ndjson" -X POST http://localhost:9200/novels/_bulk --data-binary "@data2.json"
```

### Appendix C Search Query
GET novels/_search
{
  "_source": [
    "title",
    "author",
    "year",
    "origin",
    "genre",
    "keywords",
    "url"
  ],
  "query": {
    "multi_match": {
      "query": query,
      "fuzziness": "auto",
      "fuzzy_transpositions": "true",
      "slop": "5",
      "fields": [
        "title",
        "author",
        "genre",
        "keywords",
        "origin",
        "story"
      ]
    }
  }
}

### Appendix D: Elasticsearch Interface


### Appendix E: Relevant Results
1. Romeo


2. Julet


3. Adventure in America


### Appendix F Irrelevant Result
 
