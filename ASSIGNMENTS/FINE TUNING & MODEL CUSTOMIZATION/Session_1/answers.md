# Session 1 - Fine-Tuning Introduction and Why Fine-Tune

1. **Restaurant review classification:** Fine-tuning on consistently labeled local-language reviews can improve sentiment and complaint labels for regional phrasing.
2. **Support intent routing:** Fine-tuning on reviewed support examples can map domain-specific wording to actions such as refund, missing item, or late delivery.
3. **Recommendation explanations:** Fine-tuning can make explanations follow a chosen concise style and use domain terminology, while a separate recommender supplies current items.

| Aspect | Pre-trained model | Fine-tuned model |
|---|---|---|
| Task fit | General language patterns | Adapted to labeled examples for the target task |
| Accuracy/relevance | Can miss domain labels or slang | May improve on representative, well-labeled domain data; not guaranteed |
| User experience | Generic or inconsistent outputs | Can use more consistent task-specific behavior |
| Cost and maintenance | Lower setup; still needs evaluation | Data curation, training, evaluation, and versioning required |

For a support chatbot that must classify local product-specific issue labels reliably, prompt changes alone may not teach a general model the distinctions present in hundreds of adjudicated examples. Fine-tuning is reasonable when the labels and examples are stable; current order status still belongs in a database or tool.

For regional Gujarati song recommendations, use **RAG plus a recommender**: retrieve a current, licensed catalog and user-approved preference signals so available songs and regional metadata stay up to date. Fine-tuning can improve style or language behavior later, but it is not the right source of changing catalog facts.

**Customization prompt example:** “Recommend Gujarati dishes using only this menu: [menu]. Ask about spice preference and dietary restrictions before recommending. Use a warm, concise tone and do not invent availability.” Fine-tuning can make this behavior more consistent across many examples; it does not make the model know the current menu.
