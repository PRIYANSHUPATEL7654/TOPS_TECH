import unittest
from task1_technique_decision import recommend_technique
from task2_delivery_agent import FoodDeliveryAgent
from task3_memory_strategy import MEMORY,decide_strategy
from task4_lifecycle import Coordinator
class AssessmentChecks(unittest.TestCase):
 def test_techniques(self):
  self.assertEqual(recommend_technique('high','yes','no','low')['technique'],'RAG')
  self.assertEqual(recommend_technique('low','no','yes','high')['technique'],'Fine-Tuning')
  self.assertEqual(recommend_technique('low','no','no','low')['technique'],'Prompt Engineering')
 def test_all_tool_routes(self):
  a=FoodDeliveryAgent()
  for q in ['restaurant open','FD4 ETA','late discount FD4','complaint cold FD4']:a.think(q)
  self.assertEqual({row[1] for row in a.log},{'check_restaurant_status','get_estimated_delivery_time','apply_discount','file_complaint'})
 def test_memory_boundary(self):
  MEMORY.pop('test-user',None)
  self.assertEqual(decide_strategy('test-user','my order is late')[0],'prompt_template')
  decide_strategy('test-user','menu')
  decide_strategy('test-user','menu')
  self.assertEqual(decide_strategy('test-user','late delivery complaint')[0],'fine_tuned')
 def test_lifecycle_strategy_changes(self):
  c=Coordinator();positive=c.run_lifecycle({'order_id':'A'},'Great, thanks');complaint=c.run_lifecycle({'order_id':'B'},'Food arrived cold')
  self.assertEqual(positive['technique_selected'],'prompt');self.assertEqual(complaint['technique_selected'],'rag');self.assertEqual(positive['simulated_processing_seconds'],0.9)
if __name__=='__main__':unittest.main(verbosity=2)
