"""LangChain summary node plus LangGraph user-follow-up branch."""
from typing import TypedDict
from langgraph.graph import StateGraph,START,END
from review_summary import summarize_review
class State(TypedDict): review:str; wants_details:bool; summary:str; response:str
def summary_node(state):return {'summary':summarize_review(state['review'])}
def followup_node(state):
 answer=input('Would you like more details about the movie? (yes/no): ').strip().lower()
 return {'wants_details':answer.startswith('y')}
def response_node(state):return {'response':'More details: check the official listing for showtimes and age rating.' if state['wants_details'] else 'Thanks for reading the summary.'}
graph=StateGraph(State);graph.add_node('summarize',summary_node);graph.add_node('ask',followup_node);graph.add_node('respond',response_node);graph.add_edge(START,'summarize');graph.add_edge('summarize','ask');graph.add_edge('ask','respond');graph.add_edge('respond',END);app=graph.compile()
if __name__=='__main__':
 review='The film is warm, funny, and well acted, though the pacing slows in the middle.'
 result=app.invoke({'review':review,'wants_details':False,'summary':'','response':''});print('Summary:',result['summary']);print(result['response'])
