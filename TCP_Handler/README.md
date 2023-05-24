## Description
Simple TCP Handler

## Goal
一個簡單的 TCP Handler\
在寫reverse shell時，如果沒有TCP Handler\
那麼 socket就只能單對單連線\
大部份能在Google上找到的 Server & Client程式\
都是一個 Client對連接一個 Server\
那如果是多個 Clients連接一個 Server呢?

## TCP Handler
可以處理多個 Client的連接，每一個連線稱為session
使用use可切換session

## Command
session
- info : 查看目前使用的session
- list : 列出所有session
- drop session_id : 斷開指定session_id的session, 沒有session_id則會斷開目前的session
use session_id
- 切換 session
msg
- 傳文字, 需要在使用session的情況下使用
