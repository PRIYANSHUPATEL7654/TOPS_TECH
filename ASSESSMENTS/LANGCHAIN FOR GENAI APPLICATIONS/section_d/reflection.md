# Section D — Test and Debug Notes

**Exact prompt:** See `ai_prompt.txt`.

**AI first draft:** `ai_original.py`. It uses `memory_key="chat_history"`, while its PromptTemplate requires `{history}`. The mismatch prevents ConversationChain from constructing with the intended prompt/memory configuration. It also answers from a fixed LLM response rather than checking the order dictionary, has no unknown-ID handling, and does not count unique IDs.

**Corrected version:** `section_d_corrected.py`. I aligned the memory key with `{history}`, added explicit input-key configuration, made the local order dictionary the authoritative source, resolves pronoun-like follow-ups from conversation history, handles unknown or absent IDs, and reports unique IDs and turn totals on `quit`.

**3–4 line reflection:** I found that the generated draft used different names for the memory variable and prompt placeholder, which breaks memory injection. I changed both to `history` and configured `input_key` explicitly. I added dictionary-backed lookup and a clear response for unknown IDs instead of trusting a generic LLM answer. Finally, I tested contextual follow-up and unique-ID counting in a terminal loop.
