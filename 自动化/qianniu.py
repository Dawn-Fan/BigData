import time

from playwright import sync_playwright
import asyncio

def edit(page,index,address):
    clickname = "//tbody/tr["+str(index)+"]/td[9]/div[1]/div[1]/div[1]/div[1]/button[1]"
    # await time.sleep(1)
    # asyncio.sleep(1)
    with page.expect_popup() as popup_info:
        page.click(clickname)
    page2 = popup_info.value

    page2.fill("input[placeholder=\"最多允许输入30个汉字（60字符）\"]", "as打动")
    # print("123")
    # time.sleep(123)

    # Click text="使用物流配送"
    # page2.click("text=\"使用物流配送\"")

    # Click //div[normalize-space(.)='运费模板 新建运费模板刷新模板数据']/div[2]/span
    page2.click(
        "body.new-seller:nth-child(2) div.engine-app div.com-struct.sell-wrap div.com-struct.sell-struct-content:nth-child(5) div.com-struct div.com-struct.sell-card:nth-child(8) div.com-struct:nth-child(7) div.next-row.next-row-no-padding.sell-o-addon div.next-col.next-col-20.sell-o-addon-content:nth-child(2) div.sell-o-addon-info div.info-content div.sell-transport span.next-checkbox-group.sell-extractway-checkbox div.child-block div.child-block.logis-block div.next-row div.next-col.next-col-11:nth-child(2) span.next-select.medium.transport-select > span.next-select-inner:nth-child(2)")

    # Click //li[normalize-space(.)='安阳' and normalize-space(@role)='menuitem']
    # this_address = "//li[normalize-space(.)="+address+"and normalize-space(@role)='menuitem']"
    this_address = "//li[contains(text(),'"+address+"')]"
    print(this_address)
    time.sleep(1)
    page2.click(this_address)

    page2.check(
        "//body/div[@id='root']/div[@id='_root']/div[@id='ROOT']/div[@id='struct-content']/div[@id='struct-card']/div[@id='post-sale-service-card']/div[@id='struct-startTime']/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/label[1]/label[1]/span[1]/input[1]")

    # time.sleep(1010)
    print("OK")
    # Close page
    page2.close()

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext(storageState="cookie")

    # Open new page
    page = context.newPage()

    # Go to https://myseller.taobao.com/home.htm#/index
    page.goto("https://myseller.taobao.com/home.htm#/index")

    # Click text="仓库中的宝贝"
    with page.expect_popup() as popup_info:
        page.click("text=\"仓库中的宝贝\"")
    page1 = popup_info.value

    # Click //a[normalize-space(.)='知道了' and normalize-space(@role)='button']
    page1.click("//a[normalize-space(.)='知道了' and normalize-space(@role)='button']")

    # Click img[alt="WanXiang Logo"]
    page1.click("img[alt=\"WanXiang Logo\"]")

    # Click //tr[7]/td[9]/div/div/div/div/button[1][normalize-space(.)='编辑商品' and normalize-space(@title)='编辑商品']
    # asyncio.edit(page1,7,"安阳")      #一个窗口
    # asyncio.edit(page1, 7, "安阳")
    edit(page1,5,"安阳")
    # asyncio.run(edit(page1, 7, "安阳"))
    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)