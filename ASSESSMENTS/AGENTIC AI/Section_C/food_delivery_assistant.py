"""C: Menu-driven multi-tool agent with memory, strategy and visible ReAct summaries."""
import json
TOOLS={
 'place_order':{'name':'place_order','description':'Create a draft order and return an order ID.','parameters':{'type':'object','properties':{'restaurant':{'type':'string'},'item':{'type':'string'},'cuisine':{'type':'string'}},'required':['restaurant','item','cuisine']}},
 'track_order':{'name':'track_order','description':'Return status and ETA for an order ID.','parameters':{'type':'object','properties':{'order_id':{'type':'string'}},'required':['order_id']}},
 'file_complaint':{'name':'file_complaint','description':'Record a complaint for an order.','parameters':{'type':'object','properties':{'order_id':{'type':'string'},'issue':{'type':'string'}},'required':['order_id','issue']}},
 'get_recommendations':{'name':'get_recommendations','description':'Recommend sample dishes for a cuisine preference.','parameters':{'type':'object','properties':{'cuisine':{'type':'string'}},'required':['cuisine']}}}
ORDERS={}
def place_order(restaurant,item,cuisine):
 order_id=f"FD{len(ORDERS)+5001}";ORDERS[order_id]={'restaurant':restaurant,'item':item,'cuisine':cuisine,'status':'Placed','eta':'30 minutes'};return {'order_id':order_id,**ORDERS[order_id]}
def track_order(order_id):return {'order_id':order_id,**ORDERS[order_id]} if order_id in ORDERS else {'error':'Order not found'}
def file_complaint(order_id,issue):return {'complaint_id':f'C-{order_id}','order_id':order_id,'issue':issue,'status':'Recorded'}
def get_recommendations(cuisine):
 options={'Gujarati':['Gujarati thali','Khandvi'],'South Indian':['Masala dosa','Idli'],'Italian':['Margherita pizza','Pasta']};return {'cuisine':cuisine,'dishes':options.get(cuisine.title(),['Chef special','Seasonal bowl'])}
def decide_response_strategy(action_type,memory):
 if action_type=='file_complaint' and len(memory['complaints_filed'])>=1:return 'fine_tuned'
 if action_type in {'track_order','get_recommendations'}:return 'rag'
 return 'prompt'
class Agent:
 def __init__(self):self.session_log=[];self.session_memory={'orders_placed':[],'complaints_filed':[],'preferred_cuisine':None,'interaction_count':0}
 def run_action(self,action,args):
  strategy=decide_response_strategy(action,self.session_memory)
  print('Reason summary: route this request to the matching local tool; check the returned result.')
  print('Action:',action,'arguments:',args)
  funcs={'place_order':place_order,'track_order':track_order,'file_complaint':file_complaint,'get_recommendations':get_recommendations}
  result=funcs[action](**args);print('Observation:',result)
  if action=='place_order':self.session_memory['orders_placed'].append(result['order_id']);self.session_memory['preferred_cuisine']=args['cuisine']
  if action=='file_complaint':self.session_memory['complaints_filed'].append(result['complaint_id'])
  if action=='get_recommendations':self.session_memory['preferred_cuisine']=args['cuisine']
  self.session_memory['interaction_count']+=1
  self.session_log.append({'action':action,'arguments':args,'result':result,'strategy':strategy})
  print('Strategy:',strategy);print('Memory:',self.session_memory);return result
 def report(self):
  print('Session report:');print(json.dumps({'actions':self.session_log,'session_memory':self.session_memory},indent=2))
def main():
 a=Agent();print('Tool schemas:');print(json.dumps(list(TOOLS.values()),indent=2))
 while True:
  print('\n1 Place Order  2 Track Order  3 File Complaint  4 Get Personalised Recommendations  5 Exit')
  option=input('Choose: ').strip()
  if option=='5':a.report();break
  if option=='1':args={'restaurant':input('Restaurant: '),'item':input('Dish: '),'cuisine':input('Cuisine: ')};action='place_order'
  elif option=='2':args={'order_id':input('Order ID: ')};action='track_order'
  elif option=='3':args={'order_id':input('Order ID: '),'issue':input('Issue: ')};action='file_complaint'
  elif option=='4':args={'cuisine':input('Cuisine: ')};action='get_recommendations'
  else:print('Choose a valid option.');continue
  a.run_action(action,args)
if __name__=='__main__':main()
