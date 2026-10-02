# Session 4 - Role, System, and Reasoning Prompts

## 1. Restaurant reviewer role
**Prompt:** “Act as a fair food reviewer. Review an imaginary new Ahmedabad cafe using only these supplied details: Gujarati snacks, indoor seating, ₹300 average spend. Do not claim a personal visit. Keep the review balanced.”

**Sample response:** “Sample: This imaginary Ahmedabad cafe brings Gujarati snacks to a relaxed indoor setting, with an average spend around ₹300. The focused menu sounds convenient for a casual bite; check the current menu and availability before visiting.”

## 2. IPL-only system boundary
**System prompt:** “Answer only questions about IPL teams, players, fixtures, and scores. If asked about another topic, politely say: ‘I can only help with IPL cricket.’ Never invent live scores; explain when current verification is unavailable.”

**Test question:** “What is the latest Bollywood movie?”

**Expected response:** “I can only help with IPL cricket.”

## 3. Wallet arithmetic
The assignment's third price is interpreted as ₹899 because the supplied text shows `%899` (likely a typo). Total: ₹7,499 + ₹2,799 + ₹899 = ₹11,197. Wallet: ₹2,000. Shortfall: ₹11,197 − ₹2,000 = ₹9,197. The balance is not enough. A good assistant should show concise arithmetic and flag the typo assumption.

## 4. Ahmedabad day-trip prompt and sample
**Prompt:** “Plan one day in Ahmedabad for a first-time visitor. Give a morning, afternoon, and evening itinerary with food, travel, and entertainment. Use only well-known public places; do not invent opening hours or current ticket prices. Mark any details that need checking.”

**Illustrative response:** Morning: visit Sabarmati Ashram, then choose breakfast at a nearby cafe after checking today's hours. Travel by cab or auto and allow extra time for city traffic. Afternoon: explore the old city and have a Gujarati thali at a restaurant selected after checking its current menu and opening time. Evening: visit the riverfront or a scheduled cultural venue; verify event timings and transport before leaving. Keep water and a backup indoor stop in case of heat or rain.

## 5. Casual role prompt under 20 words
“Write a casual Instagram-style review of an imaginary Ahmedabad cafe using only: Gujarati snacks, cozy seats, ₹300 average. Under 20 words.”

**Sample output (16 words):** “Gujarati snack cravings, cozy seats, and a ₹300 average—this imaginary cafe sounds perfect for an easy catch-up.”
