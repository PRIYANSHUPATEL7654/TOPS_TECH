import numpy as np

sentences=["Fresh food arrived", "The order was late", "Great taste and service"]
# Small fixed 3-dimensional vectors make the calculation reproducible and interpretable.
embeddings=np.array([[1.0,.2,.1],[.1,1.0,.2],[.7,.3,.8]])
Q=embeddings[0:1]; K=embeddings; V=embeddings
scores=(Q @ K.T)/np.sqrt(K.shape[1])
weights=np.exp(scores-scores.max(axis=1,keepdims=True)); weights/=weights.sum(axis=1,keepdims=True)
context=weights @ V
for text,weight in zip(sentences,weights[0]): print(f"attention({sentences[0]!r} -> {text!r}) = {weight:.3f}")
print("Weighted context vector:",context.round(3).tolist())
print("Interpretation: larger weights mean the query assigns more influence to that key in this toy example.")
