# Section B task files

- B1: `quickbite/train_model.py` trains/evaluates Joblib model, confirms identical predictions.
- B2: `quickbite/api.py` loads once at import/startup; run `python -m quickbite.api`; test success and missing fields with `python -m quickbite.test_api`.
- B3: `streamlit run assessment/section_b/task_b3_dish_description.py`; uses configured OpenAI-compatible or Ollama endpoint, prints prompt, spinner, result, count, Regenerate. Demo mode works without credentials.
- B4: `python assessment/task_b4_memory_chain.py`; five preloaded turns, then interactive loop; `exit` prints turn count and memory dump. ConversationBufferMemory and prompt history key are explicit.
