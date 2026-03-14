<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $email = $_POST["email"];
    $password = $_POST["password"];

    $file = "users.csv";

    if (($handle = fopen($file, "r")) !== FALSE) {

        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {

            $usernameCSV = $data[0];
            $emailCSV = $data[1];
            $passwordCSV = $data[2];

            if ($email === $emailCSV && password_verify($password, $passwordCSV)) {

                $_SESSION["user"] = $usernameCSV;
                fclose($handle);
                header("Location: /Soundbeats/html/index.html");
                exit();
            }
        }

        fclose($handle);
    }

    echo "Credenciales incorrectas";
}
?>