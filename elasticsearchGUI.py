import tkinter
from elasticsearch import Elasticsearch

# Create a window
master = tkinter.Tk()
master.title('Elasticsearch Interface')
master.geometry('800x600')


def elasticsearch(query):
    # Retrieve the elasticsearch results

    result = ''
    es = Elasticsearch()
    res = es.search(
        index="novels",
        body={
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
                    "fields": ["title", "author", "genre", "keywords", "origin", "story"]
                }
            }
        })
    result = ('Found %d Results:' % res['hits']['total']['value']) + '\n'
    for hit in res['hits']['hits']:
        hit['_source']['keywords'] = str(hit['_source']['keywords'])
        hit['_source']['keywords'] = hit['_source']['keywords'].replace(
            '[', '')
        hit['_source']['keywords'] = hit['_source']['keywords'].replace(
            ']', '')
        hit['_source']['keywords'] = hit['_source']['keywords'].replace(
            '\'', '')

        result += '\nScore: ' + str(hit['_score'])
        result += ("\nTitle: %(title)s\nAuthor: %(author)s\nYear: %(year)s\nOrigin: %(origin)s\nGenre: %(genre)s\nKeywords: %(keywords)s\nURL: %(url)s\n" %
                   hit["_source"])
    return result

# Put the elasticsearch results to the window


def showSearchResults():
    query = query_text.get()
    result = elasticsearch(query)
    results_label.delete('1.0', END)
    results_label.insert(END, result)


# Search label widget
search_label = tkinter.Label(master, text="Keyword: ")
search_label.place(relx=0.23, y=12, anchor=tkinter.NW)

# Query text field widget
query = tkinter.StringVar()
query_text = tkinter.Entry(master, textvariable=query, width=50)
query_text.place(relx=0.5, y=5, rely=0.028, anchor=tkinter.CENTER)

# Search button widget
search_button = tkinter.Button(
    master, text="Search", command=showSearchResults)
search_button.place(relx=0.77, y=9, anchor=tkinter.NE)

# Results text field widget
results = tkinter.StringVar()
results_label = tkinter.Text(master, width=80, height=30)
results.set('Results will be shown here.')
results_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# Scrollbar of the results text field
scrollbar = tkinter.Scrollbar(master)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
results_label.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=results_label.yview)

master.mainloop()
