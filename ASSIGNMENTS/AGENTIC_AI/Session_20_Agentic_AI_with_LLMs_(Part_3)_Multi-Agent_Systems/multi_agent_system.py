"""Session 20 multi-agent systems with explicit messages and handoffs."""
PRODUCTS=[{'name':'Phone A','category':'phone','price':19999},{'name':'Phone B','category':'phone','price':14999},{'name':'Laptop C','category':'laptop','price':55999},{'name':'Headphones D','category':'audio','price':4999}]
class SearchAgent:
 def search(self,query):return [p for p in PRODUCTS if query.casefold() in (p['name']+' '+p['category']).casefold()]
class RecommendationAgent:
 def recommend(self,user_id):return [p for p in PRODUCTS if p['category']=='phone'][:3]
class PlaylistAgent:
 def top_trending(self):return ['Kesariya','Blinding Lights','Levitating']
 def create_playlist(self,name,songs):return {'name':name,'songs':songs}
class ChatAgent:
 def __init__(self,playlist_agent):self.playlist_agent=playlist_agent;self.messages=[]
 def handle(self,request):
  self.messages.append({'from':'ChatAgent','to':'PlaylistAgent','message':request});result=self.playlist_agent.create_playlist('Suggested Playlist',self.playlist_agent.top_trending());self.messages.append({'from':'PlaylistAgent','to':'ChatAgent','message':result});return result
class MultiAgentManager:
 def __init__(self):self.playlist=PlaylistAgent();self.chat=ChatAgent(self.playlist);self.messages=[]
 def handle(self,request):result=self.chat.handle(request);self.messages.extend(self.chat.messages);self.chat.messages=[];return result
def cricket_fetch_agent(scores):return scores
def cricket_summary_agent(scores):return f"Top scorer: {max(scores,key=scores.get)} ({max(scores.values())} runs)."
if __name__=='__main__':
 s=SearchAgent();r=RecommendationAgent();print('Search:',s.search('phone'));print('Recommendations:',r.recommend('U1'))
 manager=MultiAgentManager();print('Playlist:',manager.handle('Make a top trending playlist'));print('Messages:',manager.messages)
 scores=cricket_fetch_agent({'Player A':72,'Player B':45});print(cricket_summary_agent(scores))
