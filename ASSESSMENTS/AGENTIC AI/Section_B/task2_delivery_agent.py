"""B2: four tools, schemas, keyword router and call history."""
import json,re

def check_restaurant_status(name):return f"{name}: open now (sample availability)."
def get_estimated_delivery_time(order_id):return f"Order {order_id}: estimated arrival in 32 minutes (sample ETA)."
def apply_discount(order_id,reason):return f"Discount review for {order_id}: {reason}; sample 10% credit eligible after approval."
def file_complaint(order_id,issue):return f"Complaint recorded for {order_id}: {issue}. Reference C-{order_id}."
SCHEMAS=[
 {'name':'check_restaurant_status','description':'Check whether a restaurant is open.','parameters':{'type':'object','properties':{'name':{'type':'string'}},'required':['name']}},
 {'name':'get_estimated_delivery_time','description':'Get sample ETA for an order.','parameters':{'type':'object','properties':{'order_id':{'type':'string'}},'required':['order_id']}},
 {'name':'apply_discount','description':'Request an eligible discount; confirmation/policy is required in production.','parameters':{'type':'object','properties':{'order_id':{'type':'string'},'reason':{'type':'string'}},'required':['order_id','reason']}},
 {'name':'file_complaint','description':'Record a complaint for an order.','parameters':{'type':'object','properties':{'order_id':{'type':'string'},'issue':{'type':'string'}},'required':['order_id','issue']}}]
class FoodDeliveryAgent:
 def __init__(self):self.log=[]
 def think(self,query):
  q=query.casefold(); match=re.search(r'\b(?:FD|O)\d+\b',query,re.I); order=match.group(0) if match else 'FD4521'
  if 'discount' in q or 'credit' in q:tool='apply_discount';result=apply_discount(order,query)
  elif 'complaint' in q or 'cold' in q or 'wrong item' in q:tool='file_complaint';result=file_complaint(order,query)
  elif 'eta' in q or 'late' in q or 'delivery time' in q:tool='get_estimated_delivery_time';result=get_estimated_delivery_time(order)
  elif 'restaurant' in q or 'open' in q:tool='check_restaurant_status';result=check_restaurant_status(query.replace('Is ','').replace(' open?',''))
  else:tool='get_estimated_delivery_time';result=get_estimated_delivery_time(order)
  self.log.append((query,tool,result));return result
if __name__=='__main__':
 print('Schemas:')
 print(json.dumps(SCHEMAS,indent=2))
 agent=FoodDeliveryAgent()
 queries=['Is Saravana Bhavan open?','Where is order FD4521?','My order O77 is late, ETA?','File complaint FD4521 cold food','Can I get a discount on FD4521?']
 for q in queries:
  print('Q:',q)
  print('A:',agent.think(q))
 print('Session log:')
 for row in agent.log:print(row)
