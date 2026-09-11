# Section A - Concept Application

## S1 - Clear versus unclear prompts

An unclear prompt says something broad such as “Handle this refund.” It leaves the order-status check, eligibility rules, response format, and uncertain cases unspecified. A clear prompt assigns a support role, supplies the order facts and policy, lists decision rules in priority order, and requires a predictable schema such as `decision`, `reason`, and `next_step`.

Two changes: first, add explicit rules: verify order status and payment before approving; approve only when the policy condition is met; otherwise request the missing information or reject with a reason. This prevents inconsistent decisions. Second, require a fixed output format and a word limit, for example JSON with three fields and no extra text. This makes the response easier to validate and display. I would also include a few examples of valid and invalid cases and instruct the model to escalate uncertain cases.

## S2 - Zero-shot versus few-shot

Zero-shot gives only the category definitions and asks the model to classify. It is quick and uses little context, but the model may interpret boundaries differently. Few-shot includes representative Input/Output examples, showing exactly how labels such as “Wrong Item” and “Missing Item” differ. With 200 labelled examples but a limited context window, I would select a compact few-shot set rather than include all 200. The examples should be diverse, clear, balanced across four labels, and close to the language used in real messages. The number depends on context-window size, example length, label complexity, expected accuracy, and the point where extra examples stop improving validation results.

## S3 - Chain-of-Thought prompting

For route planning, asking the model to consider each stop's travel time, traffic delay, priority, and constraints in an ordered analysis can reduce skipped inputs and improve the final route. A prompt can say: “List the five stops and their priority; estimate the adjusted travel cost for each possible next stop; apply the highest-priority constraints; verify that every stop appears exactly once; then return the route and a concise justification.” One limitation is that step-by-step reasoning is not a guarantee of mathematical correctness; the model can still make arithmetic or map-distance errors. A routing algorithm or maps API should verify the result.

## S4 - RAG over fine-tuning

RAG is better for a 150-page handbook updated every quarter because new or corrected text can be re-ingested and indexed without retraining the model. Retrieval also gives the answer a direct source context, which makes policy answers easier to audit. Fine-tuning changes model behavior and style, but it is a poor mechanism for frequently changing factual content and can preserve obsolete rules until another training cycle. Fine-tuning would be better when the policy facts are stable but the organization needs a consistent specialized output style or classification behavior learned from many labelled examples.

## S5 - Chunk size and overlap

Chunk size controls how much context is stored and retrieved at once. Overlap repeats the end of one chunk at the start of the next so a sentence or related paragraph is less likely to be separated. Here I would increase chunks from a very small size to roughly 150-250 words and use 30-50 words of overlap, while keeping paragraph boundaries when possible. This gives the dish name and nearby price more opportunity to appear together. The trade-off is more stored vectors, slower indexing/search, and potentially more irrelevant context in the final prompt.

## S6 - FAISS versus ChromaDB

FAISS is a fast library for similarity search and is a good fit for a local, read-heavy index embedded in an application, especially when the developer manages persistence and metadata separately. ChromaDB is a higher-level vector database that provides collections, documents, metadata, and persistence, making it convenient for prototypes and applications that need filtering and record management. Switching to ChromaDB would not automatically remove outdated FAISS records: stale data is a data-lifecycle problem, not only a storage-engine problem. Regardless of the choice, the system needs deletion or update logic, stable record IDs, metadata/version checks, and a rebuild or synchronization process when a complaint is resolved.
