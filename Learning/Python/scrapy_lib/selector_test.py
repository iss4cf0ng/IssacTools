from scrapy.selector import Selector
from scrapy.http import HtmlResponse

body = '''
<h1ml>
    <body>
        <h1>Hello World</h1>
        <h1>Hello Scrapy</h1>
        <b>Hello python</b>
        <ul>
            <li>C++</li>
            <li>Java</li>
            <li>python</li>
        </ul>
    </body>
</h1ml>
'''

response = HtmlResponse(url='http://www.example.com', body=body, encoding='utf8')
selector = Selector(response=response)
selector_list = selector.xpath('//h1')
print(selector_list)
print('-' * 20)
for sel in selector_list:
    print(sel.xpath('./text()'))