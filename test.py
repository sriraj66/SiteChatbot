from embedchain import App
import threading
from constants import *

id = '3bb915ee-dfa9-46fb-8a1c-4142fccf214'
# "Act as Assistance. Answer the following questions within 3 lines in the style of Assistance."

config = {
    'app': {
        'config': {
            'name': 'full-stack-app',
            'id': id,
        }
    },
    'llm': {
        'provider': 'openai',
        'config': {
            'model': 'gpt-3.5-turbo',
            'temperature': 0.5,
            'max_tokens': 1000,
            'top_p': 1,
            'stream': False,
            'prompt': (
                "Use the following pieces of context to answer the query at the end.\n"
                "If you don't know the answer, just say that you don't know. Dont give  irrevelant Answers. \n"
                "$context\n\nQuery: $query\n\nHelpful Answer:"
            ),
            'system_prompt': (
                "Act as the Assistance to join this college. and give within 3 lines.\n"
                "give crispy answers, or if there is more points give as list items<ul> <li>  for bullets and point"
            ),
            'api_key': key
        }
    },
    'vectordb': {
        'provider': 'chroma',
        'config': {
            'collection_name': 'full-stack-app',
            'dir': 'db',
            'allow_reset': True
        }
    },
    'embedder': {
        'provider': 'openai',
        'config': {
            'model': 'text-embedding-ada-002',
            'api_key': key
        }
    },
    'chunker': {
        'chunk_size': 2000,
        'chunk_overlap': 100,
        'length_function': 'len',
        'min_chunk_size': 0
    },
    'cache': {
      'similarity_evaluation': {
          'strategy': 'distance',
          'max_distance': 1.0,
      },
      'config': {
          'similarity_threshold': 0.8,
          'auto_flush': 50,
      },
    },
}


app = App.from_config(config=config)

app.add("https://krct.ac.in")

while 1:
    answer, sources = app.chat(input("Query : "), citations=True)
    print(answer)
    print("Sources : ",len(sources))
    

