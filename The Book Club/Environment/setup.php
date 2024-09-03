<?php
try {
    $db = new PDO('sqlite:/var/www/html/db/database.sqlite');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Create users table
    $db->exec("CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        is_admin BOOLEAN NOT NULL
    )");

    // Insert admin and guest users
    $db->exec("INSERT INTO users (username, password, is_admin) VALUES
        ('admin', '5f4dcc3b5aa765d61d8327deb882cf99', 1),
        ('guest', '084e0343a0486ff05530df6c705c8bb4', 0)");

    echo "Database setup complete!";
} catch (PDOException $e) {
    echo "An error occurred: " . $e->getMessage();
}
?>
