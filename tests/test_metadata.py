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
    print(uri)
    assert uri == 'data:application/json;base64,eyJuYW1lIjoiQ29tbWl0L1JldmVhbCAyMDIzIiwiZGVzY3JpcHRpb24iOiJUaGlzIHRva2VuIHJlcHJlc2VudHMgYSBoYXNoZWQgY29tbWl0bWVudCB0aGF0IGNhbiBiZSByZXZlYWxlZCAyMDIzLTEyLTMxLiIsImltYWdlIjoiZGF0YTppbWFnZS9zdmcreG1sO2Jhc2U2NCxQSE4yWnlCNGJXeHVjejBpYUhSMGNEb3ZMM2QzZHk1M015NXZjbWN2TWpBd01DOXpkbWNpSUhOMGVXeGxQU0ppWVdOclozSnZkVzVrT2lNeE5URTFNakFpSUhacFpYZENiM2c5SWpBZ01DQTNNREFnTXpBd0lqNDhjR0YwYUNCcFpEMGlZU0lnWm1sc2JEMGlJekUxTVRVeU1DSWdaRDBpVFRFd0lERXdhRFkzTUdFeU1DQXhNQ0F3SURBZ01TQXhNQ0F4TUhZeU5qQmhNakFnTVRBZ01DQXdJREV0TVRBZ01UQklNakJoTWpBZ01UQWdNQ0F3SURFdE1UQXRNVEJXTVRCNklpOCtQSFJsZUhRZ1ptbHNiRDBpSTJWbU5EUTBOQ0lnWkc5dGFXNWhiblF0WW1GelpXeHBibVU5SW0xcFpHUnNaU0lnWm05dWRDMW1ZVzFwYkhrOUlrMWxibXh2TEcxdmJtOXpjR0ZqWlNJZ1ptOXVkQzF6YVhwbFBTSXhNaUkrUEhSbGVIUlFZWFJvSUdoeVpXWTlJaU5oSWo0bUl6RTJNRHREYjIxdGFYUXZVbVYyWldGc0lESXdNak1nSmlNNE1qSTJPendoVzBORVFWUkJXeUF3ZUdZNE1EazJZek5tTTJObVltRmtZemxtTTJFeE1EaGtNbU0xT0RaalkyTTRNVFpqTURVeE1EY3hNV000WkRZeU1qaGhZVFJtWVRVd056TXlOR1F6TUdNZ01IaG1PREE1Tm1NelpqTmpabUpoWkdNNVpqTmhNVEE0WkRKak5UZzJZMk5qT0RFMll6QTFNVEEzTVRGak9HUTJNakk0WVdFMFptRTFNRGN6TWpSa016QmpJREI0Wmpnd09UWmpNMll6WTJaaVlXUmpPV1l6WVRFd09HUXlZelU0Tm1Oall6Z3hObU13TlRFd056RXhZemhrTmpJeU9HRmhOR1poTlRBM016STBaRE13WXlBd2VHWTRNRGsyWXpObU0yTm1ZbUZrWXpsbU0yRXhNRGhrTW1NMU9EWmpZMk00TVRaak1EVXhNRGN4TVdNNFpEWXlNamhoWVRSbVlUVXdOek15TkdRek1HTmRYVDQ4TDNSbGVIUlFZWFJvUGp3dmRHVjRkRDQ4Y0dGMGFDQm1hV3hzUFNKeVoySmhLREFzTUN3d0xEQXBJaUJ6ZEhKdmEyVTlJaU5sWmpRME5EUWlJR1E5SWsweU1DQXlNR2cyTlRCaE1UQWdNVEFnTUNBd0lERWdNVEFnTVRCMk1qUXdZVEV3SURFd0lEQWdNQ0F4TFRFd0lERXdTRE13WVRFd0lERXdJREFnTUNBeExURXdMVEV3VmpJd2VpSXZQanhtYjNKbGFXZHVUMkpxWldOMElIZzlJalV3SWlCNVBTSXpNQ0lnZDJsa2RHZzlJall5TUNJZ2FHVnBaMmgwUFNJeU5UQWlQanhrYVhZZ2MzUjViR1U5SW1admJuUXRabUZ0YVd4NU9rMWxibXh2TEcxdmJtOXpjR0ZqWlR0amIyeHZjam9qWm1abU8yWnZiblF0YzJsNlpUb3lOSEI0TzJScGMzQnNZWGs2Wm14bGVEdGhiR2xuYmkxcGRHVnRjenBqWlc1MFpYSTdhblZ6ZEdsbWVTMWpiMjUwWlc1ME9tTmxiblJsY2p0b1pXbG5hSFE2TWpRd2NIZ2lJQ0I0Yld4dWN6MGlhSFIwY0RvdkwzZDNkeTUzTXk1dmNtY3ZNVGs1T1M5NGFIUnRiQ0krUEhBK1kyOXRiV2wwYldWdWREd3ZjRDQ4TDJScGRqNDhMMlp2Y21WcFoyNVBZbXBsWTNRK1BDOXpkbWMrIn0='

def test_json(cr, metadata, owner, receiver, chain):
    metadata.setToken(cr, sender=owner)
    commitment = eth_utils.keccak("commitment".encode('utf-8'))
    cr.commit(commitment, sender=receiver)
    chain.pending_timestamp = 1703980801
    cr.reveal(1, "commitment", sender=receiver)
    json = metadata.tokenJSON(1)
    assert json == '{"name":"Commit/Reveal 2023","description":"This token represents a hashed commitment that can be revealed 2023-12-31.","image":"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJiYWNrZ3JvdW5kOiMxNTE1MjAiIHZpZXdCb3g9IjAgMCA3MDAgMzAwIj48cGF0aCBpZD0iYSIgZmlsbD0iIzE1MTUyMCIgZD0iTTEwIDEwaDY3MGEyMCAxMCAwIDAgMSAxMCAxMHYyNjBhMjAgMTAgMCAwIDEtMTAgMTBIMjBhMjAgMTAgMCAwIDEtMTAtMTBWMTB6Ii8+PHRleHQgZmlsbD0iI2VmNDQ0NCIgZG9taW5hbnQtYmFzZWxpbmU9Im1pZGRsZSIgZm9udC1mYW1pbHk9Ik1lbmxvLG1vbm9zcGFjZSIgZm9udC1zaXplPSIxMiI+PHRleHRQYXRoIGhyZWY9IiNhIj4mIzE2MDtDb21taXQvUmV2ZWFsIDIwMjMgJiM4MjI2OzwhW0NEQVRBWyAweGY4MDk2YzNmM2NmYmFkYzlmM2ExMDhkMmM1ODZjY2M4MTZjMDUxMDcxMWM4ZDYyMjhhYTRmYTUwNzMyNGQzMGMgMHhmODA5NmMzZjNjZmJhZGM5ZjNhMTA4ZDJjNTg2Y2NjODE2YzA1MTA3MTFjOGQ2MjI4YWE0ZmE1MDczMjRkMzBjIDB4ZjgwOTZjM2YzY2ZiYWRjOWYzYTEwOGQyYzU4NmNjYzgxNmMwNTEwNzExYzhkNjIyOGFhNGZhNTA3MzI0ZDMwYyAweGY4MDk2YzNmM2NmYmFkYzlmM2ExMDhkMmM1ODZjY2M4MTZjMDUxMDcxMWM4ZDYyMjhhYTRmYTUwNzMyNGQzMGNdXT48L3RleHRQYXRoPjwvdGV4dD48cGF0aCBmaWxsPSJyZ2JhKDAsMCwwLDApIiBzdHJva2U9IiNlZjQ0NDQiIGQ9Ik0yMCAyMGg2NTBhMTAgMTAgMCAwIDEgMTAgMTB2MjQwYTEwIDEwIDAgMCAxLTEwIDEwSDMwYTEwIDEwIDAgMCAxLTEwLTEwVjIweiIvPjxmb3JlaWduT2JqZWN0IHg9IjUwIiB5PSIzMCIgd2lkdGg9IjYyMCIgaGVpZ2h0PSIyNTAiPjxkaXYgc3R5bGU9ImZvbnQtZmFtaWx5Ok1lbmxvLG1vbm9zcGFjZTtjb2xvcjojZmZmO2ZvbnQtc2l6ZToyNHB4O2Rpc3BsYXk6ZmxleDthbGlnbi1pdGVtczpjZW50ZXI7anVzdGlmeS1jb250ZW50OmNlbnRlcjtoZWlnaHQ6MjQwcHgiICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHA+Y29tbWl0bWVudDwvcD48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9zdmc+"}'

def test_svg(cr, metadata, owner, receiver, chain):
    metadata.setToken(cr, sender=owner)
    commitment = eth_utils.keccak("commitment".encode('utf-8'))
    cr.commit(commitment, sender=receiver)
    chain.pending_timestamp = 1703980801
    cr.reveal(1, "commitment", sender=receiver)
    svg = metadata.tokenSVG(1)
    assert svg == '<svg xmlns="http://www.w3.org/2000/svg" style="background:#151520" viewBox="0 0 700 300"><path id="a" fill="#151520" d="M10 10h670a20 10 0 0 1 10 10v260a20 10 0 0 1-10 10H20a20 10 0 0 1-10-10V10z"/><text fill="#ef4444" dominant-baseline="middle" font-family="Menlo,monospace" font-size="12"><textPath href="#a">&#160;Commit/Reveal 2023 &#8226;<![CDATA[ 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c]]></textPath></text><path fill="rgba(0,0,0,0)" stroke="#ef4444" d="M20 20h650a10 10 0 0 1 10 10v240a10 10 0 0 1-10 10H30a10 10 0 0 1-10-10V20z"/><foreignObject x="50" y="30" width="620" height="250"><div style="font-family:Menlo,monospace;color:#fff;font-size:24px;display:flex;align-items:center;justify-content:center;height:240px"  xmlns="http://www.w3.org/1999/xhtml"><p>commitment</p></div></foreignObject></svg>'

def test_svg_empty_commitment(cr, metadata, owner, receiver, chain):
    metadata.setToken(cr, sender=owner)
    commitment = eth_utils.keccak("commitment".encode('utf-8'))
    cr.commit(commitment, sender=receiver)
    svg = metadata.tokenSVG(1)
    assert svg == '<svg xmlns="http://www.w3.org/2000/svg" style="background:#151520" viewBox="0 0 700 300"><path id="a" fill="#151520" d="M10 10h670a20 10 0 0 1 10 10v260a20 10 0 0 1-10 10H20a20 10 0 0 1-10-10V10z"/><text fill="#ef4444" dominant-baseline="middle" font-family="Menlo,monospace" font-size="12"><textPath href="#a">&#160;Commit/Reveal 2023 &#8226;<![CDATA[ 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c 0xf8096c3f3cfbadc9f3a108d2c586ccc816c0510711c8d6228aa4fa507324d30c]]></textPath></text><path fill="rgba(0,0,0,0)" stroke="#ef4444" d="M20 20h650a10 10 0 0 1 10 10v240a10 10 0 0 1-10 10H30a10 10 0 0 1-10-10V20z"/><foreignObject x="50" y="30" width="620" height="250"><div style="font-family:Menlo,monospace;color:#fff;font-size:24px;display:flex;align-items:center;justify-content:center;height:240px"  xmlns="http://www.w3.org/1999/xhtml"><p></p></div></foreignObject></svg>'
