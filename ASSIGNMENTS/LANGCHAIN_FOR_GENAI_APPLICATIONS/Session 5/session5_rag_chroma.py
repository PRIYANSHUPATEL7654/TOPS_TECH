"""Session 5: Chroma + sentence-transformer RAG demo. First run may download the embedding model."""
from pathlib import Path
REVIEWS=["The paneer pizza was cheesy, fresh, and delicious.","Best spicy biryani I have ordered this month.","The dosa was crisp and the coconut chutney tasted fresh.","Tasty noodles with generous vegetables and quick delivery.","The chocolate brownie was warm, rich, and soft."]
FACTS=["Paneer tikka is marinated paneer grilled with spices.","Masala dosa is a crisp rice-lentil crepe served with potato filling.","Biryani is a seasoned rice dish layered with vegetables or meat.","Hakka noodles are stir-fried noodles often served with vegetables.","A brownie is a baked chocolate dessert with a dense texture.","Idli is a steamed savory cake made from fermented rice and lentil batter.","Samosa is a fried pastry commonly filled with spiced potatoes.","Lassi is a yogurt-based drink that may be sweet or salted.","Gulab jamun is a milk-solid dessert served in syrup.","Tandoori dishes are cooked with spices, traditionally in a clay oven."]
def main():
    try:
        from langchain_chroma import Chroma
        from langchain_community.embeddings import HuggingFaceEmbeddings
        emb=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db=Chroma(collection_name="quickbite_reviews",embedding_function=emb,persist_directory=str(Path(__file__).resolve().parents[1]/"chroma_db"))
        if db._collection.count()==0: db.add_texts(REVIEWS)
        q=input("Food query (e.g. best pizza): ") or "best pizza"
        hits=db.similarity_search(q,k=1)
        print("Most relevant review:",hits[0].page_content)
        print("RAG improves grounding by retrieving relevant menu facts/reviews before generation; a plain model can lack current/local evidence.")
    except Exception as e:
        print("Vector dependencies/model unavailable:",e)
        print("Install requirements; fallback review:",REVIEWS[0])
    print("Knowledge file facts:\n- " + "\n- ".join(FACTS))
if __name__=="__main__": main()
