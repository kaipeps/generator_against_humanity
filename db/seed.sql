INSERT INTO cards(color, text, author_id, author_name, pick, public_card) 
VALUES 
    ("black", "Special K's _ Shack: Now serving _.", 1, "Kai Pepper", 2, t),
    ("white", "Shrimp.", 1, "Kai Pepper", 0, t),
    ("black", "Why am I getting an error?", 1, "Kai Pepper", 1, t),
    ("white", "JavaScript. Just... JavaScript.", 1, "Kai Pepper", 0, t),
    ("white", "Zoom issues.", 1, "Kai Pepper", 0, t),
    ("white", "Indentation.", 1, "Kai Pepper", 0, t);

INSERT INTO saves(saved_card_id, saved_user_id) 
VALUES 
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1);
