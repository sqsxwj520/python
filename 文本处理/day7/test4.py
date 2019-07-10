"""分析器"""
# pv分析(page view)即页面浏览量或页面点击量
from urllib.parse import urlparse

urls = """/ index.php?m = ajax & c = RedLoginHead
/js/layer/skin/layer.css
/app/template/default//style/css.css
http://www.magedu.com/index.php
"""
for url in urls.splitlines():
    d = urlparse(url)
    print(d)
    print(d.path)
