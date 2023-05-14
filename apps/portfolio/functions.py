import re

def is_mobile(request):
    user_agent = request.META['HTTP_USER_AGENT']
    pattern = r'mobile|android|iphone|ipod|ipad|windows phone'
    regex = re.compile(pattern, re.IGNORECASE)
    return bool(regex.search(user_agent))