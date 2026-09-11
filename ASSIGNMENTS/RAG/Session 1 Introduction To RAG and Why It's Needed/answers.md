# Session 1 Answers

## 1. RAG in my own words

Retrieval-Augmented Generation (RAG) is a method where an application first searches a trusted collection of current information and then gives the most relevant pieces to a language model. The model uses that context to write its answer. The model does not have to rely only on what it learned during training.

Example: in a food-delivery app, a RAG-powered help assistant could retrieve the current restaurant menu, delivery estimate, and refund policy before answering. If a customer asks whether a dish contains peanuts, the answer can be based on the restaurant's latest menu rather than a general guess.

## 2. Questions an LLM trained in 2022 may struggle with

1. What are the current IRCTC departure and arrival times for a specific train tomorrow? The schedule may have changed after 2022.
2. Who won the IPL 2024 final and what was the score? IPL 2024 happened after the model's training period.
3. Which trains have seats available for a particular date this week? Availability is live, changing data that cannot be known from old training.

Outdated knowledge is a problem because the bot may sound confident while providing a wrong schedule, result, or availability. That can cause missed journeys, incorrect bookings, and loss of trust. A live data source or RAG connection to updated documents is needed.

## 3. Workflow

The workflow is: user query -> retrieve relevant documents -> combine the query and documents with the LLM -> generate a grounded answer. The diagram is supplied separately in Mermaid and SVG format.

## 4. Comparison

| Aspect | RAG | Fine-tuning | Prompt Engineering |
|---|---|---|---|
| Cost | Usually moderate: storage, embeddings, and retrieval; the base model is reused. | Higher: preparing data and training compute are required. | Lowest: mainly prompt design and API usage. |
| Data Freshness | Very good; update or replace documents without retraining. | Weak for frequently changing facts; retraining is normally needed. | Depends on information placed in the prompt; context must be supplied each time. |
| Use Case Example | Customer-support assistant retrieving a current refund policy. | Teaching a model a stable company writing style or classification behavior. | Asking a general LLM to return JSON with fixed fields. |
| Speed of Implementation | Medium; requires document processing and a vector index. | Slowest; requires dataset preparation, training, and evaluation. | Fastest; change the instructions and test. |

## 5. Real-world example

GitHub Copilot uses retrieval-like context gathering from the developer's open files, nearby code, and project context before generating a suggestion. This gives the model details about the current function, variable names, and repository conventions. As a result, suggestions are more relevant to the code being edited than an answer based only on general programming knowledge.
