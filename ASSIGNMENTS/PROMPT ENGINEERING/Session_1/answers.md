# Session 1 - Prompt Basics

## 1. Unclear and clear song prompts
- **Unclear:** “List trending songs in India.” It does not specify date range, language, platform, format, or whether “trending” means streams or social media.
- **Clear:** “Give me 10 Bollywood songs released from 1 January 2023 through 31 December 2025. Include song title, film or album, artist names, and release year in a table. Do not call them currently trending unless you can cite a current chart and date.”
- **Comparison:** The second request constrains scope and output and distinguishes a historical release list from a live ranking. This avoids invented trend claims.

## 2. Three prompt mistakes
| Mistake | Don't | Do |
|---|---|---|
| Vague request | “Order food.” | “Suggest three vegetarian dinner options under ₹300 near my selected delivery address; ask before placing an order.” |
| Missing constraints | “Find a movie.” | “Show Hindi comedy films starting after 7 p.m. today at the selected cinema; list showtime and ticket price if available.” |
| Bundling unrelated jobs | “Pick food, book a movie, and plan travel.” | “First compare dinner options. Return the top three with price and delivery estimate; wait for my choice.” |

## 3. Café review prompt comparison
- **Vague prompt:** “Write a review for a new cafe.”
- **Illustrative output:** “A lovely new cafe with a welcoming feel and tasty drinks. A nice place to relax or meet friends.”
- **Detailed prompt:** “Write a 70-word first-person sample review of an imaginary Ahmedabad cafe serving Gujarati-inspired brunch and specialty coffee. Describe a bright, relaxed ambience and ₹250-₹450 per-person pricing. Do not claim personal visit or real business facts; label it as a fictional sample.”
- **Illustrative output:** “Sample review: The imaginary cafe pairs Gujarati-inspired brunch with carefully made coffee in a bright, relaxed space. The menu feels playful without losing familiar flavors, and the ₹250-₹450 range makes it a comfortable occasional brunch stop. I would highlight the seasonal snacks and calm seating for a long catch-up. This is a fictional example, not a review of a real visit.”
- The detailed version is more useful because it names the cuisine, mood, audience, price range, length, and truthfulness limits.

## 4. Recommendation feature prompt
“Act as a recommendation copywriter for a music app. Using only the listening-history summary I provide, write three short playlist recommendations. For each, give a title, one-sentence reason, and two seed genres. Do not infer sensitive traits or claim a song is available unless it appears in my catalog. Ask one question if the history is insufficient.”
