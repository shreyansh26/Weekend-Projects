<?php
// this helps to get the ip address of the attacker
if(getenv(HTTP_X_FORWARDED_FOR)) {
  $ip = getenv(HTTP_X_FORWARDED_FOR);
} else {
  $ip = getenv(REMOTE_ADDR);
}

date_default_timezone_set("Asia/Calcutta");

if($ip) {
  $path = $_SERVER['DOCUMENT_ROOT'] . '/logs.txt';
  $file_handle = fopen($path, 'a+');
  if($file_handle) {
    $output = $ip . "--" . gethostbyaddr($ip) . "--" . date("Y:m:d") . "--" . date("H:i:s");
    fwrite($file_handle, $output.PHP_EOL);
    fclose($file_handle);
  } else {
    print("No");
  }
}
?>

<html>
<head>
  <title>404 Not found</title>
</head>

<body>
<h1>404 Not Found</h1>
The requested page "/backdoor.php" was not found on this server.
</body>
</html>
