from langchain_community.tools import BraveSearch
api_key = "API KEY"
tool = BraveSearch.from_api_key(api_key=api_key, search_kwargs={"count": 3})

context=tool.invoke('CSk vs KKr Match Hielights')

print(context)