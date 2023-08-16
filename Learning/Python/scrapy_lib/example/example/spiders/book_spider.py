import scrapy

class BooksSpider(scrapy.Spider):
    name = "books" #Label of the spider
    start_urls = ['http://books.toscrape.com'] #Start url, can be multi

    def parse(self, response):
        '''
        Analysis data
        Every data of book in <article class="product_pod">
        Using css() method to find article
        '''
        for book in response.css('article.product_pod'):
            #Book name stored in article > h3 > a @title
            name = book.xpath('./h3/a/@title').extract_first()

            '''
            Price stored in element p, class price_color, text
            Example : <p class="price_color">£51.77</p>
            '''
            price = book.css('p.price_color::text').extract_first()
            yield {
                'name' : name,
                'price' : price,
            }

        '''
        Analysis url link
        Next page : ul.paper > li.next > a
        Example : <ul class="pager"><li class="next"><a href="catalogue/page-2.html">next</a></li></ul>
        '''
        next_url = response.css('ul.paper li.next a::attr(href)').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)