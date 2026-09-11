# Step 2 - Test and Debug Note

The original code compared the raw input directly with `quit`, so inputs such as ` quit ` did not exit. It also always requested two FAISS results, even when the index contained fewer than two chunks, and its prompt did not explicitly restrict answers to the supplied context. I corrected the loop with `strip()` and a case-insensitive comparison, bounded `k` by the index size, ignored blank chunks, and added a grounded-answer instruction. These changes make the program safer for real command-line use and reduce unsupported answers.
