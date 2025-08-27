<?php
$title = $_GET['b'];
$text = $_GET['c'];
$by = $_GET['e'];
$to = $_GET['a'];
$headers = ''; //

ini_set('user_agent', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36');

if (strpos($to, '@yandex.ru') !== false) {
    $headers = "From: $by\r\n";
    $headers .= "Reply-To: $by\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/html; charset=UTF-8\r\n";
    $headers .= "SPF: v=spf1 include:spf.yandex.net ~all\r\n";
    $headers .= "DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=example.com; s=selector; h=from:to:subject:date:message-id; bh=...; b=...\r\n";
} elseif (strpos($to, '@gmail.com') !== false) {
    $senderName = explode("@", $by)[0];
    $headers = "From: $senderName <$by>\r\n";
    $headers .= "Reply-To: $by\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "SPF: v=spf1 include:_spf.google.com ~all\r\n";
}

if (mail($to, $title, $text, $headers)) {
    echo "Successful!";
} else {
    echo "Something went wrong...";
}

?>

