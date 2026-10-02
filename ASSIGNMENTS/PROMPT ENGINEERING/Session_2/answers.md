# Session 2 - Structured and Output Prompts

## 1. Spotify playlist guide
**Prompt:** “Explain how to create a new playlist in Spotify using numbered steps. Keep each step to one action, use plain language, and include separate notes for mobile and desktop if the controls differ.”

**Sample answer:**
- Open Spotify and sign in.
- Select **Your Library**.
- Select **Create** or **+**, then choose **Playlist**.
- Enter a title and optional description.
- Add songs using **Add to playlist** or the playlist menu.
- Review the playlist in Your Library. Interface labels can vary by app version.

## 2. Zomato vs Swiggy comparison prompt
“Compare Zomato and Swiggy for a user deciding where to order dinner. Return a table with columns Feature, Zomato, Swiggy. Include restaurant discovery, delivery tracking, loyalty/subscription options, and availability caveat. Do not assert current fees or offers; say they vary by location and date.”

| Feature | Zomato | Swiggy |
|---|---|---|
| Restaurant discovery | Search and browse restaurants where service is available | Search and browse restaurants where service is available |
| Delivery tracking | Order tracking is offered for eligible orders | Order tracking is offered for eligible orders |
| Membership or loyalty | Plans and benefits may change by market and date | Plans and benefits may change by market and date |
| Fees and offers | Vary by restaurant, address, and time | Vary by restaurant, address, and time |

## 3. Last five IPL winners as JSON
The requested wording is made reproducible by defining the five completed seasons 2021-2025; season results are stable. JSON is valid and contains year and team.
```json
[
  {"year": 2021, "team": "Chennai Super Kings"},
  {"year": 2022, "team": "Gujarat Titans"},
  {"year": 2023, "team": "Chennai Super Kings"},
  {"year": 2024, "team": "Kolkata Knight Riders"},
  {"year": 2025, "team": "Royal Challengers Bengaluru"}
]
```

## 4. UPI benefits, exactly three bullets and under 30 words
- Pay digitally without carrying cash.
- Transfer money instantly between supported bank accounts.
- Review transactions in one app.

## 5. BookMyShow booking guide prompt
“Explain how to book a movie ticket using headings exactly in this sequence: Step 1: Search Movie; Step 2: Choose Cinema and Showtime; Step 3: Select Seats; Step 4: Review Price; Step 5: Pay; Step 6: Find the Ticket. Give one clear action under each heading and note that actual screens may vary.”
