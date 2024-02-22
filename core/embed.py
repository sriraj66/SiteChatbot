import threading
from embedchain import App
from .models import College

class Emmbedded(threading.Thread):
    
    def __init__(self, uid, prompt):
        super(Emmbedded, self).__init__()
        self.id = str(uid)
        self.prompt = prompt
        self.clg = College.objects.get(uid=self.id)
        self.key = self.clg.api_key
        self.config = {
            "app": {
                "config": {
                "id": self.id,
                "name": self.clg.name,
                }
            },
            "llm": {
                "provider": "openai",
                "config": {
                "model": "gpt-3.5-turbo",
                "temperature": 0.7,
                "max_tokens": 1000,
                "top_p": 1,
                "stream": False,
                "prompt": "Use the following pieces of context to answer the query at the end.\nIf you don't know the answer, just say that you don't know, don't try to make up an answer.\n$context\n\nQuery: $query\n\nHelpful Answer:",
                "system_prompt": "Act as the Influncer to join this college. and discribe",
                "api_key": self.key
                }
            },
            "vectordb": {
                "provider": "chroma",
                "config": {
                "collection_name": "full-stack-app",
                "dir": "db",
                "allow_reset": True
                }
            },
            "embedder": {
                "provider": "openai",
                "config": {
                "model": "text-embedding-ada-002",
                "api_key": self.key
                }
            },
            "chunker": {
                "chunk_size": 2000,
                "chunk_overlap": 100,
                "length_function": "len",
                "min_chunk_size": 0
            },
            "cache": {
                "similarity_evaluation": {
                    "strategy": "distance",
                    "max_distance": 1.0,
                },
                "config": {
                    "similarity_threshold": 0.8,
                    "auto_flush": 50,
                },
            },
        }
        self.app = App.from_config(config=self.config)
        
    def add_sources(self):
        urls = self.clg.sub_urls.all()
        for i in urls:
            try:
                self.app.add(i.url)
                print(i.url)
            except Exception as e:
                print(e)
        
        self.app.add(self.clg.hints)
        
        self.clg.state = True
        self.clg.save()
        return True

    def query(self):
        if self.clg.state == False:
            t = threading.Thread(target=self.add_sources)
            t.start()
            return "The Database is updating... Try after some time"
        else:
            return self.app.query(self.prompt)
        
    def search(self, prompt):
        return self.app.search(prompt)
