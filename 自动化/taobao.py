from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext(storageState="cookie")

    # Open new page
    page = context.newPage()

    # Go to https://error.taobao.com/app/tbhome/common/error.html
    page.goto("https://error.taobao.com/app/tbhome/common/error.html")

    # Click text="出售中的宝贝"
    page.click("text=\"出售中的宝贝\"")
    # assert page.url == "https://item.manager.taobao.com/taobao/manager/render.htm?tab=on_sale"

    # Click //a[normalize-space(.)='知道了' and normalize-space(@role)='button']
    page.click("//a[normalize-space(.)='知道了' and normalize-space(@role)='button']")

    # Click text="全部宝贝"
    page.click("text=\"全部宝贝\"")
    # assert page.url == "https://item.manager.taobao.com/taobao/manager/render.htm?tab=all&table.sort.upShelfDate_m=desc"

    # Click //tr[7]/td[8]/div/div/div/div/button[1][normalize-space(.)='编辑商品' and normalize-space(@title)='编辑商品']
    with page.expect_popup() as popup_info:
        page.click("//tr[7]/td[8]/div/div/div/div/button[1][normalize-space(.)='编辑商品' and normalize-space(@title)='编辑商品']")
    page1 = popup_info.value

    # Close page
    page1.close()

    # Click //tr[7]/td[8]/div/div/div/div/button[1][normalize-space(.)='编辑商品' and normalize-space(@title)='编辑商品']
    with page.expect_popup() as popup_info:
        page.click("//tr[7]/td[8]/div/div/div/div/button[1][normalize-space(.)='编辑商品' and normalize-space(@title)='编辑商品']")
    page2 = popup_info.value

    # Close page
    page2.close()

    # Click text="编辑商品"
    with page.expect_popup() as popup_info:
        page.click("text=\"编辑商品\"")
    page3 = popup_info.value

    # Click input[placeholder="最多允许输入30个汉字（60字符）"]
    page3.click("input[placeholder=\"最多允许输入30个汉字（60字符）\"]")

    # Press a with modifiers
    page3.press("input[placeholder=\"最多允许输入30个汉字（60字符）\"]", "Control+a")

    # Fill input[placeholder="最多允许输入30个汉字（60字符）"]
    page3.fill("input[placeholder=\"最多允许输入30个汉字（60字符）\"]", "as打动")

    # Close page
    page3.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)