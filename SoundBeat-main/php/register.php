<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $username = $_POST["username"];
    $email = $_POST["email"];
    $password = $_POST["password"];

    $file = "/csv/users.csv";

    
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    
    $handle = fopen($file, "a");
    fputcsv($handle, [$username, $email, $hashedPassword]);
    fclose($handle);

    $_SESSION["user"] = $username;

    header("Location: /index/index.php");
    exit();
}
?>