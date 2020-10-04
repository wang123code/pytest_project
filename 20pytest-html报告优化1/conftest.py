from datetime import datetime
from py.xml import html
import pytest


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
    outcome = yield 
    report = outcome.get_result()
    report.description=str(item.function.__doc__)
    

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    if report.passed:
      del cells[:]


@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('No log output captured.', class_='empty log'))

    