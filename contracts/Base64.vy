# @version 0.3.7

TABLE: constant(
    String[64]
) = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


@view
@external
def encode(data: Bytes[4096]) -> DynArray[String[4], 1366]:
    charChunks: DynArray[String[4], 1366] = []

    padBytes: uint256 = 3 - len(data) % 3
    padded: Bytes[4098] = empty(Bytes[4098])
    if padBytes == 2:
        padded = concat(data, b"\x00\x00")
    elif padBytes == 1:
        padded = concat(data, b"\x00")
    else:
        padded = data

    i: uint256 = 0
    for _ in range(4096):
        chunk: uint256 = convert(slice(padded, i, 3), uint256)

        c1: uint256 = shift(chunk, -18) & 63
        c2: uint256 = shift(chunk, -12) & 63
        c3: uint256 = shift(chunk, -6) & 63
        c4: uint256 = chunk & 63

        charChunks.append(
            concat(
                "",
                slice(TABLE, c1, 1),
                slice(TABLE, c2, 1),
                slice(TABLE, c3, 1),
                slice(TABLE, c4, 1),
            )
        )
        i += 3

        if i == len(padded):
            break

    if padBytes == 2:
        lastChunk: String[2] = slice(charChunks.pop(), 0, 2)
        charChunks.append(concat(lastChunk, "=="))
    if padBytes == 1:
        lastChunk: String[3] = slice(charChunks.pop(), 0, 3)
        charChunks.append(concat(lastChunk, "="))

    return charChunks
