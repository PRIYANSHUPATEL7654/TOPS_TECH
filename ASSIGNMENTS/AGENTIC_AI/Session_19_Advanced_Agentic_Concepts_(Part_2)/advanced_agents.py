"""Advanced Agentic Concepts Part 2; separate from Session 19 GitHub MCP."""
from collections import Counter
class MusicAgent:
 def perceive(self,user_id,recent_history):return {'user_id':user_id,'history':recent_history}
 def reason(self,context):
  history=context['history'];fav=Counter(x['artist'] for x in history).most_common(1);return {'favorite_artist':fav[0][0] if fav else None,'genre':history[-1].get('genre') if history else None}
 def act(self,plan,catalog):return [s for s in catalog if (not plan['genre'] or s['genre']==plan['genre']) and (not plan['favorite_artist'] or s['artist']!=plan['favorite_artist'])][:3]
 def recommend(self,user_id,history,catalog):return self.act(self.reason(self.perceive(user_id,history)),catalog)
class NewReleaseAgent:
 def fetch(self):return [{'title':'Orbit','genre':'Sci-Fi'},{'title':'Second Chance','genre':'Drama'},{'title':'Laugh Track','genre':'Comedy'}]
class MoviePreferenceAgent:
 def __init__(self,genres):self.genres=genres
 def select(self,movies):return [m for m in movies if m['genre'] in self.genres]
class MovieCoordinator:
 def __init__(self):self.messages=[]
 def recommend(self,genres):
  movies=NewReleaseAgent().fetch();self.messages.append({'from':'NewReleaseAgent','to':'MoviePreferenceAgent','payload':movies});result=MoviePreferenceAgent(genres).select(movies);self.messages.append({'from':'MoviePreferenceAgent','to':'Coordinator','payload':result});return result
class AgentRestaurantRecommender:
 def __init__(self,catalog):self.catalog=catalog
 def perceive(self,preference):return preference.casefold().strip()
 def reason(self,preference):return [r for r in self.catalog if preference in r['cuisine'].casefold()]
 def act(self,matches):return [r['name'] for r in matches[:3]] or ['Ask for another cuisine or area']
def delivery_automation_idea():return ['Perceive new orders, ratings, location, and restaurant hours.','Reason about capacity, delivery windows, and constraints.','Draft a batch plan and ask a dispatcher to approve.','Observe partner confirmations and updated ETAs.','Re-plan delayed orders and notify customers.','Learn from timing errors without retaining unnecessary personal data.']
if __name__=='__main__':
 cat=[{'title':'Song X','artist':'A','genre':'Pop'},{'title':'Song Y','artist':'B','genre':'Pop'},{'title':'Song Z','artist':'C','genre':'Jazz'}];print('Music:',MusicAgent().recommend('U1',[{'artist':'A','genre':'Pop'}],cat))
 co=MovieCoordinator();print('Movies:',co.recommend(['Comedy']));print('Messages:',co.messages)
 a=AgentRestaurantRecommender([{'name':'Dosa House','cuisine':'South Indian'},{'name':'Swati Snacks','cuisine':'Gujarati'}]);print('Restaurant:',a.act(a.reason(a.perceive('south indian'))));print(*delivery_automation_idea(),sep='\n')
