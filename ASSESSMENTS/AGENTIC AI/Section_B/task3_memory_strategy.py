"""B3: user memory affects strategy choice."""
MEMORY={}
MENU={'masala dosa':'South Indian, ₹180','Gujarati thali':'Gujarati, ₹250','paneer wrap':'North Indian, ₹160'}
def prompt_template_response(query):return f"I can help with your order. Please share any missing details for: {query}"
def rag_lookup_response(query):
 hits=[f'{k}: {v}' for k,v in MENU.items() if any(w in query.casefold() for w in k.split())]
 return 'Menu results: '+('; '.join(hits) if hits else 'Dishes: '+', '.join(MENU))
def fine_tuned_response(query):return 'I am sorry about the food-delivery issue. I have recorded the complaint for review under the service policy.'
def decide_strategy(user_id,query):
 m=MEMORY.setdefault(user_id,{'interaction_count':0,'preferred_cuisine':None,'last_complaint':None})
 q=query.casefold()
 if any(w in q for w in ['complaint','cold','late','wrong item']) and m['interaction_count']>=3:name='fine_tuned';response=fine_tuned_response(query);m['last_complaint']=query
 elif any(w in q for w in ['menu','dish','item','recommend','food']):name='rag_lookup';response=rag_lookup_response(query)
 else:name='prompt_template';response=prompt_template_response(query)
 for cuisine in ['Gujarati','South Indian','North Indian']:
  if cuisine.casefold() in q:m['preferred_cuisine']=cuisine
 m['interaction_count']+=1
 return name,response
if __name__=='__main__':
 questions=['How can I place an order?','Show me the menu','Which dish is available?','My food arrived cold and late','Recommend Gujarati food']
 for q in questions:
  strategy,response=decide_strategy('U-42',q);print(q,'->',strategy,':',response);print('Memory:',MEMORY['U-42'])
