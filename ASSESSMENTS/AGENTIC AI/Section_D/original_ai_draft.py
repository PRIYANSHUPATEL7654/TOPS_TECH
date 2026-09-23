"""AI first draft supplied for Section D; contains a bug intentionally exposed by test."""
ORDERS={'FD1001':{'status':'Delivered','minutes_late':42,'cold':True}}
def lookup_order_status(order_id):
 order=ORDERS.get(order_id)
 return order if order else {'error':'ORDER_NOT_FOUND'}
def check_refund_eligibility(order_id,issue):
 order=ORDERS.get(order_id)
 if not order:return {'error':'ORDER_NOT_FOUND'}
 return {'eligible':order['minutes_late']>=30 or order['cold'],'credit_percent':20}
def run_agent(order_id,complaint):
 print('Cycle 1 — Thought: verify the order before choosing a remedy.')
 print('Action: lookup_order_status',order_id);status=lookup_order_status(order_id);print('Observation:',status)
 print('Cycle 2 — Thought: check the policy using the order result.')
 print('Action: check_refund_eligibility',order_id);eligibility=check_refund_eligibility(order_id,complaint);print('Observation:',eligibility)
 # Bug: eligibility errors/false are ignored, so the draft promises a credit anyway.
 return 'We will apply a 20% credit to your next order.'
if __name__=='__main__':
 for oid in ['FD1001','FD404']:print('Final:',run_agent(oid,'late and cold'))
