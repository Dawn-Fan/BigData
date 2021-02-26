import time

from playwright import sync_playwright
import asyncio
import excel_main as ex

def edit(page,index,address1,address2):
    clickname = "//tbody/tr["+str(index)+"]/td[9]/div[1]/div[1]/div[1]/div[1]/button[1]"
    with page.expect_popup() as popup_info:
        page.click(clickname)
    page2 = popup_info.value
    run_page_edit(page2,address1,address2)

def  run_page_edit(page2,address1,address2): #这是进入编辑页面后的操作
    # page2.reload(0,"domcontentloaded")
    time.sleep(2)
    page2.fill("input[placeholder=\"最多允许输入30个汉字（60字符）\"]",address2)
    time.sleep(2)

    # Click text="使用物流配送"
    # page2.click("text=\"使用物流配送\"")
    # page2.check("//html[1]/body[1]/div[4]/div[1]/div[1]/div[5]/div[1]/div[8]/div[6]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/label[1]/span[1]/input[1]")
    # Click //div[normalize-space(.)='运费模板 新建运费模板刷新模板数据']/div[2]/span
    # time.sleep(3)

    # page2.click("//body/div[@id='root']/div[@id='_root']/div[@id='ROOT']/div[@id='struct-content']/div[@id='struct-card']/div[@id='deliver-card']/div[@id='struct-tbExtractWay']/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/div[2]/span[1]/span[1]")
    page2.click(
        "body.new-seller:nth-child(2) div.engine-app div.com-struct.sell-wrap div.com-struct.sell-struct-content:nth-child(5) div.com-struct div.com-struct.sell-card:nth-child(8) div.com-struct:nth-child(7) div.next-row.next-row-no-padding.sell-o-addon div.next-col.next-col-20.sell-o-addon-content:nth-child(2) div.sell-o-addon-info div.info-content div.sell-transport span.next-checkbox-group.sell-extractway-checkbox div.child-block div.child-block.logis-block div.next-row div.next-col.next-col-11:nth-child(2) span.next-select.medium.transport-select > span.next-select-inner:nth-child(2)")
    time.sleep(2)
    # Click //li[normalize-space(.)='安阳' and normalize-space(@role)='menuitem']
    # this_address = "//li[normalize-space(.)="+address+"and normalize-space(@role)='menuitem']"
    this_address = "//li[contains(text(),'"+address1+"')]"
    # print(this_address)
    # time.sleep(1)
    page2.click(this_address)
    time.sleep(2)
    page2.check(
        "//body/div[@id='root']/div[@id='_root']/div[@id='ROOT']/div[@id='struct-content']/div[@id='struct-card']/div[@id='post-sale-service-card']/div[@id='struct-startTime']/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/label[1]/label[1]/span[1]/input[1]")
    time.sleep(3)
    # page2.click("//span[contains(text(),'立刻上架')]")
    # page2.check("/html[1]/body[1]/div[4]/div[1]/div[1]/div[5]/div[1]/div[9]/div[11]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]/span[1]/label[1]/label[1]/span[1]/input[1]")
    # with page2.waitForLoadState():
    # page2 = context.newPage()
    # with page2.content().expect_page() as new_page_info:
    page2.click('"提交宝贝信息"')

    time.sleep(4)
        # page2.click(clickname)
    # page2.on("domcontentloaded")
    print(address2,"----","OK")

    # Close page
    page2.close()

def run(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.newContext(storageState="cookie")

    # Open new page
    page = context.newPage()

    # Go to https://myseller.taobao.com/home.htm#/index
    page.goto("https://myseller.taobao.com/home.htm#/index")

    # Click text="仓库中的宝贝"
    with page.expect_popup() as popup_info:
        page.click("text=\"仓库中的宝贝\"")
    page1 = popup_info.value
    # time.sleep(10)
    # Click //a[normalize-space(.)='知道了' and normalize-space(@role)='button']
    page1.click("//a[normalize-space(.)='知道了' and normalize-space(@role)='button']")

    # Click img[alt="WanXiang Logo"]
    # page1.click("img[alt=\"WanXiang Logo\"]")

    # Click //tr[7]/td[9]/div/div/div/div/button[1][normalize-space(.)='编辑商品' and normalize-space(@title)='编辑商品']
    # asyncio.edit(page1,7,"安阳")      #一个窗口
    # asyncio.edit(page1, 7, "安阳")
    # with open("sum.txt",'r') as p:
    #     sum = p.read()
    while_count=300

    sleeptime = 1
    # page1.setDefaultTimeout(6)
    # page1.reload("domcontentloaded")
    f = ex.excel("./地址.xlsx","38节鲜花速递康乃馨玫瑰混搭花束送长辈")
    with open("sum.txt","r+") as file:
        sum = int(file.read())

        print("启动———————————————————— 序号=",sum,'\n')
        while (sum<746):
            while_count -= 5


            address1, address2 = f.getdata(sum)
            print(address1,address2)
            edit(page1,1, address1,address2)
            time.sleep(sleeptime)
            sum += 1
            file.seek(0,0)
            file.truncate(0)
            file.write(str(sum))


            address1, address2 = f.getdata(sum)
            print(address1, address2)
            edit(page1,3, address1,address2)
            sum += 1
            file.seek(0, 0)
            file.truncate(0)
            file.write(str(sum))
            time.sleep(sleeptime)

            address1, address2 = f.getdata(sum)
            print(address1, address2)
            edit(page1,5, address1,address2)
            sum += 1
            file.seek(0, 0)
            file.truncate(0)
            file.write(str(sum))
            time.sleep(sleeptime)

            address1, address2 = f.getdata(sum)
            print(address1, address2)
            edit(page1,7, address1,address2)
            sum += 1
            file.seek(0, 0)
            file.truncate(0)
            file.write(str(sum))
            time.sleep(sleeptime)

            address1, address2 = f.getdata(sum)
            print(address1, address2)
            edit(page1,9, address1,address2)
            sum+=1
            file.seek(0, 0)
            file.truncate(0)
            file.write(str(sum))
            time.sleep(4)

            print("\n\n-------5个结束，sum=",sum,'\n')
            page1.reload(0, 'domcontentloaded')
            time.sleep(2)
            page1.reload(0, 'domcontentloaded')
            time.sleep(2)



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