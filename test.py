from embedchain import App
import threading
from .constants import *

id = '3bb915ee-dfa9-46fb-8a1c-4142fccf2194'

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
                "If you don't know the answer, just say that you don't know, don't try to make up an answer.\n"
                "$context\n\nQuery: $query\n\nHelpful Answer:"
            ),
            'system_prompt': (
                "Act as William Shakespeare. Answer the following questions in the style of William Shakespeare."
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

print(app.query("Name of the college"))

