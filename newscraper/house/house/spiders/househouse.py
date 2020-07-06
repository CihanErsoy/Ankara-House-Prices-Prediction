import scrapy
from ..items import HouseItem
from urllib.parse import urljoin

class HousehouseSpider(scrapy.Spider):
    page_number = 2
    name = 'househouse'
    allowed_domains = ['hurriyetemlak.com']
    start_urls = ['https://www.hurriyetemlak.com/ankara-satilik/daire']
    def parse(self, response):
        all_contents = response.xpath('//div[contains(@class , "listing-item")]')
        for content in all_contents:
            link = content.xpath('.//a[@class = "img-link"]/@href').get()
            yield response.follow(url = link, callback = self.parse_pages)
        next_page = "https://www.hurriyetemlak.com/ankara-satilik/daire?page=" + str(HousehouseSpider.page_number)
        if HousehouseSpider.page_number <= 1000:
            HousehouseSpider.page_number += 1
            yield response.follow(url = next_page, callback=self.parse)

    def parse_pages(self, response):
        data = HouseItem()

        price = response.xpath('//div[@class = "right"]/*[contains(text()," TL")]/text()').get()
        if price is None:
            pass
        else:
            price = price.strip()
            price = price.rstrip(' TL')
            pricelist = price.split(',')
            price = "".join(pricelist)
            price = int(price)

            town = response.xpath('//div[@class="det-title-bottom"]/ul/li[2]/text()').get()
            if town is None:
                pass
            else:
                town=town.strip()

            area = response.xpath('//div[@class="det-title-bottom"]//sup[contains(text(),"2")]/parent::span/text()').get()
            if area is None:
                pass
            else:
                area = area.strip()
                area = area.rstrip(' m')

            typeofit = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Konut Şekli")]/following-sibling::span/text()').get()
            if typeofit is None:
                pass
            else:
                typeofit = typeofit.strip()

            roomfirst = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Oda")]/following-sibling::span/text()').get()
            if roomfirst is None:
                room = roomfirst
            else:
                roomlist = [int(m) for m in roomfirst.split() if m.isdigit()]
                if len(roomlist) ==2:
                    room =  roomlist[0] + roomlist[1]
                elif len(roomlist) ==1:
                    room = roomlist[0]
                elif len(roomlist) ==3:
                    room =  roomlist[0] + roomlist[1] + roomlist[2]
                else:
                    room = roomfirst

            floorfirst = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Bulunduğu Kat")]/following-sibling::span/text()').get()
            if floorfirst is None:
                floornumber = floorfirst
            elif len([r for r in floorfirst if r.isdigit()]) == 0:
                floornumber = floorfirst
            else:
                floornumber = [int(r.strip('.')) for r in floorfirst.split() if r.strip('.').isdigit()]
                floornumber = floornumber[0]

            agefirst = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Bina Yaşı")]/following-sibling::span/text()').get()
            if agefirst is None:
                age = agefirst
            else:
                if agefirst == 'Sıfır Bina':
                    age = 0
                else:
                    age = [t for t in agefirst.split() if t.isdigit()]
                    age = int(age[0])

            heating = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Isınma")]/following-sibling::span/text()').get()
            if heating is None:
                pass
            else:
                heating = heating.strip()

            totalfloor= response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Kat Sayısı")]/following-sibling::span/text()').get()
            if totalfloor is None:
                floorcount = totalfloor
            else:
                floorcount = [int(s) for s in totalfloor.split() if s.isdigit()]
                floorcount = floorcount[0]

            creditavlb = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Krediye")]/following-sibling::span/text()').get()
            if creditavlb is None:
                pass
            else:
                creditavlb = creditavlb.strip()

            furniture = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Eşya Durumu")]/following-sibling::span/text()').get()
            if furniture is None:
                pass
            else:
                furniture = furniture.strip()

            firsthand = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Yapının Durumu")]/following-sibling::span/text()').get()
            if firsthand is None:
                pass
            else:
                firsthand = firsthand.strip()

            maintenancefee = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Aidat")]/following-sibling::span/text()').get()
            if maintenancefee is None:
                pass
            else:
                maintenancefee = maintenancefee.strip()
                maintenancefee = maintenancefee.rstrip(' TL')

            frontage_list = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Cephe")]/following-sibling::div//text()').getall()
            if frontage_list is None:
                frontage = frontage_list
            else:
                frontage_list_str = [k.strip() for k in frontage_list]
                frontage = "".join(frontage_list_str)
                frontage = frontage.strip()

            fuel = response.xpath('//div[@class="det-adv-info"]//span[contains(text(),"Yakıt")]/following-sibling::span/text()').get()
            if fuel is None:
                pass
            else:
                fuel = fuel.strip()


            data['Price'] = price
            data['Town'] = town
            data['Area'] = area
            data['Typeofit'] = typeofit
            data['Room'] = room
            data['FloorNumber'] = floornumber
            data['Age'] = age
            data['Heating'] = heating
            data['FloorCount'] = floorcount
            data['CreditAvlb'] = creditavlb
            data['Furniture'] = furniture
            data['Firsthand'] = firsthand
            data['MaintenanceFee'] = maintenancefee
            data['Frontage'] = frontage
            data['Fuel'] = fuel



            yield data
