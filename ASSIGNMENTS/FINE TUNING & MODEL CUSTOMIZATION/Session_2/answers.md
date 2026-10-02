# Session 2 - Prompt vs RAG vs Fine-Tuning

## Instagram bio prompt and sample
**Prompt:** “Write three Instagram bio options for a computer science college student interested in data science and building apps. Each under 90 characters; no unsupported awards or job claims.”

**Sample:** “CS student | Exploring data + AI | Building one project at a time”

## Three app scenarios
- **Prompting:** Reformat a one-off customer-support explanation or generate a short Instagram bio. The task is clear and behavior changes without training.
- **RAG:** Answer questions about current IPL statistics or a BookMyShow catalog using an indexed, updateable source. The answer can cite retrieved records.
- **Fine-tuning:** Apply a stable, domain-specific classification taxonomy or consistent response style from many curated examples, after measuring that prompting is insufficient.

| Criterion | Prompt engineering | RAG | Fine-tuning |
|---|---|---|---|
| Setup cost | Low | Medium: data ingestion, retrieval, evaluation | High: training data, compute, evaluation |
| Time to deploy | Hours to days | Days to weeks | Weeks, depending on data and training |
| Maintenance | Prompt/version review | Refresh index and monitor retrieval | Recurate data and retrain/version |
| Best use | Instructions and output format | Changing or citable knowledge | Stable behavior or task adaptation |

## BookMyShow-style recommendation advice
**Advice:** Use retrieval for the live catalog, showtimes, language, genre, and location; combine it with a ranking system that uses a user's explicit preferences. A prompt controls how recommendations are explained. Fine-tuning is optional later if a large set of high-quality examples shows a repeatable behavior gap.

**Decision:** Start with retrieval plus a transparent recommendation/ranking layer, and use prompting for conversation. This keeps current movie facts out of model memory.
