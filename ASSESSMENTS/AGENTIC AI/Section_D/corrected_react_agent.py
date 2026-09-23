"""Corrected, tested ReAct customer-support example."""
ORDERS={'FD1001':{'status':'Delivered','minutes_late':42,'cold':True}}
def lookup_order_status(order_id):
 order=ORDERS.get(order_id)
 return {'error':'ORDER_NOT_FOUND','order_id':order_id} if order is None else {'order_id':order_id,**order}
def check_refund_eligibility(order_id,issue):
 order=ORDERS.get(order_id)
 if order is None:return {'error':'ORDER_NOT_FOUND','order_id':order_id}
 eligible=order['minutes_late']>=30 or (order['cold'] and 'cold' in issue.casefold())
 return {'eligible':eligible,'credit_percent':20 if eligible else 0,'policy':'sample policy; approval required'}
def run_agent(order_id,complaint):
 print('Cycle 1 — Thought summary: verify the order and delivery record first.')
 print('Action: lookup_order_status(',order_id,')',sep='');status=lookup_order_status(order_id);print('Observation:',status)
 if status.get('error'):
  print('Next-step decision: the order was not found; verify the eligibility lookup also and ask the customer to check the ID.')
 else: print('Next-step decision: order exists; check the complaint against the refund policy.')
 print('Cycle 2 — Thought summary: check eligibility; do not promise a credit unless policy confirms it.')
 print('Action: check_refund_eligibility(',order_id,', issue=',repr(complaint),')',sep='');eligibility=check_refund_eligibility(order_id,complaint);print('Observation:',eligibility)
 if status.get('error') or eligibility.get('error'):final='I could not verify this order. Please check the order ID; no refund or credit has been applied.'
 elif eligibility.get('eligible'):final=f"The order appears eligible for a {eligibility['credit_percent']}% credit under the sample policy. A support agent must approve it before it is applied."
 else:final='The available order details do not qualify for a credit under the sample policy. I can escalate the complaint for review.'
 print('Final response:',final);return final
if __name__=='__main__':
 print('=== Known order ===');run_agent('FD1001','late and cold')
 print('=== Unknown order test ===');run_agent('FD404','late and cold')
