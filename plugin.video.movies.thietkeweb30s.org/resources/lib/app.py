# -*- coding: utf-8 -*-
import sys
import os
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmc
import json
from importlib import import_module
from utils.media_helper import MediaHelper
import utils.xbmc_helper as XbmcHelper

ADDON = xbmcaddon.Addon()
HANDLE = int(sys.argv[1])
BASEURL = sys.argv[0]
ARGS = urlparse.parse_qs(sys.argv[2][1:])
ADDON_ID = ADDON.getAddonInfo('id')
KODI_VERSION = int(xbmc.getInfoLabel('System.BuildVersion')[0:2])

print("***********************Current version %d" % KODI_VERSION)

SITES = [
    {
        'name': '[COLOR lime][B]bilutv.org[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/gz5330jiap6p4gj/bilutv.png',
        'class': 'Bilutv',
        'plugin': 'bilutv.plugin',
        'version': 1
    },
    {
        'name': '[COLOR lime][B]phimmedia.tv[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/4azdcrtqampxl9m/phim.png',
        'class': 'Phimmedia',
        'plugin': 'phimmedia.plugin',
        'version': 1
    },
    {
        'name': '[COLOR lime][B]phimmoi.net[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/41x5hno59xg83y3/phimmoi.png',
        'class': 'Phimmoi',
        'plugin': 'phimmoi.plugin',
        'version': 18
    },
    {
        'name': '[COLOR lime][B]tvhay.org[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/6k6u3ente4zu2s9/tvhay.png',
        'class': 'Tvhay',
        'plugin': 'tvhay.plugin',
        'version': 1
    },
    {
        'name': '[COLOR lime][B]phim3s.pw[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/3dbpjmpn73wzvfy/phim3s.png',
        'class': 'Phim3s',
        'plugin': 'phim3s.plugin',
        'version': 31
    },
    {
        'name': '[COLOR lime][B]phimbathu.org[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/bms8xxu7zfk4o7a/phimbathu.png',
        'class': 'Phimbathu',
        'plugin': 'phimbathu.plugin',
        'version': 1
    },
    {
        'name': '[COLOR lime][B]kenh88.com[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/z07t966jrvzxtvc/kenh88.png',
        'class': 'Kenh88',
        'plugin': 'kenh88.plugin',
        'version': 1
    },
    {
        'name': '[COLOR lime][B]phim14.net[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/5506ims2p7gbg06/phim14.png',
        'class': 'Phim14',
        'plugin': 'phim14.plugin',
        'version': 1
    },
    {
        'name': '[COLOR lime][B]animehay.tv[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/aclmu46n3zu9q75/animetvn.png',
        'class': 'Animehay',
        'plugin': 'animehay.plugin',
        'version': 1
    },
    {
        'name': '[COLOR lime][B]vuviphim.com[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/2zxo0r4oyow91hl/VUVIPHIM.png',
        'class': 'Vuviphim',
        'plugin': 'vuviphim.plugin',
        'version': 1
    },
    {
        'name': '[COLOR lime][B]vtv16.com[/B][/COLOR]',
        'logo': 'https://dl.dropboxusercontent.com/s/p24o3chw886ucbg/VTV16.png',
        'class': 'Vtv16',
        'plugin': 'vtv16.plugin',
        'version': 1
    },{
        'name': '[COLOR red][B]fcine.net[/B][/COLOR] dùng cho kodi 17 trở lên',
        'logo': 'https://dl.dropboxusercontent.com/s/mqjvrt7d4lcaufl/fcine.png',
        'class': 'Fcine',
        'plugin': 'fcine.plugin',
        'version': 1
    },{
        'name': '[COLOR red][B]fimfast.com[/B][/COLOR] dùng cho kodi 17 trở lên',
        'logo': 'https://dl.dropboxusercontent.com/s/5jnbn1sbrvsfixr/fimfast.png',
        'class': 'Fimfast',
        'plugin': 'fimfast.plugin',
        'version': 1
    },
]

addon_data_dir = os.path.join(xbmc.translatePath('special://userdata/addon_data').decode('utf-8'), ADDON_ID)
if not os.path.exists(addon_data_dir):
    os.makedirs(addon_data_dir)


def build_url(query):
    """build the plugin url"""
    return BASEURL + '?' + urllib.urlencode(query)


def onInit():
    xbmcplugin.setPluginCategory(HANDLE, 'My Video Collection')
    xbmcplugin.setContent(HANDLE, 'movies')
    for site in SITES:
        if site['version'] > KODI_VERSION:
            print("***********************Skip version %d" % site['version'])
            continue

        list_item = xbmcgui.ListItem(label=site['name'])
        list_item.setArt({'thumb': site['logo'], 'icon': site['logo']})
        url = build_url({'mode': 'category', 'module': site['plugin'], 'class': site['class']})
        is_folder = True
        xbmcplugin.addDirectoryItem(HANDLE, url, list_item, is_folder)

    xbmcplugin.endOfDirectory(HANDLE, cacheToDisc=True)


def list_category(cats, module, classname):
    xbmcplugin.setPluginCategory(HANDLE, classname)
    xbmcplugin.setContent(HANDLE, 'files')

    # show search link
    url = build_url({'mode': 'search', 'module': module, 'class': classname})
    xbmcplugin.addDirectoryItem(HANDLE, url,
                                xbmcgui.ListItem(label="[COLOR green][B] %s [/B][/COLOR]" % "Tìm kiếm ..."), True)

    for cat in cats:
        list_item = xbmcgui.ListItem(label=cat['title'])
        if 'subcategory' in cat and len(cat['subcategory']) > 0:
            url = build_url({'mode': 'category', 'url': cat['link'], 'name': cat['title'],
                             'subcategory': json.dumps(cat['subcategory']), 'module': module, 'class': classname})
        else:
            url = build_url({'mode': 'movies', 'url': cat['link'], 'page': 1, 'module': module, 'class': classname})
        xbmcplugin.addDirectoryItem(HANDLE, url, list_item, isFolder=True)

    xbmcplugin.endOfDirectory(HANDLE)


def list_movie(movies, link, page, module, classname):
    xbmcplugin.setPluginCategory(HANDLE, classname)
    xbmcplugin.setContent(HANDLE, 'movies')

    if movies is not None:
        for item in movies['movies']:
            try:
                list_item = xbmcgui.ListItem(label=item['label'])
                list_item.setLabel2(item['realtitle'])
                list_item.setIconImage('DefaultVideo.png')
                list_item.setArt({'thumb': item['thumb']})
                if 'poster' in item:
                    list_item.setArt({'poster': item['poster']})
                if 'intro' in item:
                    list_item.setInfo(type='video', infoLabels={'plot': item['intro']})
                url = build_url(
                    {'mode': 'movie', 'url': item['id'], 'thumb': item['thumb'], 'title': item['title'],
                     'module': module, 'class': classname})
                is_folder = True
                xbmcplugin.addDirectoryItem(HANDLE, url, list_item, is_folder)
            except:
                print(item)

        print("***********************Current page %d" % page)
        # show next page
        if movies['page'] > 1 and page < movies['page']:
            label = "Next page %d / %d >>" % (page, movies['page'])
            next_item = xbmcgui.ListItem(label=label)
            if 'page_patten' in movies and movies['page_patten'] is not None:
                link = movies['page_patten']

            url = build_url({'mode': 'movies', 'url': link, 'page': page + 1, 'module': module, 'class': classname})
            xbmcplugin.addDirectoryItem(HANDLE, url, next_item, True)
    else:
        return
    xbmcplugin.endOfDirectory(HANDLE)


def show_episode(movie, thumb, title, module, class_name):
    if len(movie['episode']) > 0:  # should not in use anymore
        for item in movie['episode']:
            li = xbmcgui.ListItem(label=item['title'])
            li.setInfo('video', {'title': item['title']})
            li.setProperty('fanart_image', thumb)
            li.setArt({'thumb': thumb})
            url = build_url({'mode': 'play',
                             'title': title,
                             'thumb': thumb,
                             'url': json.dumps(item),
                             'direct': 0,
                             'module': module,
                             'class': class_name})
            li.setProperty("IsPlayable", "true")
            xbmcplugin.addDirectoryItem(HANDLE, url, li, isFolder=True)

    elif len(movie['group']) > 0:
        idx = 0
        for key, items in movie['group'].iteritems():
            idx += 1
            label = "[COLOR red][B][---- %s : [COLOR yellow]%d eps[/COLOR] ----][/B][/COLOR]" % (key, len(items))
            sli = xbmcgui.ListItem(label=label)
            if len(items) < 2 or len(movie['group']) == 1:
                xbmcplugin.addDirectoryItem(HANDLE, None, sli, isFolder=False)
                _build_ep_list(items, title, thumb, module, class_name)
            elif idx is len(movie['group']):
                xbmcplugin.addDirectoryItem(HANDLE, None, sli, isFolder=False)
                _build_ep_list(items, title, thumb, module, class_name)
            else:
                url = build_url({'mode': 'server',
                                 'title': title,
                                 'server': key,
                                 'thumb': thumb,
                                 'items': json.dumps(items),
                                 'module': module,
                                 'class': class_name})
                xbmcplugin.addDirectoryItem(HANDLE, url, sli, isFolder=True)
    else:
        return

    xbmcplugin.setPluginCategory(HANDLE, title)
    xbmcplugin.setContent(HANDLE, 'movies')
    xbmcplugin.endOfDirectory(HANDLE)


def _build_ep_list(items, title, thumb, module, class_name):
    for item in items:
        li = xbmcgui.ListItem(label=item['title'])
        li.setInfo('video', {'title': item['title']})
        li.setProperty('fanart_image', thumb)
        li.setArt({'thumb': thumb})

        url = build_url({'mode': 'play',
                         'title': title,
                         'thumb': thumb,
                         'url': json.dumps(item),
                         'direct': 0,
                         'module': module,
                         'class': class_name})
        li.setProperty("IsPlayable", "true")
        xbmcplugin.addDirectoryItem(HANDLE, url, li, isFolder=False)


def show_server_links(items, title, thumb, server, module, class_name):
    xbmcplugin.setPluginCategory(HANDLE, "%s - %s " % (title, server))
    xbmcplugin.setContent(HANDLE, 'videos')

    label = "[COLOR red][B][---- %s : [COLOR yellow]%d eps[/COLOR] ----][/B][/COLOR]" % (server, len(items))
    sli = xbmcgui.ListItem(label=label)
    xbmcplugin.addDirectoryItem(HANDLE, None, sli, isFolder=False)
    _build_ep_list(items, title, thumb, module, class_name)
    xbmcplugin.endOfDirectory(HANDLE)


def show_links(movie, title, thumb, module, class_name):
    if len(movie['links']) == 0:
        return

    print("***********************Found Total Link %d" % len(movie['links']))
    xbmcplugin.setPluginCategory(HANDLE, title)
    xbmcplugin.setContent(HANDLE, 'movies')
    for item in movie['links']:
        li = xbmcgui.ListItem(label=item['title'])
        li.setInfo('video', {'title': item['title']})
        li.setProperty('fanart_image', thumb)
        li.setArt({'thumb': thumb})
        title = "%s - %s" % (item['title'], title)
        url = build_url({'mode': 'play',
                         'title': title,
                         'thumb': thumb,
                         'url': json.dumps(item),
                         'direct': 1,
                         'module': module,
                         'class': class_name})
        li.setProperty("IsPlayable", "true")
        xbmcplugin.addDirectoryItem(HANDLE, url, li, False)

    xbmcplugin.endOfDirectory(HANDLE)


def play(movie, title=None, thumb=None, direct=False):
    print("*********************** playing ")
    if direct:
        mediatype = MediaHelper.resolve_link(movie)
        play_item = xbmcgui.ListItem(path=movie['link'])
    else:
        if len(movie['links']) == 0:
            return
        else:
            movie = movie['links'][0]
            mediatype = MediaHelper.resolve_link(movie)
            play_item = xbmcgui.ListItem(path=movie['link'])
            try:
                title = "%s - %s" % (movie['title'].encode('utf-8'), title.encode('utf-8'))
            except:
                pass

    # if 'subtitle' in movie and movie['subtitle']:
    #     play_item.setSubtitles([movie['subtitle']])
    #
    # if mediatype == 'hls':
    #     play_item.setProperty('inputstreamaddon', 'inputstream.adaptive')
    #     play_item.setProperty('inputstream.adaptive.manifest_type', 'hls')
    #     link = movie['link'].split('|')
    #     if link and len(link) > 1:
    #         play_item.setProperty('inputstream.adaptive.stream_headers', link[1])
    #
    #     play_item.setContentLookup(False)
    # else:
    play_item.setProperty('IsPlayable', 'true')
    play_item.setLabel(title)
    play_item.setArt({'thumb': thumb})

    xbmcplugin.setResolvedUrl(HANDLE, True, listitem=play_item)


def dosearch(plugin, module, classname, text, page=1):
    xbmcplugin.setPluginCategory(HANDLE, 'Kết quả tìm kiếm')
    xbmcplugin.setContent(HANDLE, 'movies')
    if not text:
        keyboard = xbmc.Keyboard('', 'Tìm kiếm phim tại thietkeweb30s.org')
        keyboard.doModal()
        if keyboard.isConfirmed():
            text = keyboard.getText()

    if not text:
        return

    XbmcHelper.search_history_save(text)
    print("*********************** searching %s" % text)
    movies = plugin().search(text)

    if movies is not None:
        for item in movies['movies']:
            try:
                list_item = xbmcgui.ListItem(label=item['label'])
                list_item.setLabel2(item['realtitle'])
                list_item.setIconImage('DefaultVideo.png')
                list_item.setArt({
                    'thumb': item['thumb'],
                })
                url = build_url(
                    {'mode': 'movie', 'url': item['id'], 'thumb': item['thumb'], 'title': item['title'],
                     'module': module, 'class': classname})
                is_folder = True
                xbmcplugin.addDirectoryItem(HANDLE, url, list_item, is_folder)
            except:
                print(item)
    else:
        return
    xbmcplugin.endOfDirectory(HANDLE)


def search(module, classname):
    xbmcplugin.setPluginCategory(HANDLE, 'Search')
    xbmcplugin.setContent(HANDLE, 'movies')
    url = build_url({'mode': 'dosearch', 'module': module, 'class': classname})
    xbmcplugin.addDirectoryItem(HANDLE,
                                url,
                                xbmcgui.ListItem(label="[COLOR orange][B]%s[/B][/COLOR]" % "Nhập tên phim tìm kiếm ..."),
                                True)

    # Support to save search history
    contents = XbmcHelper.search_history_get()
    if contents:
        url = build_url({'mode': 'clearsearch', 'module': module, 'class': classname})
        xbmcplugin.addDirectoryItem(HANDLE,
                                    url,
                                    xbmcgui.ListItem(label="[COLOR red][B]%s[/B][/COLOR]" % "Xóa văn bản tìm kiếm ..."),
                                    True)
        for txt in contents:
            url = build_url({'mode': 'dosearch', 'module': module, 'class': classname, 'url': txt})
            xbmcplugin.addDirectoryItem(HANDLE,
                                        url,
                                        xbmcgui.ListItem(
                                            label="[COLOR blue][B]%s[/B][/COLOR]" % txt),
                                        True)
    xbmcplugin.endOfDirectory(HANDLE)


def get_plugin(arg):
    classname = ARGS.get('class', None)[0]
    module = ARGS.get('module', None)[0]
    print("*********************** Run module: %s - plugin: %s " % (module, classname))
    return getattr(import_module(module), classname), module, classname


def router():
    mode = ARGS.get('mode', None)
    instance = module = classname = None
    if mode is not None:
        instance, module, classname = get_plugin(ARGS)

    if mode is None:
        onInit()

    elif mode[0] == 'category':
        if 'subcategory' in ARGS:
            list_category(json.loads(ARGS.get('subcategory')[0]), module, classname)
        else:
            list_category(instance().getCategory(), module, classname)

    elif mode[0] == 'movies':
        link = ARGS.get('url')[0]
        page = int(ARGS.get('page')[0])
        print("*********************** Display %s page %s" % (link, page))
        movies = instance().getChannel(link, page)
        list_movie(movies, link, page, module, classname)

    elif mode[0] == 'movie':
        id = ARGS.get('url')[0]
        thumb = ARGS.get('thumb')[0]
        title = ARGS.get('title')[0]
        movie = instance().getMovie(id)
        print("*********************** Display movie %s %s" % (title, id))
        if len(movie['episode']) > 0 or len(movie['group']) > 0:
            show_episode(movie, thumb, title, module, classname)
        else:
            show_links(movie, title, thumb, module, classname)

    elif mode[0] == 'server':
        thumb = ARGS.get('thumb')[0]
        title = ARGS.get('title')[0]
        server = ARGS.get('server')[0]
        items = json.loads(ARGS.get('items')[0])
        show_server_links(items, title, thumb, server, module, classname)

    elif mode[0] == 'links':
        url = ARGS.get('url')[0]
        title = ARGS.get('title')[0]
        thumb = ARGS.get('thumb')[0]
        print("*********************** Get Movie Link %s" % url)
        movie = instance().getLink(url)
        show_links(movie, title, thumb, module, classname)

    elif mode[0] == 'play':
        print("*********************** Play movie")
        url = ARGS.get('url')[0]
        title = ARGS.get('title')[0]
        thumb = ARGS.get('thumb')[0]
        direct = int(ARGS.get('direct')[0])
        if direct is 0:
            movie = instance().getLink(json.loads(url))
        else:
            movie = json.loads(url)
        play(movie, title, thumb, direct)

    elif mode[0] == 'search':
        search(module, classname)

    elif mode[0] == 'dosearch':
        text = ARGS.get('url') and ARGS.get('url')[0] or None
        dosearch(instance, module, classname, text)

    elif mode[0] == 'clearsearch':
        XbmcHelper.search_history_clear()
        return