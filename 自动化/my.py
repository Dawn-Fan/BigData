from playwright import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fitem.manager.taobao.com%2Ftaobao%2Fmanager%2Frender.htm
    page.goto("https://login.taobao.com/member/login.jhtml?redirectURL=http%3A%2F%2Fitem.manager.taobao.com%2Ftaobao%2Fmanager%2Frender.htm")

    # Click //div[normalize-space(.)='扫码登录更安全']/i
    page.click("//div[normalize-space(.)='扫码登录更安全']/i")

    # Go to https://login.taobao.com/member/login_unusual.htm?user_num_id=2083282850&from=tb&style=default&css_style=default&is_scure=true&c_is_scure=true&tpl_redirect_url=http%3A%2F%2Fitem.manager.taobao.com%2Ftaobao%2Fmanager%2Frender.htm&cr=http%3A%2F%2Fitem.manager.taobao.com%2Ftaobao%2Fmanager%2Frender.htm&sub=false&loginsite=0&login_type=3&lang=zh_CN&appkey=00000000&new_iv_check=true&iv_check_time=1612200869429&iv_check_sign=d29121f93f75b23ca4dab8751f34377c
    page.goto("https://login.taobao.com/member/login_unusual.htm?user_num_id=2083282850&from=tb&style=default&css_style=default&is_scure=true&c_is_scure=true&tpl_redirect_url=http%3A%2F%2Fitem.manager.taobao.com%2Ftaobao%2Fmanager%2Frender.htm&cr=http%3A%2F%2Fitem.manager.taobao.com%2Ftaobao%2Fmanager%2Frender.htm&sub=false&loginsite=0&login_type=3&lang=zh_CN&appkey=00000000&new_iv_check=true&iv_check_time=1612200869429&iv_check_sign=d29121f93f75b23ca4dab8751f34377c")

    # Go to https://item.manager.taobao.com/taobao/manager/render.htm
    async def abc():
        await page.goto("https://item.manager.taobao.com/taobao/manager/render.htm")
    abc()
    page.goto("https://item.manager.taobao.com/taobao/manager/render.htm")
    # Click text="编辑商品"
    with page.expect_popup() as popup_info:
        page.click("text=\"编辑商品\"")
    page1 = popup_info.value

    # Click text="宝贝标题"
    page1.click("text=\"宝贝标题\"")

    # Click input[placeholder="最多允许输入30个汉字（60字符）"]
    page1.click("input[placeholder=\"最多允许输入30个汉字（60字符）\"]")

    # Fill input[placeholder="最多允许输入30个汉字（60字符）"]
    page1.fill("input[placeholder=\"最多允许输入30个汉字（60字符）\"]", "你是个大")

    # Fill //div[normalize-space(.)='淘宝二手默认运费模板_湖南']/div/div/span/input[normalize-space(@type)='text']
    page1.fill("//div[normalize-space(.)='淘宝二手默认运费模板_湖南']/div/div/span/input[normalize-space(@type)='text']", "呵呵")

    # Fill //label[normalize-space(.)='定时上架']/label/span/input[normalize-space(@type)='radio']
    page1.fill("//label[normalize-space(.)='定时上架']/label/span/input[normalize-space(@type)='radio']", "1")

    # Fill //label[normalize-space(.)='放入仓库']/label/span/input[normalize-space(@type)='radio']
    page1.fill("//label[normalize-space(.)='放入仓库']/label/span/input[normalize-space(@type)='radio']", "2")

    # Go to https://item.taobao.com/item.htm?id=637968310017
    page1.goto("https://item.taobao.com/item.htm?id=637968310017")

    # Click text="关闭"
    page1.click("text=\"关闭\"")

    # Close page
    page1.close()

    # Go to https://item.manager.taobao.com/taobao/manager/render.htm
    page.goto("https://item.manager.taobao.com/taobao/manager/render.htm")

    # Click text="编辑商品"
    with page.expect_popup() as popup_info:
        page.click("text=\"编辑商品\"")
    page2 = popup_info.value

    # Close page
    page2.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)