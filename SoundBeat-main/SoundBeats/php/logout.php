<?php
session_start();
session_destroy();
header("Location: /Soundbeats/php/index.php");
exit();
?>