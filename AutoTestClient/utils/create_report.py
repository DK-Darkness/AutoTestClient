import time,os
from selenium import webdriver

prefix = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Test Report</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style type="text/css">
        html {
            font-family: sans-serif;
            font-size: 12px;
            -ms-text-size-adjust: 100%;
            -webkit-text-size-adjust: 100%;
        }

        body {
            margin: 10px;
        }

        table {
            border-collapse: collapse;
            border-spacing: 0;
        }

        td,
        th {
            padding: 0;
        }

        .pure-table {
            border-collapse: collapse;
            border-spacing: 0;
            empty-cells: show;
            border: 1px solid #cbcbcb;
        }

        .pure-table caption {
            color: #000;
            font: italic 85%/1 arial, sans-serif;
            padding: 1em 0;
            text-align: center;
        }

        .pure-table td,
        .pure-table th {
            border-left: 1px solid #cbcbcb;
            border-width: 0 0 0 1px;
            font-size: inherit;
            margin: 0;
            overflow: visible;
            padding: .5em 1em;
        }

        .pure-table thead {
            background-color: #e0e0e0;
            color: #000;
            text-align: left;
            vertical-align: bottom;
        }

        .pure-table td {
            background-color: transparent;
        }

        .pure-table-odd td {
            background-color: #f2f2f2;
        }
    </style>

<body>
    <table class="pure-table">
        <thead>
            <tr>
                <th>#</th>
                <th>"重要级别"</th>
                <th>测试用例标题</th>
                <th>预置条件</th>
                <th>操作步骤</th>
                <th>预期结果</th>
                <th>测试结果</th>
            </tr>
        </thead>

        <tbody>
'''
suffix = '''
        </tbody>
    </table>
</body>

</html>
'''
def write_to_report(result):
    with open('test_report.html','w',encoding='utf-8') as f:
        f.write(prefix)
        for case in result:
            if case['id'] % 2 == 0:
                f.write('            <tr class="pure-table-odd">\n')
            else:
                f.write('            <tr>\n')
            f.write('                <td>{}</td>'.format(str(case['id'])))
            f.write('<td>{}</td>'.format(case['level']))
            f.write('<td>{}</td>'.format(case['head']))
            f.write('<td>{}</td>'.format(case['pre_step']))
            f.write('<td>{}</td>'.format(case['step']))
            f.write('<td>{}</td>'.format(case['target']))
            if case['result'] == 'PASS':
                f.write('<td><font color="green">{}</font></td>\n'.format(case['result']))
            elif case['result'] == 'FAIL':
                f.write('<td><font color="red">{}</font></td>\n'.format(case['result']))
            elif case['result'] == 'ABSENCE':
                f.write('<td><font color="gray">{}</font></td>\n'.format(case['result']))
            elif case['result'] == '':
                f.write('<td></td>\n')
            f.write('            </tr>\n')
        f.write(suffix)