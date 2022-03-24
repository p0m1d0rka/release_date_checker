from pip._internal.operations import freeze
import requests
import re

base_url = "https://pypi.org/project"
x = freeze.freeze()
for name in x:
    module_name, version = name.split('==')
    resp = requests.get(f"{base_url}/{module_name}/{version}")

    open_time_tag = resp.text.find("<time")
    close_time_tag = resp.text.find("</time>")
    time_tag = resp.text[open_time_tag:close_time_tag]
    m = re.findall('.*datetime=\"(?P<dt>.*?)\"\s.*', time_tag)
    if len(m) > 0:
        release_date = m[0]
    else:
        release_date = 'unknown'
    print(f"{module_name} - {version} - {release_date}")

