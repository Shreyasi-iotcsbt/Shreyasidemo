# char_by_char_brute_force_demo
A character-by-character brute force demo simulates a password-cracking attack that guesses one character at a time instead of the whole password at once. It locks in each position as soon as it matches, rather than needing the entire string to align in a single guess.

This makes it dramatically faster than a naive full-string brute force — for a password of length n with k possible characters, it takes roughly k × n attempts on average instead of k^n. It's mainly used to illustrate how attacks that get partial feedback (timing side-channels, partial-match oracles, etc.) are far more dangerous than attacks that only get a pass/fail on the whole guess.

Purpose: To demonstrate, for educational purposes, how the amount of feedback an attacker receives fundamentally changes the difficulty of a brute-force attack — showing why systems should only ever return a single pass/fail result for an entire credential, never partial or per-character correctness, since even a small information leak (like knowing one character is right) can reduce cracking time from computationally infeasible to trivial.
