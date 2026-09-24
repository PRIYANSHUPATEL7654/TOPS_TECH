"""Session 1: LangChain version, prompt template, simple chain, design notes."""
from importlib.metadata import version
from langchain_core.prompts import PromptTemplate
print("langchain",version("langchain"))
prompt=PromptTemplate.from_template("Why do you support {team} in the IPL?")
print("Final prompt:",prompt.format(team="Gujarat Titans"))
print("Chain flow: user input -> prompt template -> language model -> parsed text output")
print("Food app chain benefits: (1) reusable prompt/model/output stages; (2) consistent error handling and retries; (3) easy tracing and replacement of model/retriever without rewriting app logic.")
print("Direct OpenAI API drawbacks: provider coupling, duplicated prompt/error code, and harder multi-step composition/scaling.")
