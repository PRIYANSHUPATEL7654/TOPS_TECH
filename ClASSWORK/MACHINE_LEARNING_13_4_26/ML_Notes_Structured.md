# Machine Learning Notes
**Structured | Corrected | Enhanced with Real-life Examples**

Date-wise organization preserved from original notes.  
Corrections applied for accuracy • Missing concepts filled • Clear examples + real-world analogies added.  
Progress markers show where each topic sits in the overall ML landscape.  
A complete ML tree appears at the end.

---

## 13/3/2026 – AI Landscape Overview

**Artificial Intelligence (AI)** is the broad field of making machines perform tasks that normally require human intelligence.

1. **Machine Learning (ML)**  
   Algorithms that learn patterns from data instead of being explicitly programmed.  
   - **Supervised Learning**: Labeled data (input + correct output).  
   - **Unsupervised Learning**: Unlabeled data (find hidden structure).  
   - **Reinforcement Learning**: Agent learns by trial-and-error with rewards/penalties  
     *(Examples: self-driving cars, game-playing robots, recommendation engines that adapt to user clicks)*.

2. **Deep Learning (DL)**  
   Subset of ML using multi-layer neural networks. Dominates image, speech and complex pattern tasks.

3. **Generative AI (Gen AI)**  
   Models that create new content (text, images, code).  
   Public-facing examples: ChatGPT, Grok, Gemini, Midjourney.

4. **Agentic AI**  
   Autonomous systems that plan, use tools and complete multi-step workflows. Used inside companies for automation. Requires strong Python backend knowledge.  

   Typical pipeline:  
   `AI model (end-to-end) → API → Docker + GitHub Actions/Jenkins → Deploy server → Frontend calls the AI`

**Real-life analogy**:  
Traditional software is a recipe you follow step-by-step.  
ML is a chef who tastes the dish and adjusts.  
Gen AI is a chef who invents new recipes.  
Agentic AI is a full kitchen team that orders ingredients, cooks and serves without constant supervision.

**Progress in whole ML**: ~5% – high-level map of the field established.

---

## 15/3/2026 – Machine Learning Lifecycle

1. Problem definition  
2. Data collection  
3. Preprocessing (cleaning raw data – missing values, outliers, duplicates)  
4. Exploratory Data Analysis (EDA) – discover patterns, distributions, correlations  
5. Feature Engineering – create new useful columns from existing ones  
6. Model selection  
7. Train/Test split (commonly 80/20 or 70/30)  
8. Evaluation (accuracy, R², F1, etc.)  
9. Deployment  
10. Monitoring (model drifts when new live data arrives; retrain when performance drops)

**Realtime example**: Netflix recommendation system – problem = “what to show next”, data = watch history, continuous monitoring because user tastes change.

**Progress in whole ML**: ~10% – end-to-end process understood.

---

## 17/4/2026 – Supervised Learning Fundamentals

**Supervised Learning** uses labeled data (both input features and target output are known).

### 1. Regression (continuous numeric output)

- **Simple Linear Regression**  
  \( y = mx + c \)  
  (or more standard: \( y = \beta_0 + \beta_1 x \))

  **Example**:  
  Experience (years) → Salary  
  1 → 20k, 2 → 25k, 3 → 30k → slope \( m = 5k \) per year.

- **Overfitting**: Model memorizes training data → excellent train score, poor test score.  
- **Underfitting**: Model is too simple → poor performance on both train and test.

**Column names** in ML are called **features** (inputs) or **labels/targets** (outputs).

**Encoding** (text → numbers because models work with numbers only):

- **Label Encoding**: Assigns integers alphabetically or by order  
  (Ahmedabad=0, Patan=1, Surat=2).  
  *Risk*: implies ordinal relationship that may not exist.

- **One-Hot Encoding**: Creates binary columns for each category (no false ordinality).  
  Produces sparse matrices; convert with `.toarray()` when needed.

**Epoch** = one full pass through the training data.  
**random_state** = seed for reproducible train/test splits (common value 42).

### 2. Classification (categorical output – Yes/No, Spam/Not Spam, etc.)

**Real-life examples**:
- **Regression** → House price prediction, stock price forecasting, temperature prediction.  
- **Classification** → Email spam filter, medical diagnosis (disease/no disease), loan approval (approve/reject).

**Progress in whole ML**: ~20% – core supervised paradigm + basic regression/classification + encoding.

---

## 20/4/2026 – Evaluation Metrics

**Error** = Actual − Predicted.

- **MSE (Mean Squared Error)**: Average of squared errors. Lower is better.  
  No fixed “good” range – depends on target scale.  
- **RMSE**: Square root of MSE (same units as target).  
- **R² (Coefficient of Determination)**: Proportion of variance explained (0–1). 1 = perfect.  
  *(Note: R² is for regression; classification uses Accuracy, Precision, Recall, F1.)*

**Confusion Matrix** (Classification):

|                  | Predicted Positive | Predicted Negative |
|------------------|--------------------|--------------------|
| **Actual Positive** | TP                 | FN                 |
| **Actual Negative** | FP                 | TN                 |

**Ways to improve low performance**: better data, better features, different model, hyper-parameter tuning, more data.

**Realtime example**: Credit-card fraud detection – high cost of False Negatives (missed fraud) vs False Positives (false alarms).

**Progress in whole ML**: ~25% – evaluation toolkit for supervised models.

---

## 22/4/2026 – Data Shape & Basic Pipeline

- Inputs (**X**) are 2-D (samples × features).  
- Targets (**y**) are 1-D.  
- Classic flow: \( X \) → model (\( y = mx + c \) or more complex) → \( \hat{y} \).

Advanced steps: custom Pipeline (sklearn Pipeline or custom), expose model via API, build Streamlit/Gradio UI.

**Progress in whole ML**: ~28%.

---

## 29/4/2026 – Deployment & DevOps Basics

Two deployment styles:

1. **Manual**: change code → rebuild → redeploy on server (AWS, etc.).  
2. **Automated CI/CD pipeline** (GitHub Actions or Jenkins):  
   push → build → test (unit + integration + e2e) → smoke/sanity tests → deploy.

**Requirements.txt** pins library versions.  
**Docker** = OS-level virtualization (image contains code + dependencies).  
**Kubernetes** manages many containers.

**Architecture**:
- **Monolithic**: one codebase, one server, one database (multiple APIs possible).  
- **Microservices**: separate services  
  *(Zomato example: customer, restaurant, rider, admin – each with own server)*.

**Progress in whole ML**: ~32% – models can now leave the notebook and reach users.

---

## 1/5/2026 – Testing & Server Concepts

- **Testing Server** → all tests run here.  
- **Production Server** → live traffic.  

**Alpha testing**: internal company users.  
**Beta testing**: limited external users.  

**CORS**: solves browser cross-origin conflicts (frontend port 4000 ↔ backend port 8000).

Monitoring: errors written to log files → investigated.

**Progress in whole ML**: ~35%.

---

## 4/5/2026 – Practical Deployment Flow (Render + GitHub Actions + Docker)

Typical sequence:

- Create `requirements.txt`, `Dockerfile`, `.github/workflows/deploy.yml`.  
- Generate Docker personal access token.  
- Store secrets in GitHub (Docker username + token, Render deploy hook).  
- Push → automated build & deploy on Render.

**Progress in whole ML**: ~37%.

---

## 8/5/2026 – Multiple Linear Regression & Classification Internals

**Multiple Linear Regression** (more than one feature):  
\[ y = b_0 + b_1 x_1 + b_2 x_2 + \dots + b_n x_n \]

Training loop (gradient descent intuition):

1. Initialize weights.  
2. Forward pass → prediction.  
3. Compute loss.  
4. Backward pass → update weights.  
5. Repeat for many epochs.

**Classification threshold**: usually 0.5 (sigmoid output ≥ 0.5 → positive class).

**Learning rate (α)**: step size (0.1 common; too high → unstable, too low → slow).

**Batch size**: number of samples processed before weight update.  
**Epoch**: full pass over dataset.

In pure linear models input connects directly to output.  
Neural networks insert hidden layers with weights.

**Progress in whole ML**: ~42% – multi-feature regression + basic optimization concepts.

---

## 11/5/2026 – Feature Scaling & Logistic Regression

**StandardScaler**:  
\[ z = \frac{x - \mu}{\sigma} \]  

Brings features to mean 0, std 1 so no feature dominates because of scale  
*(age 30 vs blood pressure 180 vs sugar 350)*.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy_score(y_test, y_pred)
```

- Regression → `r2_score`  
- Classification → `accuracy_score` (also Precision / Recall / F1)

**Realtime example**: Medical diagnosis model – age, BP, glucose must be scaled so the model does not ignore age.

**Progress in whole ML**: ~48%.

---

## 15/5/2026 – Regularization Techniques (Neural Nets)

**Dropout**: randomly turn off neurons during training → reduces co-adaptation → fights overfitting.  
**Data Augmentation**: artificially expand dataset (rotate/flip images, synonym replacement for text).

**Progress in whole ML**: ~50%.

---

## 18/5/2026 – Types of Chatbots

1. **Static / Rule-based**: if-else conditions.  
2. **Agentic AI**: LangChain (single agent), LangGraph, CrewAI (multi-agent).  
3. **RAG-based**: Retrieval-Augmented Generation (retrieve relevant documents then generate answer).

**Progress in whole ML**: ~52% (application layer).

---

## 25/5/2026 – 28/5/2026 – Decision Trees

**Decision Tree**: recursively split data on the feature that best separates the target.

**Gini Impurity** (binary):  
\[ Gini = 1 - (p_1^2 + p_2^2) \]  
Range 0 (pure) → 0.5 (most impure for binary). Lower = better split.

**Entropy**:  
\[ Entropy(S) = -\sum p_i \log_2(p_i) \]  
Range 0 (pure) → 1 (maximum impurity for binary).

**Information Gain** = Parent Entropy − Weighted Child Entropy.  
Highest IG feature becomes the root (or next split).

**Real-life example**: Loan approval tree – first question might be “Credit Score > 700?”, then “Income stable?”, etc.

- Gini is computationally cheaper (preferred for large data in practice).  
- Entropy is information-theoretic.

**Progress in whole ML**: ~58% – first non-linear, interpretable supervised model.

---

## 2/6/2026 – K-Nearest Neighbors (KNN)

Distance (Euclidean):  
\[ d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \]

Choose odd \( k \), take majority vote of the \( k \) nearest training points.

**Advantages**: no explicit training phase, works well on small data.  
**Disadvantages**: slow on large data, sensitive to feature scale → must scale.

**Feature Scaling for KNN**:
- **Min-Max**: \( \dfrac{x - \min}{\max - \min} \) → [0,1]  
- **Standardization**: same as StandardScaler.

**Realtime example**: “Customers similar to you also bought…” (recommendation systems).

**Progress in whole ML**: ~62%.

---

## 3/6/2026 – 5/6/2026 – Ensemble Methods

**Random Forest** = Bagging of many Decision Trees + majority vote (classification) or average (regression).  
Uses bootstrap sampling (random subsets with replacement).  
Key hyper-parameters: `n_estimators` (number of trees), `max_depth`.

**XGBoost (Extreme Gradient Boosting)** = sequential boosting.  
Each new tree corrects the residual errors of previous trees.  
Usually higher accuracy than Random Forest.  
Learning rate (η) commonly 0.1; smaller values need more trees.

**Bagging vs Boosting**:
- **Bagging**: trees independent → reduce variance.  
- **Boosting**: trees sequential → reduce bias.

**Hyper-parameter tuning**: systematically search `n_estimators` (50–200+), `max_depth`, learning rate, etc.

**Task idea from notes**: daily stock-price prediction with XGBoost + Alpha Vantage API → frontend dashboard.

**Progress in whole ML**: ~70% – powerful ensemble methods mastered.

---

## Unsupervised Learning (introduced ~5/6 & expanded 29/6)

No labels. Goal = discover structure.

### 1. Clustering

- **K-Means**: choose \( k \) centroids, assign points to nearest centroid, update centroids until stable.  
  Best when number of clusters is known / data volume is large.

- **Hierarchical**:
  - Agglomerative (bottom-up): start with each point as cluster → merge closest.
  - Divisive (top-down).  
  Visualized by dendrogram.  
  Linkage methods: Single (min), Complete (max), Average, Ward (variance).  
  Prefer when number of clusters is unknown or data is small.

- **DBSCAN**: density-based.  
  Parameters: `eps` (neighborhood radius), `min_samples`.  
  Discovers arbitrary shapes + marks noise/outliers.

### 2. Association (Market Basket Analysis)

“People who bought X also bought Y” (Apriori, FP-Growth).

**Real-life examples**:
- **K-Means** → customer segmentation (Jio plans, retail shopping behavior).  
- **Hierarchical** → gene clustering, document taxonomy.  
- **DBSCAN** → anomaly detection (fraud, sensor faults).  
- **Association** → Amazon “Frequently bought together”.

**Progress in whole ML**: ~78% – unsupervised branch opened.

---

## 16/6/2026 – 17/6/2026 – Neural Networks, NLP & Modern Stack

**ANN** – feed-forward, no memory.  
**RNN** – has memory (hidden state). Suffers from vanishing/exploding gradients on long sequences.  
**LSTM/GRU** (extensions) solve vanishing gradient.  
**Transformer** – attention mechanism; remembers all positions; basis of modern LLMs.  
Encoder (input) + Decoder (output).

**CNN** – convolution filters for images/video (multiple passes).  
**YOLO** – single-pass object detection  
*(real-time traffic cameras, number-plate recognition for challans)*.

**NLP pipeline basics**: tokenization, stemming/lemmatization, stop-word removal.

**Hugging Face**: open-source model hub – download, fine-tune, deploy.

**RAG**: retrieve relevant chunks from a vector database (embeddings) then feed to LLM.  
Works on static knowledge bases.

**Fine-tuning**: adapt a pre-trained LLM to domain-specific data (company policies, product catalog).

**Framework notes**: FastAPI (modern, async), Flask, Django.  
REST (lightweight) vs SOAP (heavier, more formal).

**Progress in whole ML**: ~88% – deep learning & generative stack introduced.

---

## 24/6/2026 – Supporting Knowledge (SQL)

Normalization, ACID, indexing – important for clean data pipelines that feed ML models.

**Progress in whole ML**: ~90%.

---

## 29/6/2026 – Clustering Decision Guide & DBSCAN Details

- Large data + known \( k \) → **K-Means**.  
- Small data or unknown \( k \) → **Hierarchical**.  
- Arbitrary shapes + noise → **DBSCAN** (`eps`, `min_samples`).  

`fcluster` can cut a dendrogram into a desired number of clusters.

**Progress in whole ML**: ~92%.

---

## Complete Machine Learning Tree  
*(Supervised + Unsupervised focus)*

```
Machine Learning
├── Supervised Learning (Labeled data)
│   ├── Regression (Continuous target)
│   │   ├── Linear Regression (Simple & Multiple)
│   │   ├── Polynomial Regression
│   │   ├── Ridge / Lasso / ElasticNet
│   │   └── Tree-based (Decision Tree, Random Forest, XGBoost, LightGBM…)
│   └── Classification (Categorical target)
│       ├── Logistic Regression
│       ├── K-Nearest Neighbors (KNN)
│       ├── Decision Tree / Random Forest / XGBoost
│       ├── Support Vector Machines (SVM)
│       ├── Naïve Bayes
│       └── Neural Networks (ANN, CNN for images)
│
├── Unsupervised Learning (Unlabeled data)
│   ├── Clustering
│   │   ├── K-Means
│   │   ├── Hierarchical (Agglomerative / Divisive)
│   │   ├── DBSCAN
│   │   └── Gaussian Mixture Models
│   ├── Dimensionality Reduction
│   │   ├── PCA, t-SNE, UMAP
│   └── Association Rule Learning
│       └── Apriori, FP-Growth
│
├── Semi-supervised & Self-supervised
├── Reinforcement Learning
│   └── Q-Learning, Policy Gradients, PPO, etc.
│
└── Deep Learning / Generative
    ├── ANN, CNN, RNN/LSTM, Transformers
    ├── Generative Models (GANs, Diffusion, LLMs)
    ├── RAG, Fine-tuning, Agentic systems
    └── Computer Vision (YOLO, etc.) & NLP
```

## Complete Machine Learning Tree  

Machine Learning
│
├── Supervised Learning
│   ├── Regression
│   │   ├── Linear Regression (Simple & Multiple)
│   │   ├── Polynomial Regression
│   │   ├── Ridge / Lasso / ElasticNet
│   │   ├── Support Vector Regression (SVR)
│   │   ├── Decision Tree / Random Forest / Gradient Boosting / XGBoost / LightGBM / CatBoost
│   │   └── Neural Networks (ANN, DNN)
│   │
│   └── Classification
│       ├── Logistic Regression
│       ├── K-Nearest Neighbors (KNN)
│       ├── Naive Bayes
│       ├── Support Vector Machines (SVM)
│       ├── Decision Tree / Random Forest / Gradient Boosting / XGBoost / LightGBM / CatBoost
│       └── Neural Networks (ANN, DNN, CNN for images)
│
├── Unsupervised Learning
│   ├── Clustering
│   │   ├── K-Means / K-Medoids
│   │   ├── Hierarchical (Agglomerative & Divisive)
│   │   ├── DBSCAN / HDBSCAN
│   │   ├── Gaussian Mixture Models (GMM)
│   │   └── Spectral Clustering
│   │
│   ├── Dimensionality Reduction
│   │   ├── PCA (Principal Component Analysis)
│   │   ├── t-SNE
│   │   ├── UMAP
│   │   ├── Autoencoders
│   │   └── ICA / LDA
│   │
│   └── Association Rule Learning
│       ├── Apriori
│       └── FP-Growth
│
├── Semi-Supervised Learning
│   ├── Self-Training
│   ├── Co-Training
│   ├── Label Propagation / Label Spreading
│   └── Graph-based methods
│
├── Self-Supervised Learning
│   ├── Contrastive Learning (SimCLR, MoCo, CLIP)
│   ├── Masked Language / Image Modeling
│   └── Predictive Coding
│
├── Reinforcement Learning
│   ├── Value-Based (Q-Learning, DQN, Double DQN, Rainbow)
│   ├── Policy-Based (REINFORCE, Policy Gradient)
│   ├── Actor-Critic (A2C, A3C, PPO, SAC, TD3)
│   └── Multi-Agent RL
│
├── Deep Learning
│   ├── Feedforward Networks (ANN / MLP)
│   ├── Convolutional Neural Networks (CNN)
│   ├── Recurrent Networks (RNN, LSTM, GRU)
│   ├── Transformers (Encoder, Decoder, Encoder-Decoder)
│   ├── Graph Neural Networks (GNN)
│   └── Attention Mechanisms
│
├── Generative Models
│   ├── Generative Adversarial Networks (GANs)
│   ├── Variational Autoencoders (VAE)
│   ├── Diffusion Models
│   ├── Autoregressive Models
│   └── Large Language Models (LLMs) & Multimodal Models
│
├── Ensemble Methods
│   ├── Bagging (Random Forest, etc.)
│   ├── Boosting (AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost)
│   └── Stacking / Blending
│
└── Specialized / Applied Areas
    ├── Natural Language Processing (NLP)
    ├── Computer Vision
    ├── Speech & Audio
    ├── Recommendation Systems
    ├── Time Series Forecasting
    ├── Anomaly Detection
    ├── MLOps & Model Deployment
    └── Agentic Systems / Tool-using Agents

---

### Current Coverage Summary

From your notes you now have a **solid foundation** in:

- Supervised Learning (Linear / Logistic Regression, Decision Trees, Ensembles, KNN)
- Unsupervised Clustering (K-Means, Hierarchical, DBSCAN)
- Introduction to Neural Nets, Transformers, RAG and production deployment

**Remaining major areas** for future study:  
SVM, PCA / dimensionality reduction, advanced boosting variants, full Transformer architecture internals, Reinforcement Learning, and large-scale MLOps.

---

*These notes are corrected, enriched with intuition + real-world anchors, and mapped onto the bigger ML map.  
Treat this as a living document – keep adding new dates as you progress.*
