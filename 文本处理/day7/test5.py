"""分析器"""
# UserAgent分析
from user_agents import parse

uas = """Mozilla/5.0 (Windows NT 
Mozilla/5.0 (Windows NT 6.1; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
"""
for uastr in uas.splitlines():
    ua = parse(uastr)
    print(ua.browser)
    print(ua.browser.family, ua.browser.version[0] if len(ua.browser.version) else 0, ua.browser.version_string)
