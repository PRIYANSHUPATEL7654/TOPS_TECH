"""B4: coordinator orders Order, Dispatch, Support agents."""
import json
PARTNERS=[{'name':'Partner A','eta_min':28},{'name':'Partner B','eta_min':35}]
class OrderAgent:
 def process(self,data):return {'order_id':data.get('order_id','FD1001'),'customer':data.get('customer','Guest'),'items':data.get('items',[]),'restaurant':data.get('restaurant','Sample Kitchen'),'total':data.get('total',300),'status':'placed'}
class DispatchAgent:
 def process(self,data):partner=min(PARTNERS,key=lambda p:p['eta_min']);return {'partner':partner['name'],'eta_minutes':partner['eta_min'],'order_id':data['order_id']}
class SupportAgent:
 def process(self,data):
  text=data.get('feedback','').casefold()
  if any(w in text for w in ['unsafe','allergy','injury','harass']):cls,tech='escalate','fine_tuned'
  elif any(w in text for w in ['late','cold','wrong','missing','bad']):cls,tech='complaint','rag'
  else:cls,tech='positive','prompt'
  return {'classification':cls,'technique':tech,'response':'We appreciate the feedback.' if cls=='positive' else 'We are reviewing the order against service policy.' if cls=='complaint' else 'A support specialist will review this safety concern.'}
class Coordinator:
 def __init__(self):self.order=OrderAgent();self.dispatch=DispatchAgent();self.support=SupportAgent()
 def run_lifecycle(self,customer_input,feedback):
  order=self.order.process(customer_input);dispatch=self.dispatch.process(order);support=self.support.process({'order':order,'dispatch':dispatch,'feedback':feedback});simulated_time_seconds=round(0.4+0.3+0.2,1);report={'order_summary':order,'dispatch_details':dispatch,'feedback_classification':support['classification'],'technique_selected':support['technique'],'support_response':support['response'],'simulated_processing_seconds':simulated_time_seconds};print(json.dumps(report,indent=2));return report
if __name__=='__main__':
 c=Coordinator();c.run_lifecycle({'order_id':'FD1001','customer':'Maya','items':['Dosa'],'restaurant':'Dosa House','total':180},'Great food, arrived on time!');c.run_lifecycle({'order_id':'FD1002','customer':'Arjun','items':['Thali'],'restaurant':'Green House','total':250},'Delivery was late and food cold.')
