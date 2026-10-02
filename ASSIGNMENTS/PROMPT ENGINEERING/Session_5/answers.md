# Session 5 - Hallucination Handling and Real Projects

## 1. Trending Ahmedabad dishes
A chatbot may confidently name dishes without access to current Zomato rankings. Those names are not verifiable from the prompt alone, so a responsible response is: “I cannot verify live Zomato trends. Please check the app's Ahmedabad page and date the result.” This documents the hallucination risk rather than presenting a fabricated top five.

## 2. Grounded IPL 2023 final summary
**Prompt:** “Only use this text: ‘Chennai Super Kings won the IPL 2023 final against Gujarat Titans by 5 wickets.’ Do not add dates, scores, players, venue, or other details.”

**Response:** “Chennai Super Kings defeated Gujarat Titans by five wickets in the IPL 2023 final.” Every fact is supported by the provided sentence.

## 3. Product generation plus verification
**Generation prompt:** “Write a product description for a fictional wireless earbud listing. Use only these supplied facts: Bluetooth 5.3, up to 6 hours per charge, USB-C case, black color. Do not invent price, noise cancellation, warranty, or water resistance. Label it fictional.”

**Sample:** “Fictional wireless earbuds in black with Bluetooth 5.3, up to six hours per charge, and a USB-C charging case.”

**Follow-up verification:** “Is every claim in your previous answer supported by the supplied facts? List any assumptions or invented details. If none, say ‘No unsupported details found.’”

## 4. Reduced-hallucination iPhone prompt
“Using only the official Apple product page for the exact iPhone model and region linked below, summarize its listed display, camera, chip, and battery claims. Include the page URL beside each fact, state ‘not listed’ where absent, and do not compare with other models. Source: [paste official Apple URL].” This constrains the source and requires traceable claims.

## 5. Movie summary with citations
**Prompt:** “Summarize the supplied movie page in 3 sentences. After each factual sentence, cite the exact source URL and section. Use only that source; if a fact is absent, write ‘source not found’ instead of guessing.”

**Test response for a blank source:** “Source not found: no movie page URL or source text was supplied, so a factual summary cannot be verified.” This is the correct grounded result when no source is provided.
