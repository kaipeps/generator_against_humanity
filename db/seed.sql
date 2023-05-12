INSERT INTO cards(author_id, color, text, pick, public_card)
VALUES
    (1, "black", "Special K's _ Shack, now serving _.", 2, TRUE),
    (1, "black", "Why am I getting this error?", 1, TRUE),
    (1, "white", "Zoom issues.", 0, TRUE),
    (1, "white", "Indentation.", 0, TRUE),
    (1, "white", "Code blocks.", 0, TRUE),
    (1, "white", "Tracebacks.", 0, TRUE),
    (1, "white", "Shrimp.", 0, TRUE);

-- Templates:
-- Black cards -
--     (1, "black", "", x, TRUE),
-- where 'x' is the number of cards needed to fill the blanks.

-- White cards -
--     (1, "white", "", 0, TRUE),
