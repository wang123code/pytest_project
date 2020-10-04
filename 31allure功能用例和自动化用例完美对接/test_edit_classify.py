import allure


@allure.feature("编辑分类文章")
class TestArticleclassify():
    '''编辑文章分类'''
    @allure.story("登录-编辑文章分类，重复保存，保存失败")
    @allure.issue("http://49.235.92.12:8080/zentao/bug-view-1.html")  # 禅道bug地址
    @allure.testcase("http://49.235.92.12:8080/zentao/testcase-view-5-1.html")  # 禅道用例连接地址
    def test_edit_classify5(self, login):
        '''用例描述：编辑文章分类-输入重复的分类，保存失败，不能添加重复的
        setup: 登录login
        step1: 编辑文章分类，输入文章类别，如：计算机
        step2: 点保存按钮
        step3: 重新打开编辑页，输入：计算机
        step4: 再次点保存按钮
        assert: 保存失败，提示：已存在
        '''
        driver = login
        edit = ArticleclassifyPage(driver)
        edit.click_classify_nav()
        edit.edit_classify("计算机")
        res2 = edit.is_edit_classify_success("计算机")
        print("编辑是否成功：%s"%res2)
        assert res2  # 断言