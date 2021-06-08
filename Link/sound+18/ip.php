<?php
$ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];

$file = 'ip.txt';
$fp = fopen($file, 'w');

fwrite($fp,$ipaddress);
fclose($fp);
?>