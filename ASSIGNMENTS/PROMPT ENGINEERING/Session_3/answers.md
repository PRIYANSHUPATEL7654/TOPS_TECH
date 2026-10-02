# Session 3 - Zero-Shot, One-Shot, and Few-Shot Prompting

## 1. Zero-shot latest IPL match
**Prompt:** “Summarize the latest completed IPL match in one sentence. Verify the match date and result from the official IPL results page; if the page does not show a completed match, say that you cannot verify one.”

**Response for this submission:** “Royal Challengers Bengaluru beat Gujarat Titans by five wickets in the IPL 2026 final on 31 May 2026.” The official IPL match report identifies RCB as the winner. Source: https://www.iplt20.com/news/article/tata-ipl-2026-final-rcb-v-gt-match-report (accessed 2 October 2026).

## 2. One-shot Zomato review
**Prompt:** “Format example: ‘Crispy dosa, bright chutneys, and quick service made this a satisfying breakfast.’ Now write a similar 35-45 word review for an imaginary dosa restaurant in Ahmedabad. Avoid claiming a real visit or inventing a business name; label it as a sample.”

**Sample response:** “Sample review: Golden, crisp dosas arrive with coconut chutney and tangy sambar in this imaginary Ahmedabad eatery. The menu keeps familiar South Indian flavors front and center, while quick, friendly service makes it an easy choice for a relaxed breakfast.”

## 3. Few-shot product descriptions
**Prompt:** “Use the tone and format in these examples. Mobile: ‘A bright display and dependable battery make everyday browsing simple.’ Headphones: ‘Soft ear cups and balanced sound keep long listening sessions comfortable.’ Shoes: ‘A cushioned sole and breathable upper support all-day movement.’ Now describe a smartwatch in the same style. Do not claim unprovided specifications.”

**Output:** “A clear watch face and comfortable strap make everyday notifications easy to check.”

## 4. Playlist description comparison
- **Zero-shot:** “Write a description for a Spotify playlist called Monsoon Vibes.” → “Songs for rainy days, quiet moments, and a little daydreaming.”
- **One-shot:** Providing one sample playlist description first produced a similarly structured short description, with a mood and use case.
- **Few-shot:** Three examples of playlist copy guided the model to match the chosen length, tone, and pattern most consistently.
- **Conclusion:** Few-shot is most relevant when style consistency matters; zero-shot is fastest when only a basic description is needed.
