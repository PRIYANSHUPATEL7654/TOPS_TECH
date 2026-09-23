"""Advanced Agentic Concepts Part 1; separate from Session 18 Filesystem MCP."""
class FoodOrderAgent:
 def __init__(self):self.orders={}
 def place_order(self,order_id,items):self.orders[order_id]={'items':list(items),'status':'Placed'};return self.orders[order_id]
 def check_status(self,order_id):return self.orders.get(order_id,{'error':'Order not found'})
 def cancel_order(self,order_id):
  if order_id not in self.orders:return 'Order not found'
  self.orders[order_id]['status']='Cancelled';return 'Order cancelled'
class MovieRecommendationAgent:
 def recommend(self,genre,rating_min):
  choices=[('The Martian','science fiction',8.0),('Paddington 2','comedy',7.8),('Dangal','drama',8.3)]
  return next((title for title,g,r in choices if g.casefold()==genre.casefold() and r>=rating_min),'No matching title in sample set')
class SongAgent:
 def find_song(self,mood):return {'happy':'Walking on Sunshine','calm':'Weightless'}.get(mood.casefold(),'Try a popular song for your mood')
class PlaylistAgent:
 def recommend(self,mood,song_agent):return song_agent.find_song(mood)
class Cart:
 def __init__(self):self.items={}
 def add_item(self,name,price):self.items[name]=float(price)
 def remove_item(self,name):self.items.pop(name,None)
 def get_total(self):return round(sum(self.items.values()),2)
def has_preference(preferences,item):return item.casefold() in [x.casefold() for x in preferences]
def item_available(inventory,item):return inventory.get(item,0)>0
def decide_action(preferences,inventory,item):
 if not has_preference(preferences,item):return 'ask_preference'
 if not item_available(inventory,item):return 'offer_alternative'
 return 'recommend_item'
if __name__=='__main__':
 a=FoodOrderAgent();print(a.place_order('O1',['Dosa']));print(a.check_status('O1'));print(a.cancel_order('O1'))
 print(MovieRecommendationAgent().recommend('comedy',7));print(PlaylistAgent().recommend('happy',SongAgent()))
 print('decision:',decide_action(['Dosa'],{'Dosa':4},'Dosa'));c=Cart();c.add_item('Dosa',180);c.add_item('Lassi',60);print('cart total:',c.get_total());c.remove_item('Lassi');print('after removal:',c.get_total())
