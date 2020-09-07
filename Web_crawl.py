import scrapy


class TestCrawler2Spider(scrapy.Spider):
    name = 'test_crawler2'
    allowed_domains = ['172.18.58.238']
    start_urls = ['http://172.18.58.238/index.php']
    custom_settings = {
        'DEPTH_LIMIT': 4
    }

    def parse(self, response):
        css_selector = 'img'

        #Crawled all website URL links
        links = response.xpath("//a/@href").extract()
        for link in links:
            if link:

                yield scrapy.Request(
                    response.urljoin(link),
                    callback=self.parse
                )

        #Crawled Image Links
        for x in response.css(css_selector):
            newsel='@src'
            url = response.url
            yield{
                'Image Link': url+x.xpath(newsel).extract_first(),
            }

#Test to show that our team members can collaborate here!
