import scrapy

class KipilingWebSite(scrapy.Spider): 
	
	name = 'product'
	
	start_urls = ["https://www.kipling.com/uk-en/sale/type/all-sale/?limit=all"] #Put The Url Of The Website 

	def parse(self,response): #Define The Funcation Of The Parse 

		container = response.css('div.product-list-product-wrapper')

		product_infromation = [] #Make Empty List Of The "product_information"

		for product in container: #Use For Loop And Make Dictionary
			all_product ={
				'product_name': product.css('h3.product-name a::attr(title)').extract_first(),
				'product_info': product.css('div.short-description p::text').extract_first(),
				'product_img': product.css('div.product-list-imagecontainer a img').xpath('@src').extract_first(),
				'product_colour': product.css('p.colors-number::text').extract_first(),
				'product_old_prize': product.css('.price-box .old-price::text').extract_first(),
				'product_new_prize': product.css('.price-box .special-price::text').extract_first()
			}

			product_infromation.append(all_product) #Append The "all_prodcut" Files Into The Empty List "product_infromation"

		print "========================================"
		print product_infromation                        #Print All The Details."
		print "========================================"