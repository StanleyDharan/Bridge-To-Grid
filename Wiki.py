import wikipedia

class Wiki_feature():

    def search(query):
        return wikipedia.search(query, results=10, suggestion=False)

    def summary(query):
        return wikipedia.summary(query, sentences=5, chars=0, auto_suggest=False, redirect=False)
