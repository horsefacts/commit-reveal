def test_base64(b64):
    assert b64.encode("hello world".encode('utf-8')) == ['aGVs', 'bG8g', 'd29y', 'bGQ=']
    assert b64.encode("this is a longer string".encode('utf-8')) == ['dGhp', 'cyBp', 'cyBh', 'IGxv', 'bmdl', 'ciBz', 'dHJp', 'bmc=']
