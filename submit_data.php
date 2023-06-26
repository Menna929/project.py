<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input
    $username = filter_input(INPUT_POST, "username", FILTER_SANITIZE_STRING);
    $password = filter_input(INPUT_POST, "password", FILTER_SANITIZE_STRING);

    // Validate input
    if (empty($username) || empty($password)) {
        echo "Please enter both username and password.";
    } else {
        // Escape user input to prevent command injection attacks
        $username = escapeshellarg($username);
        $password = escapeshellarg($password);

        // Execute Python script with sanitized input
        $result = shell_exec("python3 check_login.py $username $password");

        // Check result and output appropriate message
        if (trim($result) == "True") {
            echo "Login successful.";
        } else {
            echo "Invalid username or password.";
        }
    }
}
?>