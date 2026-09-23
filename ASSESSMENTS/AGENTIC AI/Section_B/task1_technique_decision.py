"""B1: rule-based technique selector; at least five distinct rule paths."""
def recommend_technique(update_frequency,data_in_external_docs,needs_custom_behaviour,latency_budget):
 vals=(update_frequency,data_in_external_docs,needs_custom_behaviour,latency_budget)
 if update_frequency not in {'high','low'} or data_in_external_docs not in {'yes','no'} or needs_custom_behaviour not in {'yes','no'} or latency_budget not in {'low','high'}:raise ValueError('Use high/low, yes/no, yes/no, low/high')
 if data_in_external_docs=='yes' and update_frequency=='high':
  return {'technique':'RAG','justification':'The answer depends on external information that changes frequently. Retrieval can use the latest approved menu or policy without retraining the model.'}
 if data_in_external_docs=='yes':
  return {'technique':'RAG','justification':'Authoritative external documents contain the relevant facts. Retrieval grounds responses in those documents and allows updates without changing model weights.'}
 if needs_custom_behaviour=='yes' and latency_budget=='high':
  return {'technique':'Fine-Tuning','justification':'The desired behavior is stable and domain-specific. Fine-tuning can teach consistent patterns after a representative, reviewed dataset is available.'}
 if needs_custom_behaviour=='yes':
  return {'technique':'Prompt Engineering','justification':'The behavior can be described with clear instructions and examples. Prompting is quick to change and avoids the cost of training a model.'}
 if latency_budget=='low':
  return {'technique':'Prompt Engineering','justification':'This task needs a simple response and a tight response-time budget. A short prompt avoids a retrieval step and a model-training workflow.'}
 return {'technique':'Prompt Engineering','justification':'The task is stable and does not need external documents or specialized behavior. A clear prompt is the simplest solution to test and maintain.'}
if __name__=='__main__':
 cases=[('Real-time menu recommendations','high','yes','no','low'),('Complaint categorization','low','no','yes','high'),('Order confirmation message','low','no','no','low'),('Domain FAQ','low','yes','no','high')]
 for name,*args in cases:print(name,'->',recommend_technique(*args))
