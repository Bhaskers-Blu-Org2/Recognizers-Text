# ------------------------------------------------------------------------------
# <auto-generated>
#     This code was generated by a tool.
#     Changes to this file may cause incorrect behavior and will be lost if
#     the code is regenerated.
# </auto-generated>
# ------------------------------------------------------------------------------

# pylint: disable=line-too-long
class BaseUrl:
    ProtocolRegex = f'((https?|ftp):\\/\\/)'
    PortRegex = f'(:\\d{{1,5}})'
    ExtractionRestrictionRegex = f'(?<=\\s|[\\\'\"\"\\(\\[:]|^)'
    UrlPrefixRegex = f'({ExtractionRestrictionRegex}{ProtocolRegex}?|{ProtocolRegex})[a-zA-Z0-9][-a-zA-Z0-9:%._\\+~#=]{{0,256}}\\.'
    UrlSuffixRegex = f'{PortRegex}?([/#][-a-zA-Z0-9:%_\\+.~#?!&//=]*)?(?![-a-zA-Z0-9:%_\\+~#?!&//=@])'
    UrlRegex = f'{UrlPrefixRegex}(?<Tld>[a-zA-Z]{{2,18}}){UrlSuffixRegex}'
    UrlRegex2 = f'((ht|f)tp(s?)\\:\\/\\/|www\\.)[0-9a-zA-Z]([-.\\w]*[0-9a-zA-Z])*(\\.(?<Tld>[0-9a-zA-Z]+))+(:(0-9)*)*(\\/?)([a-zA-Z0-9\\-\\.\\?\\,\\\'\\/\\\\\\+&amp;%\\$#_=@]*)?'
    IpUrlRegex = f'(?<IPurl>({ExtractionRestrictionRegex}{ProtocolRegex}({BaseIp.Ipv4Regex}|localhost){UrlSuffixRegex}))'
    TldList = [r'com', r'org', r'net', r'int', r'edu', r'gov', r'mil', r'academy', r'app', r'aws', r'bot', r'buy', r'cafe', r'city', r'cloud', r'company', r'eco', r'education', r'game', r'games', r'gmbh', r'law', r'limited', r'live', r'llc', r'ltd', r'ltda', r'map', r'med', r'news', r'ngo', r'ong', r'phd', r'place', r'radio', r'science', r'search', r'shopping', r'sport', r'store', r'tvs', r'wiki', r'work', r'ac', r'ad', r'ae', r'af', r'ag', r'ai', r'al', r'am', r'an', r'ao', r'aq', r'ar', r'as', r'at', r'au', r'aw', r'ax', r'az', r'ba', r'bb', r'bd', r'be', r'bf', r'bg', r'bh', r'bi', r'bj', r'bl', r'bm', r'bn', r'bo', r'bq', r'br', r'bs', r'bt', r'bv', r'bw', r'by', r'bz', r'ca', r'cc', r'cd', r'cf', r'cg', r'ch', r'ci', r'ck', r'cl', r'cm', r'cn', r'co', r'cr', r'cu', r'cv', r'cw', r'cx', r'cy', r'cz', r'de', r'dj', r'dk', r'dm', r'do', r'dz', r'ec', r'ee', r'eg', r'eh', r'er', r'es', r'et', r'eu', r'fi', r'fj', r'fk', r'fm', r'fo', r'fr', r'ga', r'gb', r'gd', r'ge', r'gf', r'gg', r'gh', r'gi', r'gl', r'gm', r'gn', r'gp', r'gq', r'gr', r'gs', r'gt', r'gu', r'gw', r'gy', r'hk', r'hm', r'hn', r'hr', r'ht', r'hu', r'id', r'ie', r'il', r'im', r'in', r'io', r'iq', r'ir', r'is', r'it', r'je', r'jm', r'jo', r'jp', r'ke', r'kg', r'kh', r'ki', r'km', r'kn', r'kp', r'kr', r'kw', r'ky', r'kz', r'la', r'lb', r'lc', r'li', r'lk', r'lr', r'ls', r'lt', r'lu', r'lv', r'ly', r'ma', r'mc', r'md', r'me', r'mf', r'mg', r'mh', r'mk', r'ml', r'mm', r'mn', r'mo', r'mp', r'mq', r'mr', r'ms', r'mt', r'mu', r'mv', r'mw', r'mx', r'my', r'mz', r'na', r'nc', r'ne', r'nf', r'ng', r'ni', r'nl', r'no', r'np', r'nr', r'nu', r'nz', r'om', r'pa', r'pe', r'pf', r'pg', r'ph', r'pk', r'pl', r'pm', r'pn', r'pr', r'ps', r'pt', r'pw', r'py', r'qa', r're', r'ro', r'rs', r'ru', r'rw', r'sa', r'sb', r'sc', r'sd', r'se', r'sg', r'sh', r'si', r'sj', r'sk', r'sl', r'sm', r'sn', r'so', r'sr', r'ss', r'st', r'su', r'sv', r'sx', r'sy', r'sz', r'tc', r'td', r'tf', r'tg', r'th', r'tj', r'tk', r'tl', r'tm', r'tn', r'to', r'tp', r'tr', r'tt', r'tv', r'tw', r'tz', r'ua', r'ug', r'uk', r'um', r'us', r'uy', r'uz', r'va', r'vc', r've', r'vg', r'vi', r'vn', r'vu', r'wf', r'ws', r'ye', r'yt', r'za', r'zm', r'zw']
# pylint: enable=line-too-long
