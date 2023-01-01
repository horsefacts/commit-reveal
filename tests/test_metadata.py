import ape
import eth_utils

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'

def test_owner_can_set_token(cr, metadata, owner):
    metadata.setToken(cr, sender=owner)
    assert metadata.token() == cr

def test_owner_can_only_set_token_once(cr, metadata, owner):
    metadata.setToken(cr, sender=owner)
    metadata.setToken(ZERO_ADDRESS, sender=owner)
    assert metadata.token() == cr

def test_token_uri(cr, metadata, owner, receiver, chain):
    metadata.setToken(cr, sender=owner)
    commitment = eth_utils.keccak("commitment".encode('utf-8'))
    cr.commit(commitment, sender=receiver)
    chain.pending_timestamp = 1703980801
    cr.reveal(1, "commitment", sender=receiver)
    uri = metadata.tokenURI(1)
    assert uri == 'data:application/json;base64,eyJuYW1lIjoiMHhmODA5NmMzZjNjZmJhZGM5ZjNhMTA4ZDJjNTg2Y2NjODE2YzA1MTA3MTFjOGQ2MjI4YWE0ZmE1MDczMjRkMzBjIiwiZGVzY3JpcHRpb24iOiJUaGlzIHRva2VuIHJlcHJlc2VudHMgYSBoYXNoZWQgY29tbWl0bWVudCB0aGF0IGNhbiBiZSByZXZlYWxlZCBEZWNlbWJlciAzMSwgMjAyMy4iLCJpbWFnZSI6ImRhdGE6aW1hZ2Uvc3ZnK3htbDtiYXNlNjQsUEhOMlp5QjRiV3h1Y3owaWFIUjBjRG92TDNkM2R5NTNNeTV2Y21jdk1qQXdNQzl6ZG1jaUlITjBlV3hsUFNKaVlXTnJaM0p2ZFc1a09pTXhOVEUxTWpBaUlIWnBaWGRDYjNnOUlqQWdNQ0EzTURBZ016QXdJajQ4Y0dGMGFDQnBaRDBpWVNJZ1ptbHNiRDBpSXpFMU1UVXlNQ0lnWkQwaVRURXdJREV3YURZM01HRXlNQ0F4TUNBd0lEQWdNU0F4TUNBeE1IWXlOakJoTWpBZ01UQWdNQ0F3SURFdE1UQWdNVEJJTWpCaE1qQWdNVEFnTUNBd0lERXRNVEF0TVRCV01UQjZJaTgrUEhSbGVIUWdabWxzYkQwaUkyWTVOek14TmlJZ1pHOXRhVzVoYm5RdFltRnpaV3hwYm1VOUltMXBaR1JzWlNJZ1ptOXVkQzFtWVcxcGJIazlJazFsYm14dkxHMXZibTl6Y0dGalpTSWdabTl1ZEMxemFYcGxQU0l4TWlJK1BIUmxlSFJRWVhSb0lHaHlaV1k5SWlOaElqNG1JekUyTUR0RGIyMXRhWFF2VW1WMlpXRnNJREl3TWpNZ0ppTTRNakkyT3p3aFcwTkVRVlJCV3lBd2VHWTRNRGsyWXpObU0yTm1ZbUZrWXpsbU0yRXhNRGhrTW1NMU9EWmpZMk00TVRaak1EVXhNRGN4TVdNNFpEWXlNamhoWVRSbVlUVXdOek15TkdRek1HTWdNSGhtT0RBNU5tTXpaak5qWm1KaFpHTTVaak5oTVRBNFpESmpOVGcyWTJOak9ERTJZekExTVRBM01URmpPR1EyTWpJNFlXRTBabUUxTURjek1qUmtNekJqSURCNFpqZ3dPVFpqTTJZelkyWmlZV1JqT1dZellURXdPR1F5WXpVNE5tTmpZemd4Tm1Nd05URXdOekV4WXpoa05qSXlPR0ZoTkdaaE5UQTNNekkwWkRNd1l5QXdlR1k0TURrMll6Tm1NMk5tWW1Ga1l6bG1NMkV4TURoa01tTTFPRFpqWTJNNE1UWmpNRFV4TURjeE1XTTRaRFl5TWpoaFlUUm1ZVFV3TnpNeU5HUXpNR05kWFQ0OEwzUmxlSFJRWVhSb1Bqd3ZkR1Y0ZEQ0OGNHRjBhQ0JtYVd4c1BTSnlaMkpoS0RBc01Dd3dMREFwSWlCemRISnZhMlU5SWlObU9UY3pNVFlpSUdROUlrMHlNQ0F5TUdnMk5UQmhNVEFnTVRBZ01DQXdJREVnTVRBZ01UQjJNalF3WVRFd0lERXdJREFnTUNBeExURXdJREV3U0RNd1lURXdJREV3SURBZ01DQXhMVEV3TFRFd1ZqSXdlaUl2UGp4bWIzSmxhV2R1VDJKcVpXTjBJSGc5SWpVd0lpQjVQU0l6TUNJZ2QybGtkR2c5SWpZeU1DSWdhR1ZwWjJoMFBTSXlOVEFpUGp4a2FYWWdjM1I1YkdVOUltWnZiblF0Wm1GdGFXeDVPazFsYm14dkxHMXZibTl6Y0dGalpUdGpiMnh2Y2pvalptWm1PMlp2Ym5RdGMybDZaVG95TkhCNE8yUnBjM0JzWVhrNlpteGxlRHRoYkdsbmJpMXBkR1Z0Y3pwalpXNTBaWEk3YW5WemRHbG1lUzFqYjI1MFpXNTBPbU5sYm5SbGNqdG9aV2xuYUhRNk1qUXdjSGdpSUNCNGJXeHVjejBpYUhSMGNEb3ZMM2QzZHk1M015NXZjbWN2TVRrNU9TOTRhSFJ0YkNJK1BIQStZMjl0YldsMGJXVnVkRHd2Y0Q0OEwyUnBkajQ4TDJadmNtVnBaMjVQWW1wbFkzUStQQzl6ZG1jKyJ9'

def test_json(cr, metadata, owner, receiver, chain):
    metadata.setToken(cr, sender=owner)
    commitment = eth_utils.keccak("commitment".encode('utf-8'))
    cr.commit(commitment, sender=receiver)
    chain.pending_timestamp = 1703980801
    cr.reveal(1, "commitment", sender=receiver)
    json = metadata.tokenJSON(1)
    print(json)
    assert json == '{"name":"0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c","description":"This token represents a hashed commitment that can be revealed December 31, 2023.","image":"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJiYWNrZ3JvdW5kOiMxNTE1MjAiIHZpZXdCb3g9IjAgMCA3MDAgMzAwIj48cGF0aCBpZD0iYSIgZmlsbD0iIzE1MTUyMCIgZD0iTTEwIDEwaDY3MGEyMCAxMCAwIDAgMSAxMCAxMHYyNjBhMjAgMTAgMCAwIDEtMTAgMTBIMjBhMjAgMTAgMCAwIDEtMTAtMTBWMTB6Ii8+PHRleHQgZmlsbD0iI2Y5NzMxNiIgZG9taW5hbnQtYmFzZWxpbmU9Im1pZGRsZSIgZm9udC1mYW1pbHk9Ik1lbmxvLG1vbm9zcGFjZSIgZm9udC1zaXplPSIxMiI+PHRleHRQYXRoIGhyZWY9IiNhIj4mIzE2MDtDb21taXQvUmV2ZWFsIDIwMjMgJiM4MjI2OzwhW0NEQVRBWyAweGY4MDk2YzNmM2NmYmFkYzlmM2ExMDhkMmM1ODZjY2M4MTZjMDUxMDcxMWM4ZDYyMjhhYTRmYTUwNzMyNGQzMGMgMHhmODA5NmMzZjNjZmJhZGM5ZjNhMTA4ZDJjNTg2Y2NjODE2YzA1MTA3MTFjOGQ2MjI4YWE0ZmE1MDczMjRkMzBjIDB4ZjgwOTZjM2YzY2ZiYWRjOWYzYTEwOGQyYzU4NmNjYzgxNmMwNTEwNzExYzhkNjIyOGFhNGZhNTA3MzI0ZDMwYyAweGY4MDk2YzNmM2NmYmFkYzlmM2ExMDhkMmM1ODZjY2M4MTZjMDUxMDcxMWM4ZDYyMjhhYTRmYTUwNzMyNGQzMGNdXT48L3RleHRQYXRoPjwvdGV4dD48cGF0aCBmaWxsPSJyZ2JhKDAsMCwwLDApIiBzdHJva2U9IiNmOTczMTYiIGQ9Ik0yMCAyMGg2NTBhMTAgMTAgMCAwIDEgMTAgMTB2MjQwYTEwIDEwIDAgMCAxLTEwIDEwSDMwYTEwIDEwIDAgMCAxLTEwLTEwVjIweiIvPjxmb3JlaWduT2JqZWN0IHg9IjUwIiB5PSIzMCIgd2lkdGg9IjYyMCIgaGVpZ2h0PSIyNTAiPjxkaXYgc3R5bGU9ImZvbnQtZmFtaWx5Ok1lbmxvLG1vbm9zcGFjZTtjb2xvcjojZmZmO2ZvbnQtc2l6ZToyNHB4O2Rpc3BsYXk6ZmxleDthbGlnbi1pdGVtczpjZW50ZXI7anVzdGlmeS1jb250ZW50OmNlbnRlcjtoZWlnaHQ6MjQwcHgiICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHA+Y29tbWl0bWVudDwvcD48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9zdmc+"}'

def test_svg(cr, metadata, owner, receiver, chain):
    metadata.setToken(cr, sender=owner)
    commitment = eth_utils.keccak("commitment".encode('utf-8'))
    cr.commit(commitment, sender=receiver)
    chain.pending_timestamp = 1703980801
    cr.reveal(1, "commitment", sender=receiver)
    svg = metadata.tokenSVG(1)
    assert svg == '<svg xmlns="http://www.w3.org/2000/svg" style="background:#151520" viewBox="0 0 700 300"><path id="a" fill="#151520" d="M10 10h670a20 10 0 0 1 10 10v260a20 10 0 0 1-10 10H20a20 10 0 0 1-10-10V10z"/><text fill="#f97316" dominant-baseline="middle" font-family="Menlo,monospace" font-size="12"><textPath href="#a">&#160;Commit/Reveal 2023 &#8226;<![CDATA[ 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c]]></textPath></text><path fill="rgba(0,0,0,0)" stroke="#f97316" d="M20 20h650a10 10 0 0 1 10 10v240a10 10 0 0 1-10 10H30a10 10 0 0 1-10-10V20z"/><foreignObject x="50" y="30" width="620" height="250"><div style="font-family:Menlo,monospace;color:#fff;font-size:24px;display:flex;align-items:center;justify-content:center;height:240px"  xmlns="http://www.w3.org/1999/xhtml"><p>commitment</p></div></foreignObject></svg>'

def test_svg_empty_commitment(cr, metadata, owner, receiver, chain):
    metadata.setToken(cr, sender=owner)
    commitment = eth_utils.keccak("commitment".encode('utf-8'))
    cr.commit(commitment, sender=receiver)
    svg = metadata.tokenSVG(1)
    assert svg == '<svg xmlns="http://www.w3.org/2000/svg" style="background:#151520" viewBox="0 0 700 300"><path id="a" fill="#151520" d="M10 10h670a20 10 0 0 1 10 10v260a20 10 0 0 1-10 10H20a20 10 0 0 1-10-10V10z"/><text fill="#f97316" dominant-baseline="middle" font-family="Menlo,monospace" font-size="12"><textPath href="#a">&#160;Commit/Reveal 2023 &#8226;<![CDATA[ 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c]]></textPath></text><path fill="rgba(0,0,0,0)" stroke="#f97316" d="M20 20h650a10 10 0 0 1 10 10v240a10 10 0 0 1-10 10H30a10 10 0 0 1-10-10V20z"/><foreignObject x="50" y="30" width="620" height="250"><div style="font-family:Menlo,monospace;color:#fff;font-size:24px;display:flex;align-items:center;justify-content:center;height:240px"  xmlns="http://www.w3.org/1999/xhtml"><p></p></div></foreignObject></svg>'
