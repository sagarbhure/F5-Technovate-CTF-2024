<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Sprinter</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="flex flex-row">
    <div class="bg-white p-8 w-6/12 justify-center items-center h-screen">
        <h2 class="text-2xl font-bold mb-6 text-center">Admin Login</h2>
        <form action="index.php" method="POST" class="space-y-4">
            <div>
                <label for="username" class="block text-sm font-medium text-gray-700">Username:</label>
                <input type="text" id="username" name="username" required
                    class="mt-1 p-2 w-full border border-gray-300 rounded-md">
            </div>
            <div>
                <label for="password" class="block text-sm font-medium text-gray-700">Password:</label>
                <input type="password" id="password" name="password" required
                    class="mt-1 p-2 w-full border border-gray-300 rounded-md">
            </div>
            <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600">Login</button>
        </form>
        <?php
        if ($_SERVER["REQUEST_METHOD"] === "POST") {
            $username = $_POST['username'];
            $password = $_POST['password'];

            try {
                $db = new PDO('sqlite:db/database.sqlite');
                $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

                // Vulnerable SQL query
                $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
                $result = $db->query($query);

                if ($result) {
                    $user = $result->fetch(PDO::FETCH_ASSOC);

                    if ($user && $user['is_admin']) {
                        echo "<p class='mt-4 text-green-600'>Welcome admin! The flag is: technovate{simple_sql_injection_works_89}</p>";
                    } else {
                        echo "<p class='mt-4 text-red-600'>Invalid username or password.</p>";
                    }
                }
            } catch (PDOException $e) {
                echo "<p class='mt-4 text-red-600'>An error occurred: " . $e->getMessage() . "</p>";
            }
        }
        ?>
    </div>
    <div class="w-6/12">
        <img src="./with_cat.svg" alt="" srcset="">
    </div>
</body>
</html>
