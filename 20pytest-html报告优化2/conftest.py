from datetime import datetime
from py.xml import html
from selenium import webdriver
import pytest


driver = None


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2,html.th('Description'))
    cells.insert(1, html.th('Time',class_='sortable time',col='time'))
    cells.pop()
    

@pytest.mark.optionalhook
def pytest_html_results_table_row(report,cells):
    cells.insert(2,html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(),class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item,call):
    # 当测试失败的时候，自动截图，展示到html报告中
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield 
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
    report.description=str(item.function.__doc__)


def _capture_screenshot():
    # 截图保存为base64，展示到html中
    return driver.get_screenshot_as_base64()


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver
'''
@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    if report.passed:
      del cells[:]


@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('No log output captured.', class_='empty log'))
'''
    