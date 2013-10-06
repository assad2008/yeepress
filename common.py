#/usr/bin/python
#coding=utf-8

import os.path
import tenjin
from tenjin.helpers import *
from urllib import unquote, quote
from setting import THEME
import tornado.web

def safe_encode(con):
    return con.replace("<","&lt;").replace(">","&gt;")

def safe_decode(con):
    return con.replace("&lt;","<").replace("&gt;",">")

def unquoted_unicode(string, coding='utf-8'):
    return unquote(string).decode(coding)

def quoted_string(unicode, coding='utf-8'):
    return quote(unicode.encode(coding))
	
def cnnow():
    return datetime.utcnow() + timedelta(hours =+ 8)
	
def time_from_now(time):
    if isinstance(time, int):
        time = timestamp_to_datetime(time)
    time_diff = cnnow() - time
    days = time_diff.days
    if days:
        if days > 730:
            return '%s years ago' % (days / 365)
        if days > 365:
            return '1 year ago'
        if days > 60:
            return '%s months ago' % (days / 30)
        if days > 30:
            return '1 month ago'
        if days > 14:
            return '%s weeks ago' % (days / 7)
        if days > 7:
            return '1 week ago'
        if days > 1:
            return '%s days ago' % days
        return '1 day ago'
    seconds = time_diff.seconds
    if seconds > 7200:
        return '%s hours ago' % (seconds / 3600)
    if seconds > 3600:
        return '1 hour ago'
    if seconds > 120:
        return '%s minutes ago' % (seconds / 60)
    if seconds > 60:
        return '1 minute ago'
    if seconds > 1:
        return '%s seconds ago' %seconds
    return '%s second ago' % seconds
	
Tempengine = tenjin.Engine(path = [os.path.join('templates', theme) for theme in [THEME,'admin']] + ['templates'], cache = tenjin.MemoryCacheStorage(), preprocess = True)

class BaseHandler(tornado.web.RequestHandler):
    
    def render(self, template, context = None, globals = None, layout = False):
        if context is None:
            context = {}
        context.update({
            'request':self.request,
        })
        return Tempengine.render(template, context, globals, layout)

    def echo(self, template, context = None, globals = None, layout = False):
        self.write(self.render(template, context, globals, layout))
    
    def set_cache(self, seconds, is_privacy=None):
        if seconds <= 0:
            self.set_header('Cache-Control', 'no-cache')
        else:
            if is_privacy:
                privacy = 'public, '
            elif is_privacy is None:
                privacy = ''
            else:
                privacy = 'private, '
            self.set_header('Cache-Control', '%smax-age=%s' % (privacy, seconds))

